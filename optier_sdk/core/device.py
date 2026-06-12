from __future__ import annotations

from ..constants import LOGIN_DEVICE_INFO_URI
from ..models.device_info import DeviceInfo


class DeviceManager:

    def __init__(self, client) -> None:

        self._client = client

    def info(self) -> DeviceInfo:

        response = self._client._request(
            LOGIN_DEVICE_INFO_URI
        )

        data = response.get("data", {})

        return DeviceInfo(
            device_name=data.get("device_name"),
            model=data.get("model"),
            serial_number=data.get("sn"),
            firmware_version=data.get("firmware_version"),
            hardware_version=data.get("hardware_version"),
            software_version=data.get("software_version"),
            manufacturer=data.get("manufacturer"),
            vendor=data.get("vendor"),
            mac_address=data.get("mac"),
            web_version=data.get("web_version"),
            oem_model=data.get("oem_model"),
            channel_count=data.get("channel_num"),
        )