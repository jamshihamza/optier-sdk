from __future__ import annotations

from typing import Any


class TuyaManager:
    """
    Network > Tuya cloud IoT integration APIs.
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
        Get parameter range for Tuya configuration.
        """

        response = self._client._request(
            "/API/NetworkConfig/Tuya/Range",
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
        Get active Tuya configuration.
        """

        response = self._client._request(
            "/API/NetworkConfig/Tuya/Get",
            {
                "version": "1.0",
            },
        )

        return response.get(
            "data",
            {},
        )

    def set(
        self,
        enable: bool,
    ) -> None:
        """
        Set Tuya configuration.

        :param enable: Whether Tuya IoT cloud service is enabled.
        """

        self._client._request(
            "/API/NetworkConfig/Tuya/Set",
            {
                "version": "1.0",
                "data": {
                    "enable": enable,
                },
            },
        )
