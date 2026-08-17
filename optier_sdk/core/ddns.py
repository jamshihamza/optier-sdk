from __future__ import annotations

from typing import Any


class DDNSManager:
    """
    Network > DDNS (Dynamic DNS Providers & Host Resolution) APIs.
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
        Get parameter range for DDNS configuration.
        """

        response = self._client._request(
            "/API/NetworkConfig/DDNS/Range",
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
        Get active DDNS configuration.
        """

        response = self._client._request(
            "/API/NetworkConfig/DDNS/Get",
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
        Set DDNS configuration.
        """

        self._client._request(
            "/API/NetworkConfig/DDNS/Set",
            {
                "version": "1.0",
                "data": kwargs,
            },
        )

    def test(
        self,
        **kwargs,
    ) -> dict[str, Any]:
        """
        Test DDNS server connectivity and credential validation.
        """

        response = self._client._request(
            "/API/NetworkConfig/DDNS/Test",
            {
                "version": "1.0",
                "data": kwargs,
            },
        )

        return response.get(
            "data",
            {},
        )
