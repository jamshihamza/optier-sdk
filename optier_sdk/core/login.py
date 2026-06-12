from __future__ import annotations

from .login_device_info import LoginDeviceInfo


class LoginManager:
    """
    Login-related APIs.
    """

    def __init__(self, client) -> None:

        self._client = client

    def device_info(self) -> LoginDeviceInfo:

        response = self._client._request(
            "/API/Login/DeviceInfo/Get"
        )

        return LoginDeviceInfo.from_dict(
            response.get("data", {})
        )

    def channel_info(self) -> dict:

        response = self._client._request(
            "/API/Login/ChannelInfo/Get"
        )

        return response.get("data", {})