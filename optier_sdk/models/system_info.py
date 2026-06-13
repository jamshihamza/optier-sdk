from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

@dataclass(slots=True)
class SystemInfo:
    device_id: str | None = None
    device_name: str | None = None
    device_type: str | None = None
    hardware_version: str | None = None
    software_version: str | None = None
    build_time: str | None = None
    ie_client_version: str | None = None
    mcu_software_version: str | None = None
    video_format: str | None = None
    hdd_volume: str | None = None
    ip_address: str | None = None
    ipv6_address: str | None = None
    web: str | None = None
    client: str | None = None
    mac_address: str | None = None
    wireless_mac: str | None = None
    p2p_id: str | None = None
    network_state: str | None = None
    language: str | None = None
    extra: dict[str, Any] = field(default_factory=dict)