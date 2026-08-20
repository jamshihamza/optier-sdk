from __future__ import annotations

from datetime import datetime, timezone
import logging
import threading
import time
from typing import Callable

from ..domain.media import (
    StreamMetrics,
    StreamSession,
    StreamState,
    VideoFrame,
)
from .interfaces import IFrameSink, IStreamSource, IVideoDecoder
from .ring_buffer import BoundedFrameBuffer

logger = logging.getLogger("optier_vms.media.stream_worker")


class StreamWorker:
    """
    Isolated Stream Worker Thread.

    Manages connection lifecycle, frame acquisition loop, software decoding,
    backpressure handling via bounded ring buffer, and exponential reconnection backoff.
    """

    def __init__(
        self,
        session: StreamSession,
        source: IStreamSource,
        decoder: IVideoDecoder,
        buffer_capacity: int = 1,
        max_reconnect_backoff_sec: float = 16.0,
    ) -> None:
        self.session = session
        self.source = source
        self.decoder = decoder
        self.buffer = BoundedFrameBuffer[VideoFrame](maxsize=buffer_capacity)
        self._max_backoff = max_reconnect_backoff_sec
        self._current_backoff = 1.0

        self._sinks: list[IFrameSink] = []
        self._frame_callbacks: list[Callable[[VideoFrame], None]] = []

        self._stop_event = threading.Event()
        self._thread: threading.Thread | None = None
        self._lock = threading.Lock()

        # FPS Tracking
        self._fps_window_start = time.time()
        self._fps_window_frames = 0

    def add_sink(self, sink: IFrameSink) -> None:
        with self._lock:
            if sink not in self._sinks:
                self._sinks.append(sink)

    def remove_sink(self, sink: IFrameSink) -> None:
        with self._lock:
            if sink in self._sinks:
                self._sinks.remove(sink)

    def add_frame_callback(self, callback: Callable[[VideoFrame], None]) -> None:
        with self._lock:
            self._frame_callbacks.append(callback)

    def start(self) -> None:
        """
        Start the background stream worker thread.
        """
        with self._lock:
            if self._thread is not None and self._thread.is_alive():
                return

            self._stop_event.clear()
            self._thread = threading.Thread(
                target=self._run_loop,
                name=f"StreamWorker-CH{self.session.channel_index}",
                daemon=True,
            )
            self._thread.start()

    def stop(self, timeout: float = 3.0) -> None:
        """
        Signal the worker to stop, close transport and buffer, and join thread.
        """
        self._stop_event.set()
        self.buffer.close()

        if self._thread is not None and self._thread.is_alive():
            self._thread.join(timeout=timeout)
            self._thread = None

        self.source.close()
        self.decoder.close()
        self.session.state = StreamState.DISCONNECTED

    def _run_loop(self) -> None:
        """
        Main worker execution loop with state management and reconnect backoff.
        """
        self.session.started_at = datetime.now(timezone.utc)
        self.session.state = StreamState.CONNECTING

        while not self._stop_event.is_set():
            # 1. Connect
            self.session.state = StreamState.CONNECTING
            logger.debug("Connecting stream for channel %d...", self.session.channel_index)

            if not self.source.open():
                self._handle_reconnect("Failed to connect to stream source")
                continue

            self.session.state = StreamState.CONNECTED
            self.decoder.reset()
            self._current_backoff = 1.0  # Reset backoff on successful connect
            logger.info("Stream connected for channel %d (%s)", self.session.channel_index, self.source.endpoint)

            # 2. Read & Decode Loop
            frame_num = 0
            while not self._stop_event.is_set():
                ret, raw_data = self.source.read_frame()
                if not ret or raw_data is None:
                    logger.warning("Stream read failure on channel %d", self.session.channel_index)
                    break

                self.session.metrics.record_received()

                # Decode
                decoded_frame = self.decoder.decode(raw_data, frame_number=frame_num + 1)
                if decoded_frame is None:
                    self.session.metrics.record_decode_error()
                    continue

                frame_num += 1
                self.session.state = StreamState.STREAMING
                self.session.last_frame_at = decoded_frame.timestamp
                self.session.metrics.record_decoded()

                # Update observed FPS
                self._update_fps()

                # Push to bounded buffer (drops oldest unread frame if full)
                prev_drops = self.buffer.dropped_count
                self.buffer.push(decoded_frame)
                new_drops = self.buffer.dropped_count
                if new_drops > prev_drops:
                    self.session.metrics.record_drop(new_drops - prev_drops)

                # Dispatch to sinks & callbacks
                self._dispatch_frame(decoded_frame)

            # 3. Handle stream loss / reconnect
            if not self._stop_event.is_set():
                self.source.close()
                self._handle_reconnect("Stream connection lost during playback")

        # Clean exit
        self.source.close()
        self.session.state = StreamState.DISCONNECTED
        logger.debug("Stream worker stopped for channel %d", self.session.channel_index)

    def _handle_reconnect(self, reason: str) -> None:
        """
        Transition to RECONNECTING state and sleep with exponential backoff.
        """
        self.session.state = StreamState.RECONNECTING
        self.session.error_message = reason
        self.session.metrics.record_reconnect()

        logger.info(
            "Channel %d reconnecting (attempt #%d) in %.1fs: %s",
            self.session.channel_index,
            self.session.metrics.reconnect_count,
            self._current_backoff,
            reason,
        )

        # Controlled sleep that wakes immediately on stop_event
        self._stop_event.wait(timeout=self._current_backoff)

        # Exponential backoff up to max_backoff
        self._current_backoff = min(self._current_backoff * 2.0, self._max_backoff)

    def _update_fps(self) -> None:
        now = time.time()
        self._fps_window_frames += 1
        elapsed = now - self._fps_window_start
        if elapsed >= 1.0:
            current_fps = self._fps_window_frames / elapsed
            self.session.metrics.fps_decoded = round(current_fps, 2)
            self._fps_window_frames = 0
            self._fps_window_start = now

        if self.session.started_at is not None:
            uptime = (datetime.now(timezone.utc) - self.session.started_at).total_seconds()
            self.session.metrics.uptime_seconds = round(uptime, 2)

    def _dispatch_frame(self, frame: VideoFrame) -> None:
        with self._lock:
            sinks = list(self._sinks)
            callbacks = list(self._frame_callbacks)

        for sink in sinks:
            try:
                sink.on_frame(frame)
            except Exception as exc:
                logger.error("Error in frame sink: %s", exc)

        for cb in callbacks:
            try:
                cb(frame)
            except Exception as exc:
                logger.error("Error in frame callback: %s", exc)
