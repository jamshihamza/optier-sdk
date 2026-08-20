"""
OPTIER VMS Domain Entities and Enumerations.
"""

from .device import (
    Device,
    DeviceType,
    ConnectionState,
    DeviceInfo,
)
from .channel import (
    CameraChannel,
    StreamType,
    AICapability,
)
from .event import (
    VMSEvent,
    EventType,
    EventSeverity,
)
from .evidence import (
    EvidenceItem,
    ForensicTag,
    ForensicTagType,
)
from .user import (
    VMSUser,
    Role,
    Operation,
    ChannelPermission,
)

__all__ = [
    "Device",
    "DeviceType",
    "ConnectionState",
    "DeviceInfo",
    "CameraChannel",
    "StreamType",
    "AICapability",
    "VMSEvent",
    "EventType",
    "EventSeverity",
    "EvidenceItem",
    "ForensicTag",
    "ForensicTagType",
    "VMSUser",
    "Role",
    "Operation",
    "ChannelPermission",
]
