from __future__ import annotations

from typing import Any


class OSDManager:
    """
    Channel > OSD (On-Screen Display) Configuration APIs.
    """

    def __init__(
        self,
        client,
    ) -> None:

        self._client = client

    def range(self) -> dict[str, Any]:
        """
        Get parameter range for OSD configuration across channels.
        """

        response = self._client._request(
            "/API/ChannelConfig/OSD/Range",
            {
                "version": "1.0",
                "data": {},
            },
        )

        return response.get(
            "data",
            {},
        )

    def get(self) -> dict[str, Any]:
        """
        Get active OSD configuration across channels.
        """

        response = self._client._request(
            "/API/ChannelConfig/OSD/Get",
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
        Set OSD configuration.
        """

        self._client._request(
            "/API/ChannelConfig/OSD/Set",
            {
                "version": "1.0",
                "data": kwargs,
            },
        )
