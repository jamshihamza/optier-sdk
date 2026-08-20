from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from enum import Enum
import uuid
from typing import Any

from .channel import StreamType


class StreamState(str, Enum):
    DISCONNECTED = "DISCONNECTED"
    CONNECTING = "CONNECTING"
    CONNECTED = "CONNECTED"
    STREAMING = "STREAMING"
    DEGRADED = "DEGRADED"
    RECONNECTING = "RECONNECTING"
    ERROR = "ERROR"


class PixelFormat(str, Enum):
    BGR24 = "BGR24"
    RGB24 = "RGB24"
    RGBA32 = "RGBA32"
    BGRA32 = "BGRA32"
    GRAY8 = "GRAY8"
    YUV420P = "YUV420P"


@dataclass(frozen=True)
class StreamRequest:
    """
    Specification for requesting a live video stream from a device channel.
    """

    device_id: uuid.UUID
    channel_index: int
    stream_type: StreamType = StreamType.SUB

    @property
    def stream_key(self) -> str:
        """
        Unique key identifying this stream request (e.g. 'dev-uuid:CH1:sub').
        """
        return f"{self.device_id}:CH{self.channel_index}:{self.stream_type.value}"


@dataclass
class VideoFrame:
    """
    VMS-Owned Video Frame Representation.

    Encapsulates decoded image payload with dimensions, pixel format,
    timestamps, and frame counter. Independent from any specific GUI or decoder library.
    """

    width: int
    height: int
    pixel_format: PixelFormat
    timestamp: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
    frame_number: int = 0
    data: Any = field(default=None, repr=False)
    duration_ms: float = 0.0

    @property
    def byte_size(self) -> int:
        """
        Returns estimated size of the frame buffer in bytes.
        """
        if hasattr(self.data, "nbytes"):
            return int(self.data.nbytes)
        if isinstance(self.data, (bytes, bytearray, memoryview)):
            return len(self.data)
        return self.width * self.height * 3

    @property
    def aspect_ratio(self) -> float:
        return self.width / self.height if self.height > 0 else 1.0


@dataclass
class StreamMetrics:
    """
    Real-time telemetry and health statistics for a video stream session.
    """

    frames_received: int = 0
    frames_decoded: int = 0
    dropped_frames: int = 0
    decode_errors: int = 0
    reconnect_count: int = 0
    last_frame_timestamp: datetime | None = None
    fps_received: float = 0.0
    fps_decoded: float = 0.0
    uptime_seconds: float = 0.0
    latency_estimate_ms: float = 0.0

    def record_received(self) -> None:
        self.frames_received += 1

    def record_decoded(self) -> None:
        self.frames_decoded += 1
        self.last_frame_timestamp = datetime.now(timezone.utc)

    def record_drop(self, count: int = 1) -> None:
        self.dropped_frames += count

    def record_decode_error(self) -> None:
        self.decode_errors += 1

    def record_reconnect(self) -> None:
        self.reconnect_count += 1


@dataclass
class StreamSession:
    """
    VMS Live Stream Session Model.

    Tracks connection state, endpoint metadata, metrics, and health of an active stream.
    """

    id: uuid.UUID = field(default_factory=uuid.uuid4)
    device_id: uuid.UUID = field(default_factory=uuid.uuid4)
    channel_index: int = 1
    stream_type: StreamType = StreamType.SUB
    endpoint: str = "rtsp://..."
    state: StreamState = StreamState.DISCONNECTED
    started_at: datetime | None = None
    last_frame_at: datetime | None = None
    metrics: StreamMetrics = field(default_factory=StreamMetrics)
    error_message: str | None = None

    @property
    def is_active(self) -> bool:
        return self.state in (StreamState.CONNECTED, StreamState.STREAMING, StreamState.DEGRADED)
