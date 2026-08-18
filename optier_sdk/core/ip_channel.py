from __future__ import annotations

from typing import Any


class IPChannelManager:
    """
    Channel > IPChannel (Digital / IP Camera Channel Management) APIs.
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
        Get parameter range for IPChannel configuration.
        """

        response = self._client._request(
            "/API/ChannelConfig/IPChannel/Range",
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
        Get active IPChannel configuration and connected IPC channel metadata.
        """

        response = self._client._request(
            "/API/ChannelConfig/IPChannel/Get",
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
        Set IPChannel parameters (Add, Edit, Remove IPC channels).
        """

        self._client._request(
            "/API/ChannelConfig/IPChannel/Set",
            {
                "version": "1.0",
                "data": kwargs,
            },
        )

    def set_auto_add_ipc(
        self,
        **kwargs,
    ) -> None:
        """
        Set Auto Add IPC parameters.
        """

        self._client._request(
            "/API/ChannelConfig/AutoAddIPC/Set",
            {
                "version": "1.0",
                "data": kwargs,
            },
        )
