from __future__ import annotations

from typing import Any


class HTTPSManager:
    """
    Network > HTTPS (TLS/HTTPS Encryption & SSL Certificate Management) APIs.
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
        Get parameter range for HTTPS and SSL certificate configuration.
        """

        response = self._client._request(
            "/API/NetworkConfig/https/Range",
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
        Get active HTTPS and SSL certificate configuration.
        """

        response = self._client._request(
            "/API/NetworkConfig/https/Get",
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
        Set HTTPS parameters, install/uninstall/switch SSL certificates.
        """

        self._client._request(
            "/API/NetworkConfig/https/Set",
            {
                "version": "1.0",
                "data": kwargs,
            },
        )
