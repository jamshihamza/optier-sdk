from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path


@dataclass
class VMSConfig:
    """
    Global configuration settings for the OPTIER VMS application.
    """

    storage_root: Path = field(default_factory=lambda: Path("./vms_storage"))
    evidence_path: Path = field(default_factory=lambda: Path("./vms_storage/evidence"))
    snapshot_path: Path = field(default_factory=lambda: Path("./vms_storage/snapshots"))
    heartbeat_interval_seconds: int = 15
    reconnect_backoff_max_seconds: int = 30
    health_check_interval_seconds: int = 10
    max_devices: int = 64
    max_channels_per_device: int = 256
