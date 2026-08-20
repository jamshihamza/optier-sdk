from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from enum import Enum
import uuid
from typing import Any


class EventSeverity(str, Enum):
    INFO = "INFO"
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"
    CRITICAL = "CRITICAL"


class EventType(str, Enum):
    MOTION = "MOTION"
    PIR = "PIR"
    IO_ALARM = "IO_ALARM"
    FACE_MATCH = "FACE_MATCH"
    FACE_STRANGER = "FACE_STRANGER"
    LPR_MATCH = "LPR_MATCH"
    LPR_BLOCKLIST = "LPR_BLOCKLIST"
    LINE_CROSSING = "LINE_CROSSING"
    PERIMETER_INTRUSION = "PERIMETER_INTRUSION"
    STATIONARY_OBJECT = "STATIONARY_OBJECT"
    PEDESTRIAN_DETECTION = "PEDESTRIAN_DETECTION"
    CROSS_COUNTING = "CROSS_COUNTING"
    SOUND_DETECTION = "SOUND_DETECTION"
    OCCLUSION_DETECTION = "OCCLUSION_DETECTION"
    DEVICE_OFFLINE = "DEVICE_OFFLINE"
    DEVICE_ONLINE = "DEVICE_ONLINE"
    DISK_ERROR = "DISK_ERROR"
    SYSTEM_EXCEPTION = "SYSTEM_EXCEPTION"


@dataclass
class VMSEvent:
    """
    VMS Normalized Event Model.

    Normalized representation of real-time alarms, video analytics triggers,
    and system status notifications across all devices.
    """

    id: uuid.UUID = field(default_factory=uuid.uuid4)
    device_id: uuid.UUID = field(default_factory=uuid.uuid4)
    channel_index: int | None = None
    event_type: EventType = EventType.MOTION
    severity: EventSeverity = EventSeverity.INFO
    timestamp: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
    acknowledged: bool = False
    source_name: str = "System"
    description: str = ""
    snapshot_base64: str | None = None
    metadata: dict[str, Any] = field(default_factory=dict)
    raw_payload: dict[str, Any] = field(default_factory=dict)

    def acknowledge(self) -> None:
        """
        Mark this event as acknowledged by a VMS operator.
        """
        self.acknowledged = True
