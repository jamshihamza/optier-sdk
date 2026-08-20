from __future__ import annotations

from typing import Any


class IPCParamManagementManager:
    """
    Maintenance > IPC Param Management API.

    Manages connected IP camera parameter discovery, configuration backup (export)
    and batch parameter restoration (import) across all IPC channels.
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
        Get capability parameters and schema limits for IPC Parameter Management.

        :return: Dict containing channel slot schemas, status definitions, and parameter limits.
        """

        response = self._client._request(
            "/API/IPCMaintaint/IPCParamManagement/Range",
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
        Retrieve connected IPC status, IP addresses, and firmware builds across all channels.

        :return: Dict containing channel_info mapping with status (Online/Offline),
                 ip_address, software_version, and configuration availability.
        """

        response = self._client._request(
            "/API/IPCMaintaint/IPCParamManagement/Get",
            {
                "version": "1.0",
                "data": {},
            },
        )

        return response.get(
            "data",
            {},
        )

    def export_params(
        self,
        channels: dict[str, bool] | list[str],
        base_secondary_authentication: dict[str, Any] | None = None,
        **kwargs,
    ) -> dict[str, Any]:
        """
        Export configuration backup files (base64 encoded params) from target IP cameras.

        :param channels: List of channel names (e.g. ["CH1", "CH2"]) or dict mapping channel -> bool switch.
        :param base_secondary_authentication: Optional secondary authentication cipher payload.
        :return: Dict containing per-channel exported base64 params and operation states.
        """

        if isinstance(channels, list):
            channel_info = {ch: {"ImportExportSwitch": True} for ch in channels}
        else:
            channel_info = {ch: {"ImportExportSwitch": bool(enabled)} for ch, enabled in channels.items()}

        payload: dict[str, Any] = {
            "channel_info": channel_info,
        }

        if base_secondary_authentication is not None:
            payload["base_secondary_authentication"] = base_secondary_authentication

        payload.update(kwargs)

        response = self._client._request(
            "/API/IPCMaintaint/IPCParamManagement/Export",
            {
                "version": "1.0",
                "data": payload,
            },
        )

        return response.get(
            "data",
            {},
        )

    def import_params(
        self,
        channel_params: dict[str, str],
        base_secondary_authentication: dict[str, Any] | None = None,
        **kwargs,
    ) -> dict[str, Any]:
        """
        Import configuration backup files (base64 encoded params) into target IP cameras.

        :param channel_params: Dict mapping channel name (e.g. "CH1") to base64 param string.
        :param base_secondary_authentication: Optional secondary authentication cipher payload.
        :return: Dict containing per-channel import operation result states.
        """

        channel_info = {
            ch: {
                "ImportExportSwitch": True,
                "param": param_data,
            }
            for ch, param_data in channel_params.items()
        }

        payload: dict[str, Any] = {
            "channel_info": channel_info,
        }

        if base_secondary_authentication is not None:
            payload["base_secondary_authentication"] = base_secondary_authentication

        payload.update(kwargs)

        response = self._client._request(
            "/API/IPCMaintaint/IPCParamManagement/Import",
            {
                "version": "1.0",
                "data": payload,
            },
        )

        return response.get(
            "data",
            {},
        )
