from __future__ import annotations

from ..models.channel_info import ChannelInfo
from ..models.login_device_info import LoginDeviceInfo


class LoginManager:
    """
    Login-related APIs.
    """

    def __init__(self, client) -> None:
        self._client = client

    def device_info(self) -> LoginDeviceInfo:
        """
        Retrieve device information after login.
        """

        response = self._client._request(
            "/API/Login/DeviceInfo/Get"
        )

        return LoginDeviceInfo(
            response.get("data", {})
        )

    def channel_info(self) -> list[ChannelInfo]:
        """
        Retrieve channel information.
        """

        response = self._client._request(
            "/API/Login/ChannelInfo/Get"
        )

        data = response.get(
            "data",
            {},
        )

        channel_param = data.get(
            "channel_param",
            [],
        )

        #
        # Some firmware may return:
        #
        # {
        #     "type": "array",
        #     "items": [...]
        # }
        #

        if isinstance(channel_param, dict):
            channel_param = channel_param.get(
                "items",
                [],
            )

        return [
            ChannelInfo.from_dict(item)
            for item in channel_param
        ]