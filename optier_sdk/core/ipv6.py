from __future__ import annotations

from typing import Any


class IPv6Manager:
    """
    Network > IPv6 configuration APIs.
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
        Get parameter range for IPv6 configuration.
        """

        response = self._client._request(
            "/API/NetworkConfig/Ipv6/Range",
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
        Get active IPv6 configuration.
        """

        response = self._client._request(
            "/API/NetworkConfig/Ipv6/Get",
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
        Set IPv6 configuration.
        """

        self._client._request(
            "/API/NetworkConfig/Ipv6/Set",
            {
                "version": "1.0",
                "data": kwargs,
            },
        )
