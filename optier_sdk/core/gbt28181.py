from __future__ import annotations

from typing import Any


class GBT28181Manager:
    """
    Network > GB/T 28181 (Chinese National Standard Video Surveillance Network) APIs.
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
        Get parameter range for GB/T 28181 configuration.
        """

        response = self._client._request(
            "/API/NetworkConfig/T28181/Range",
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
        Get active GB/T 28181 configuration.
        """

        response = self._client._request(
            "/API/NetworkConfig/T28181/Get",
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
        Set GB/T 28181 configuration.
        """

        self._client._request(
            "/API/NetworkConfig/T28181/Set",
            {
                "version": "1.0",
                "data": kwargs,
            },
        )
