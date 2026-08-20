from __future__ import annotations

from typing import Any


class IPCUpgradeManager:
    """
    Maintenance > IPC Upgrade API.

    Manages connected IP camera firmware inspection, upgrade capability discovery,
    upgrade token acquisition, and batch firmware upgrading for IPCs across all channels.
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
        Get capability parameters and range limits for IPC Firmware Upgrade.

        :return: Dict containing channel_max, password constraints, and per-channel upgrade schemas.
        """

        response = self._client._request(
            "/API/IPCMaintaint/IPCUpgrade/Range",
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
        Retrieve connected IPC status, IP addresses, software versions, and upgrade file types.

        :return: Dict containing channel_info mapping with IPC online states, IP addresses,
                 software versions, and file type requirements.
        """

        response = self._client._request(
            "/API/IPCMaintaint/IPCUpgrade/Get",
            {
                "version": "1.0",
                "data": {},
            },
        )

        return response.get(
            "data",
            {},
        )

    def token(
        self,
        file_name: str,
        file_size: int,
        ipc_channels: list[int],
        upgrade_head: list[int] | None = None,
        base_secondary_authentication: dict[str, Any] | None = None,
        **kwargs,
    ) -> dict[str, Any]:
        """
        Request IPC upgrade authorization token before uploading firmware package.

        :param file_name: Firmware package filename.
        :param file_size: Firmware package byte size.
        :param ipc_channels: List of channel integers to be upgraded.
        :param upgrade_head: Byte array header (e.g. 1KB-3KB pre-upgrade header).
        :param base_secondary_authentication: Secondary authentication payload.
        :return: Device response payload containing upgrade_token.
        """

        payload: dict[str, Any] = {
            "file_name": file_name,
            "file_size": file_size,
            "ipc_channels": ipc_channels,
        }

        if upgrade_head is not None:
            payload["upgrade_head"] = upgrade_head
        if base_secondary_authentication is not None:
            payload["base_secondary_authentication"] = base_secondary_authentication

        payload.update(kwargs)

        response = self._client._request(
            "/API/IPCMaintaint/IPCUpgrade/Token",
            {
                "version": "1.0",
                "data": payload,
            },
        )

        return response.get(
            "data",
            {},
        )

    def upgrade(
        self,
        **kwargs,
    ) -> dict[str, Any]:
        """
        Start IPC firmware upgrade process.

        :return: Device response payload.
        """

        payload: dict[str, Any] = {}
        payload.update(kwargs)

        response = self._client._request(
            "/API/IPCMaintaint/IPCUpgrade/Upgrade",
            {
                "version": "1.0",
                "data": payload,
            },
        )

        return response.get(
            "data",
            {},
        )
