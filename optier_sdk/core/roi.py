from __future__ import annotations

from typing import Any


class ROIManager:
    """
    Channel > ROI (Region of Interest Video Stream Compression) APIs.
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
        Get parameter range for Channel ROI configuration.
        """

        response = self._client._request(
            "/API/ChannelConfig/ROI/Range",
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
        **kwargs,
    ) -> dict[str, Any]:
        """
        Get active ROI configuration across channels.
        """

        response = self._client._request(
            "/API/ChannelConfig/ROI/Get",
            {
                "version": "1.0",
                "data": kwargs,
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
        Set ROI parameters for channels.
        """

        self._client._request(
            "/API/ChannelConfig/ROI/Set",
            {
                "version": "1.0",
                "data": kwargs,
            },
        )
