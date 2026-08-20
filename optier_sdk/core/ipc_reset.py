from __future__ import annotations

from typing import Any


class IPCResetManager:
    """
    Maintenance > IPC Reset (Load Default) API.

    Manages connected IP camera online statuses and remote camera factory default
    restoration execution across all active IPC channel slots.
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
        Get capability parameters and range limits for IPC Reset (Load Default).

        :return: Dict containing channel slot schemas, status definitions, and reset capability schemas.
        """

        response = self._client._request(
            "/API/IPCMaintaint/IPCReset/Range",
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
        Retrieve connected IPC online status, IP addresses, and firmware builds across all channels.

        :return: Dict containing channel_info mapping with IPC online states, IP addresses,
                 and firmware builds.
        """

        response = self._client._request(
            "/API/IPCMaintaint/IPCReset/Get",
            {
                "version": "1.0",
                "data": {},
            },
        )

        return response.get(
            "data",
            {},
        )

    def reset_cameras(
        self,
        channels: list[str] | dict[str, bool],
        password: str | None = None,
        base_secondary_authentication: dict[str, Any] | None = None,
        **kwargs,
    ) -> dict[str, Any]:
        """
        Reset target IP cameras to factory default settings.

        :param channels: List of channel names (e.g. ["CH1", "CH2"]) or dict mapping channel -> bool reset switch.
        :param password: Admin password for secondary verification.
        :param base_secondary_authentication: Optional secondary authentication cipher payload.
        :return: Device response payload with per-channel reset operation status.
        """

        if isinstance(channels, list):
            channel_info = {ch: {"reset_switch": True} for ch in channels}
        else:
            channel_info = {ch: {"reset_switch": bool(enabled)} for ch, enabled in channels.items()}

        payload: dict[str, Any] = {
            "channel_info": channel_info,
        }

        if password is not None:
            payload["password"] = password
        if base_secondary_authentication is not None:
            payload["base_secondary_authentication"] = base_secondary_authentication

        payload.update(kwargs)

        response = self._client._request(
            "/API/IPCMaintaint/IPCReset/Set",
            {
                "version": "1.0",
                "data": payload,
            },
        )

        return response.get(
            "data",
            {},
        )
