from __future__ import annotations

import logging
import threading
import uuid

from ..domain.channel import StreamType
from ..domain.device import ConnectionState, Device
from ..domain.media import (
    StreamMetrics,
    StreamRequest,
    StreamSession,
    StreamState,
    VideoFrame,
)
from ..media.interfaces import IFrameSink, IStreamSource, IVideoDecoder
from ..media.rtsp_source import RtspStreamSource, sanitize_rtsp_url
from ..media.software_decoder import SoftwareVideoDecoder
from ..media.stream_worker import StreamWorker
from .device_service import DeviceService

logger = logging.getLogger("optier_vms.services.stream_service")


class StreamService:
    """
    VMS Media Plane Stream Manager.

    Coordinates concurrent RTSP stream sessions across multi-channel devices (1..256 channels).
    Provides strict failure isolation per stream and per device.
    """

    def __init__(self, device_service: DeviceService) -> None:
        self._device_service = device_service
        self._workers: dict[str, StreamWorker] = {}
        self._lock = threading.RLock()

    def start_stream(
        self,
        request: StreamRequest,
        sink: IFrameSink | None = None,
        custom_source: IStreamSource | None = None,
        custom_decoder: IVideoDecoder | None = None,
        buffer_capacity: int = 1,
    ) -> StreamSession | None:
        """
        Start live video streaming for a specific camera channel.
        """
        key = request.stream_key

        with self._lock:
            # If stream is already active, attach sink and return existing session
            if key in self._workers:
                worker = self._workers[key]
                if sink is not None:
                    worker.add_sink(sink)
                return worker.session

            # 1. Resolve Device and Build RTSP Endpoint
            device = self._device_service.get_device(request.device_id)
            if not device:
                logger.error("Cannot start stream: Device %s not found in registry", request.device_id)
                return None

            rtsp_url = self._resolve_rtsp_url(device, request.channel_index, request.stream_type)
            sanitized_url = sanitize_rtsp_url(rtsp_url)

            # 2. Construct Session
            session = StreamSession(
                device_id=request.device_id,
                channel_index=request.channel_index,
                stream_type=request.stream_type,
                endpoint=sanitized_url,
                state=StreamState.CONNECTING,
            )

            # 3. Create Transport & Decoder
            source = custom_source if custom_source is not None else RtspStreamSource(rtsp_url=rtsp_url)
            decoder = custom_decoder if custom_decoder is not None else SoftwareVideoDecoder()

            # 4. Instantiate Worker
            worker = StreamWorker(
                session=session,
                source=source,
                decoder=decoder,
                buffer_capacity=buffer_capacity,
            )

            if sink is not None:
                worker.add_sink(sink)

            self._workers[key] = worker

        # 5. Start Worker Thread
        worker.start()
        logger.info("Live stream started: %s (%s)", key, sanitized_url)
        return session

    def stop_stream(self, request: StreamRequest) -> bool:
        """
        Stop an active stream session and release all decoding resources.
        """
        key = request.stream_key
        with self._lock:
            worker = self._workers.pop(key, None)

        if not worker:
            return False

        worker.stop()
        logger.info("Live stream stopped: %s", key)
        return True

    def restart_stream(self, request: StreamRequest) -> StreamSession | None:
        """
        Restart an existing or failed stream session.
        """
        self.stop_stream(request)
        return self.start_stream(request)

    def get_stream(self, request: StreamRequest) -> StreamSession | None:
        """
        Retrieve the current StreamSession for a channel.
        """
        with self._lock:
            worker = self._workers.get(request.stream_key)
            return worker.session if worker else None

    def get_latest_frame(self, request: StreamRequest) -> VideoFrame | None:
        """
        Retrieve the most recent video frame from the bounded buffer.
        """
        with self._lock:
            worker = self._workers.get(request.stream_key)
            if not worker:
                return None
            return worker.buffer.peek()

    def get_metrics(self, request: StreamRequest) -> StreamMetrics | None:
        """
        Retrieve real-time metrics for an active stream session.
        """
        session = self.get_stream(request)
        return session.metrics if session else None

    def list_active_streams(self) -> list[StreamSession]:
        """
        List all currently active stream sessions.
        """
        with self._lock:
            return [worker.session for worker in self._workers.values()]

    def stream_count(self) -> int:
        """
        Count of active stream sessions.
        """
        with self._lock:
            return len(self._workers)

    def stop_all(self) -> None:
        """
        Stop all active streams across all devices during VMS shutdown.
        """
        with self._lock:
            active_workers = list(self._workers.values())
            self._workers.clear()

        for worker in active_workers:
            try:
                worker.stop()
            except Exception as exc:
                logger.warning("Error stopping worker %s: %s", worker.session.channel_index, exc)

        logger.info("All live streams stopped successfully (%d streams).", len(active_workers))

    def _resolve_rtsp_url(self, device: Device, channel_index: int, stream_type: StreamType) -> str:
        """
        Construct the authenticated RTSP stream URL for a given channel and stream subtype.
        """
        subtype = 0
        if stream_type == StreamType.SUB:
            subtype = 1
        elif stream_type == StreamType.MOBILE:
            subtype = 2

        # Format: rtsp://username:password@host:port/rtsp/streaming?channel=1&subtype=1
        return (
            f"rtsp://{device.username}:{device.password}@"
            f"{device.host}:{device.port}/rtsp/streaming?"
            f"channel={channel_index}&subtype={subtype}"
        )
