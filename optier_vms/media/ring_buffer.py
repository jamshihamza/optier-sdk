from __future__ import annotations

from collections import deque
import threading
from typing import Generic, TypeVar

from ..domain.media import VideoFrame

T = TypeVar("T", bound=VideoFrame)


class BoundedFrameBuffer(Generic[T]):
    """
    Thread-Safe Bounded Latest-Frame Ring Buffer.

    Implements a strict bounded-capacity queue (default capacity = 1 or 2)
    with LATEST-FRAME-OVERWRITE behavior to eliminate video latency.
    When full, incoming frames overwrite the oldest unconsumed frame.
    """

    def __init__(self, maxsize: int = 1) -> None:
        if maxsize < 1:
            raise ValueError("Buffer capacity must be at least 1")
        self._maxsize = maxsize
        self._queue: deque[T] = deque(maxlen=maxsize)
        self._lock = threading.Lock()
        self._not_empty = threading.Condition(self._lock)
        self._closed = False
        self._dropped_count = 0
        self._pushed_count = 0
        self._consumed_count = 0

    @property
    def capacity(self) -> int:
        return self._maxsize

    @property
    def size(self) -> int:
        with self._lock:
            return len(self._queue)

    @property
    def is_empty(self) -> bool:
        with self._lock:
            return len(self._queue) == 0

    @property
    def is_closed(self) -> bool:
        with self._lock:
            return self._closed

    @property
    def dropped_count(self) -> int:
        with self._lock:
            return self._dropped_count

    @property
    def pushed_count(self) -> int:
        with self._lock:
            return self._pushed_count

    @property
    def consumed_count(self) -> int:
        with self._lock:
            return self._consumed_count

    def push(self, frame: T) -> bool:
        """
        Push a new video frame into the buffer.
        If buffer is at full capacity, the oldest unconsumed frame is discarded
        and dropped_count is incremented.

        :return: True if frame was stored, False if buffer is closed.
        """
        with self._lock:
            if self._closed:
                return False

            if len(self._queue) == self._maxsize:
                # Discard oldest frame to make room for newest frame
                self._queue.popleft()
                self._dropped_count += 1

            self._queue.append(frame)
            self._pushed_count += 1
            self._not_empty.notify()
            return True

    def get(self, timeout: float | None = None) -> T | None:
        """
        Retrieve and remove the oldest available frame from the buffer.
        Blocks until a frame arrives, timeout expires, or buffer is closed.

        :param timeout: Timeout in seconds (None for indefinite wait).
        :return: VideoFrame or None if timed out / closed.
        """
        with self._not_empty:
            while len(self._queue) == 0:
                if self._closed:
                    return None
                if not self._not_empty.wait(timeout=timeout):
                    return None  # Timed out

            if self._closed and len(self._queue) == 0:
                return None

            frame = self._queue.popleft()
            self._consumed_count += 1
            return frame

    def peek(self) -> T | None:
        """
        Inspect the newest frame currently in the buffer without removing it.

        :return: VideoFrame or None if empty.
        """
        with self._lock:
            if not self._queue or self._closed:
                return None
            return self._queue[-1]

    def clear(self) -> None:
        """
        Discard all pending frames in the buffer.
        """
        with self._lock:
            self._queue.clear()

    def close(self) -> None:
        """
        Close the buffer and wake up any waiting consumers.
        """
        with self._lock:
            self._closed = True
            self._not_empty.notify_all()
