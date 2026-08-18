from __future__ import annotations

from typing import Any


class ProtocolManageManager:
    """
    Channel > Protocol Manage (Custom IPC RTSP Streaming Protocol Configuration) APIs.
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
        Get parameter range for Protocol Manage configuration.
        """

        response = self._client._request(
            "/API/ChannelConfig/ProtocolManage/Range",
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
        Get active custom protocol definitions.
        """

        response = self._client._request(
            "/API/ChannelConfig/ProtocolManage/Get",
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
        Set custom protocol definitions.
        """

        self._client._request(
            "/API/ChannelConfig/ProtocolManage/Set",
            {
                "version": "1.0",
                "data": kwargs,
            },
        )
