from __future__ import annotations

from typing import Any


class VideoColorManager:
    """
    Channel > Video Color Configuration APIs.
    """

    def __init__(
        self,
        client,
    ) -> None:

        self._client = client

    def range(self) -> dict[str, Any]:
        """
        Get parameter range for Video Color across channels.
        """

        response = self._client._request(
            "/API/ChannelConfig/Color/Range",
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
        Get active Video Color configuration across channels.
        """

        response = self._client._request(
            "/API/ChannelConfig/Color/Get",
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
        Set Video Color configuration.
        """

        self._client._request(
            "/API/ChannelConfig/Color/Set",
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
        Restore default Video Color configuration for specified channels.
        """

        data: dict[str, Any] = {}
        if channels is not None:
            data["channel"] = channels
        data.update(kwargs)

        response = self._client._request(
            "/API/ChannelConfig/Color/Default",
            {
                "version": "1.0",
                "data": data,
            },
        )

        return response.get(
            "data",
            {},
        )
