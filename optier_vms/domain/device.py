from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
import uuid
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from .channel import CameraChannel
    from optier_sdk import Camera


class DeviceType(str, Enum):
    NVR = "NVR"
    IPC = "IPC"
    DVR = "DVR"
    UNKNOWN = "UNKNOWN"


class ConnectionState(str, Enum):
    DISCONNECTED = "DISCONNECTED"
    CONNECTING = "CONNECTING"
    AUTHENTICATING = "AUTHENTICATING"
    SYNCHRONIZING = "SYNCHRONIZING"
    ONLINE = "ONLINE"
    DEGRADED = "DEGRADED"
    AUTH_FAILED = "AUTH_FAILED"
    ERROR = "ERROR"


@dataclass
class DeviceInfo:
    """
    Hardware and firmware information about a physical device.
    """

    model: str = "Unknown"
    serial_number: str = "Unknown"
    firmware_version: str = "Unknown"
    hardware_version: str = "Unknown"
    mac_address: str = "Unknown"
    channel_capacity: int = 1
    analog_channel_count: int = 0
    ip_channel_count: int = 0
    raw_details: dict[str, Any] = field(default_factory=dict)


@dataclass
class Device:
    """
    VMS Device Domain Model.

    Represents a physical NVR, DVR, or standalone IP Camera connected to the VMS.
    """

    id: uuid.UUID = field(default_factory=uuid.uuid4)
    name: str = "New Device"
    host: str = "127.0.0.1"
    port: int = 80
    username: str = "admin"
    password: str = ""
    device_type: DeviceType = DeviceType.NVR
    state: ConnectionState = ConnectionState.DISCONNECTED
    info: DeviceInfo = field(default_factory=DeviceInfo)
    channels: dict[int, CameraChannel] = field(default_factory=dict)
    camera_client: Any | None = field(default=None, repr=False)
    error_message: str | None = None

    def add_channel(self, channel: CameraChannel) -> None:
        """
        Add a camera channel to this device's inventory.
        """
        self.channels[channel.channel_index] = channel

    def get_channel(self, channel_index: int) -> CameraChannel | None:
        """
        Get a camera channel by its 1-based channel index.
        """
        return self.channels.get(channel_index)

    @property
    def online_channel_count(self) -> int:
        return sum(1 for ch in self.channels.values() if ch.online)
