from __future__ import annotations

from typing import Any


class VideoCoverManager:
    """
    Channel > Video Cover (Privacy Masking) Configuration APIs.
    """

    def __init__(
        self,
        client,
    ) -> None:

        self._client = client

    def range(self) -> dict[str, Any]:
        """
        Get parameter range for Video Cover configuration across channels.
        """

        response = self._client._request(
            "/API/ChannelConfig/VideoCover/Range",
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
        Get active Video Cover configuration across channels.
        """

        response = self._client._request(
            "/API/ChannelConfig/VideoCover/Get",
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
        Set Video Cover configuration.
        """

        self._client._request(
            "/API/ChannelConfig/VideoCover/Set",
            {
                "version": "1.0",
                "data": kwargs,
            },
        )
