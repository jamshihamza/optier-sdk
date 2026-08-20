from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
import uuid
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from .device import Device


class StreamType(str, Enum):
    MAIN = "main"
    SUB = "sub"
    MOBILE = "mobile"


class AICapability(str, Enum):
    FACE_DETECTION = "FACE_DETECTION"
    FACE_RECOGNITION = "FACE_RECOGNITION"
    LICENSE_PLATE_DETECTION = "LICENSE_PLATE_DETECTION"
    LINE_CROSSING = "LINE_CROSSING"
    PERIMETER_INTRUSION = "PERIMETER_INTRUSION"
    STATIONARY_OBJECT = "STATIONARY_OBJECT"
    PEDESTRIAN_DETECTION = "PEDESTRIAN_DETECTION"
    CROSS_COUNTING = "CROSS_COUNTING"
    SOUND_DETECTION = "SOUND_DETECTION"
    OCCLUSION_DETECTION = "OCCLUSION_DETECTION"


@dataclass
class CameraChannel:
    """
    VMS Camera Channel Domain Model.

    Represents a logical video channel (1..256) belonging to a physical device.
    """

    id: uuid.UUID = field(default_factory=uuid.uuid4)
    device_id: uuid.UUID = field(default_factory=uuid.uuid4)
    channel_index: int = 1
    name: str = "Camera"
    online: bool = False
    ptz_supported: bool = False
    ai_capabilities: set[AICapability] = field(default_factory=set)
    rtsp_main_url: str | None = None
    rtsp_sub_url: str | None = None
    current_status: str = "Offline"
    raw_info: dict[str, Any] = field(default_factory=dict)

    @property
    def channel_key(self) -> str:
        """
        Returns the OEM formatted channel identifier (e.g. 'CH1', 'CH36').
        """
        return f"CH{self.channel_index}"

    def supports_ai(self, capability: AICapability) -> bool:
        """
        Check if this camera channel supports a specific AI analytics capability.
        """
        return capability in self.ai_capabilities
