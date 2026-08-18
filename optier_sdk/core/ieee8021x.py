from __future__ import annotations

from typing import Any


class IEEE8021xManager:
    """
    Network > IEEE8021x configuration APIs.
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
        Get parameter range for IEEE8021x configuration.
        """

        response = self._client._request(
            "/API/NetworkConfig/IEEE8021x/Range",
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
        Get active IEEE8021x configuration.
        """

        response = self._client._request(
            "/API/NetworkConfig/IEEE8021x/Get",
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
        Set IEEE8021x configuration.
        """

        self._client._request(
            "/API/NetworkConfig/IEEE8021x/Set",
            {
                "version": "1.0",
                "data": kwargs,
            },
        )
