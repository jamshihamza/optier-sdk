from __future__ import annotations

from typing import Any


class RemoteDevManager:
    """
    Channel > Broadcast IPC / Remote Device Discovery & Provisioning APIs.
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
        Get parameter range for RemoteDev broadcast search and configuration.
        """

        response = self._client._request(
            "/API/ChannelConfig/RemoteDev/Range",
            {
                "version": "1.0",
                "data": {},
            },
        )

        return response.get(
            "data",
            {},
        )

    def search(
        self,
        **kwargs,
    ) -> dict[str, Any]:
        """
        Broadcast search for remote IPCs on the local network.
        """

        response = self._client._request(
            "/API/ChannelConfig/RemoteDev/Search",
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
        Modify remote IPC network parameters (IP address, port, DHCP, credentials).
        """

        self._client._request(
            "/API/ChannelConfig/RemoteDev/Set",
            {
                "version": "1.0",
                "data": kwargs,
            },
        )
