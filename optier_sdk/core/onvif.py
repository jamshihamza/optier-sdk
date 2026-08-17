from __future__ import annotations

from typing import Any


class OnvifManager:
    """
    Network > Onvif Configuration APIs.
    """

    def __init__(
        self,
        client,
    ) -> None:

        self._client = client

    def range(self) -> dict[str, Any]:
        """
        Get parameter range for Network ONVIF configuration.
        """

        response = self._client._request(
            "/API/NetworkConfig/Onvif/Range",
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
        Get active Network ONVIF configuration.
        """

        response = self._client._request(
            "/API/NetworkConfig/Onvif/Get",
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
        Set Network ONVIF configuration.
        """

        self._client._request(
            "/API/NetworkConfig/Onvif/Set",
            {
                "version": "1.0",
                "data": kwargs,
            },
        )
