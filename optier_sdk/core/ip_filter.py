from __future__ import annotations

from typing import Any


class IPFilterManager:
    """
    Network > IP Filter Configuration APIs.
    """

    def __init__(
        self,
        client,
    ) -> None:

        self._client = client

    def range(self) -> dict[str, Any]:
        """
        Get parameter range for Network IP Filter configuration.
        """

        response = self._client._request(
            "/API/NetworkConfig/IPFilter/Range",
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
        Get active Network IP Filter configuration.
        """

        response = self._client._request(
            "/API/NetworkConfig/IPFilter/Get",
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
        Set Network IP Filter configuration.
        """

        self._client._request(
            "/API/NetworkConfig/IPFilter/Set",
            {
                "version": "1.0",
                "data": kwargs,
            },
        )
