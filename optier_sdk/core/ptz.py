from __future__ import annotations

from typing import Any


class PTZManager:
    """
    Channel > PTZ (Channel Serial & Digital PTZ Configuration) APIs.
    """

    def __init__(
        self,
        client,
    ) -> None:

        self._client = client

    def range(
        self,
    ) -> dict[str, Any]:
        """
        Get parameter range for PTZ channel configuration.
        """

        response = self._client._request(
            "/API/ChannelConfig/PTZ/Range",
            {
                "version": "1.0",
                "data": {},
            },
        )

        return response.get(
            "data",
            {},
        )

    def get(
        self,
    ) -> dict[str, Any]:
        """
        Get active PTZ configuration for all channels.
        """

        response = self._client._request(
            "/API/ChannelConfig/PTZ/Get",
            {
                "version": "1.0",
                "data": {},
            },
        )

        return response.get(
            "data",
            {},
        )

    def set(
        self,
        **kwargs,
    ) -> None:
        """
        Set PTZ configuration parameters.
        """

        self._client._request(
            "/API/ChannelConfig/PTZ/Set",
            {
                "version": "1.0",
                "data": kwargs,
            },
        )
