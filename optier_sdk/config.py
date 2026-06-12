"""
optier_sdk.config
=================

Central configuration model used throughout the OPTIER SDK.

Design Goals
------------
- Single source of truth
- Strong typing
- Easy future expansion
- No hard-coded values inside SDK modules
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class CameraConfig:
    """
    Configuration used by the Camera client.

    Every Camera instance owns one CameraConfig object.

    Future versions may extend this model without breaking
    backward compatibility.
    """

    # ------------------------------------------------------------------
    # Connection
    # ------------------------------------------------------------------

    host: str

    username: str

    password: str

    port: int = 80

    use_https: bool = False

    # ------------------------------------------------------------------
    # Communication
    # ------------------------------------------------------------------

    timeout: float = 10.0

    verify_ssl: bool = False

    # ------------------------------------------------------------------
    # Session
    # ------------------------------------------------------------------

    heartbeat_interval: int = 25

    auto_reconnect: bool = True

    max_retry: int = 3