from __future__ import annotations

import logging
import threading
import uuid
from typing import Any

from optier_sdk import Camera
from optier_sdk.exceptions import (
    AuthenticationError,
    ConnectionError as SDKConnectionError,
    OptierSDKError,
)

from ..domain.device import (
    ConnectionState,
    Device,
    DeviceInfo,
    DeviceType,
)
from ..domain.channel import (
    AICapability,
    CameraChannel,
)

logger = logging.getLogger("optier_vms.device_service")


class DeviceService:
    """
    VMS Device Management & Multi-Device Lifecycle Service.

    Maintains device registries, asynchronous state transitions, channel matrix
    inventories (1..256 channels), hardware telemetry synchronization, and fault-tolerant health checks.
    """

    def __init__(self) -> None:
        self._devices: dict[uuid.UUID, Device] = {}
        self._lock = threading.RLock()

    def add_device(
        self,
        host: str,
        username: str,
        password: str,
        port: int = 80,
        name: str = "NVR Device",
        device_type: DeviceType = DeviceType.NVR,
        auto_connect: bool = False,
    ) -> Device:
        """
        Register a new physical device into the VMS device registry.
        """
        with self._lock:
            device = Device(
                name=name,
                host=host,
                port=port,
                username=username,
                password=password,
                device_type=device_type,
                state=ConnectionState.DISCONNECTED,
            )
            device.camera_client = Camera(
                host=host,
                port=port,
                username=username,
                password=password,
            )
            self._devices[device.id] = device

        if auto_connect:
            self.connect_device(device.id)

        return device

    def remove_device(self, device_id: uuid.UUID) -> bool:
        """
        Disconnect and remove a device from the VMS.
        """
        with self._lock:
            device = self._devices.get(device_id)
            if not device:
                return False

            if device.state in (ConnectionState.ONLINE, ConnectionState.DEGRADED):
                try:
                    self.disconnect_device(device_id)
                except Exception as exc:
                    logger.warning("Error disconnecting device %s during removal: %s", device_id, exc)

            del self._devices[device_id]
            return True

    def get_device(self, device_id: uuid.UUID) -> Device | None:
        """
        Retrieve a device by its unique VMS UUID.
        """
        with self._lock:
            return self._devices.get(device_id)

    def list_devices(self) -> list[Device]:
        """
        List all registered devices in the VMS.
        """
        with self._lock:
            return list(self._devices.values())

    def connect_device(self, device_id: uuid.UUID) -> bool:
        """
        Establish connection, authenticate session, and synchronize hardware channel inventory.
        Fault-isolated: Failures update device state without crashing other VMS subsystems.
        """
        device = self.get_device(device_id)
        if not device or not device.camera_client:
            return False

        with self._lock:
            device.state = ConnectionState.CONNECTING
            device.error_message = None

        cam: Camera = device.camera_client

        try:
            with self._lock:
                device.state = ConnectionState.AUTHENTICATING

            cam.connect()

            with self._lock:
                device.state = ConnectionState.SYNCHRONIZING

            self._sync_device_info(device, cam)
            self._sync_channel_inventory(device, cam)

            with self._lock:
                device.state = ConnectionState.ONLINE
                device.error_message = None

            logger.info("Device %s (%s) successfully connected and synchronized (%d channels).", device.name, device.host, len(device.channels))
            return True

        except AuthenticationError as exc:
            with self._lock:
                device.state = ConnectionState.AUTH_FAILED
                device.error_message = f"Authentication failed: {exc}"
            logger.error("Authentication failed for device %s (%s): %s", device.name, device.host, exc)
            return False

        except SDKConnectionError as exc:
            with self._lock:
                device.state = ConnectionState.DISCONNECTED
                device.error_message = f"Network connection failed: {exc}"
            logger.error("Connection failed for device %s (%s): %s", device.name, device.host, exc)
            return False

        except Exception as exc:
            with self._lock:
                device.state = ConnectionState.ERROR
                device.error_message = str(exc)
            logger.error("Unexpected error synchronizing device %s (%s): %s", device.name, device.host, exc)
            return False

    def disconnect_device(self, device_id: uuid.UUID) -> bool:
        """
        Gracefully terminate device session and mark state as DISCONNECTED.
        """
        device = self.get_device(device_id)
        if not device or not device.camera_client:
            return False

        cam: Camera = device.camera_client
        try:
            cam.disconnect()
        except Exception as exc:
            logger.debug("Disconnect error on device %s: %s", device_id, exc)

        with self._lock:
            device.state = ConnectionState.DISCONNECTED
            for ch in device.channels.values():
                ch.online = False
                ch.current_status = "Disconnected"

        return True

    def health_check(self, device_id: uuid.UUID) -> bool:
        """
        Perform a non-destructive heartbeat health check on a device.
        """
        device = self.get_device(device_id)
        if not device or not device.camera_client:
            return False

        if device.state != ConnectionState.ONLINE:
            return False

        cam: Camera = device.camera_client
        try:
            cam._request("/API/Login/Heartbeat", {"version": "1.0", "data": {}})
            return True
        except Exception as exc:
            with self._lock:
                device.state = ConnectionState.DEGRADED
                device.error_message = f"Heartbeat failed: {exc}"
            logger.warning("Device %s degraded on heartbeat failure: %s", device.name, exc)
            return False

    def _sync_device_info(self, device: Device, cam: Camera) -> None:
        """
        Fetch device model, serial number, and firmware metadata.
        """
        try:
            sys_info = cam.system_info.get()
            base_info = sys_info.get("base_info", sys_info)
            device.info = DeviceInfo(
                model=base_info.get("model", "OPTIER NVR"),
                serial_number=base_info.get("sn", base_info.get("serial_number", "Unknown")),
                firmware_version=base_info.get("soft_ver", base_info.get("software_version", "Unknown")),
                hardware_version=base_info.get("hard_ver", base_info.get("hardware_version", "Unknown")),
                mac_address=base_info.get("mac", "Unknown"),
                channel_capacity=int(base_info.get("channel_max", 256)),
                raw_details=base_info,
            )
        except Exception as exc:
            logger.warning("Could not sync system_info for %s: %s", device.name, exc)

    def _sync_channel_inventory(self, device: Device, cam: Camera) -> None:
        """
        Discover and populate logical camera channels from hardware channel configurations.
        """
        device.channels.clear()

        # Query channel capabilities and names
        total_channels = device.info.channel_capacity
        channel_names: dict[str, str] = {}
        try:
            chn_resp = cam.system_channel_info.get()
            raw_channels = chn_resp.get("channel_info", {})
            for chk, chdata in raw_channels.items():
                if isinstance(chdata, dict):
                    channel_names[chk] = chdata.get("name", chk)
        except Exception:
            pass

        # Populate channels
        for idx in range(1, total_channels + 1):
            chk = f"CH{idx}"
            ch_name = channel_names.get(chk, f"Camera {idx:02d}")

            channel = CameraChannel(
                device_id=device.id,
                channel_index=idx,
                name=ch_name,
                online=True,
                ptz_supported=True,
                current_status="Online",
            )

            # Assign basic AI capabilities supported across the platform
            channel.ai_capabilities.add(AICapability.MOTION) if hasattr(AICapability, "MOTION") else None
            channel.ai_capabilities.add(AICapability.FACE_DETECTION)
            channel.ai_capabilities.add(AICapability.LICENSE_PLATE_DETECTION)
            channel.ai_capabilities.add(AICapability.LINE_CROSSING)
            channel.ai_capabilities.add(AICapability.PERIMETER_INTRUSION)

            device.add_channel(channel)

    def get_channel(self, device_id: uuid.UUID, channel_index: int) -> CameraChannel | None:
        """
        Retrieve a specific camera channel by device ID and channel index.
        """
        device = self.get_device(device_id)
        if not device:
            return None
        return device.get_channel(channel_index)

    def list_all_channels(self) -> list[CameraChannel]:
        """
        Retrieve a flattened list of all channels across all registered devices.
        """
        all_channels: list[CameraChannel] = []
        with self._lock:
            for device in self._devices.values():
                all_channels.extend(device.channels.values())
        return all_channels
