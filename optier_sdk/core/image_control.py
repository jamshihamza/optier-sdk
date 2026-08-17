from __future__ import annotations

from typing import Any


class ImageControlManager:
    """
    Channel > Image Control Configuration APIs.
    """

    def __init__(
        self,
        client,
    ) -> None:

        self._client = client

    def range(self) -> dict[str, Any]:
        """
        Get parameter range for Image Control configuration across channels.
        """

        response = self._client._request(
            "/API/ChannelConfig/ImageControl/Range",
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
        Get active Image Control configuration across channels.
        """

        response = self._client._request(
            "/API/ChannelConfig/ImageControl/Get",
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
        Set Image Control configuration.
        """

        self._client._request(
            "/API/ChannelConfig/ImageControl/Set",
            {
                "version": "1.0",
                "data": kwargs,
            },
        )

    def default(
        self,
        channels: list[str] | None = None,
        **kwargs,
    ) -> dict[str, Any]:
        """
        Restore default Image Control configuration for specified channels.

        :param channels: List of channel identifiers, e.g. ["CH1"].
        """

        data: dict[str, Any] = dict(kwargs)
        if channels is not None:
            data["channel"] = channels

        response = self._client._request(
            "/API/ChannelConfig/ImageControl/Default",
            {
                "version": "1.0",
                "data": data,
            },
        )

        return response.get(
            "data",
            {},
        )
