from __future__ import annotations

from typing import Any


class FtpIPCUpgradeManager:
    """
    Maintenance > IPC FTP Upgrade API.

    Manages automated online and FTP firmware updates for connected IP cameras,
    including querying camera upgrade compatibility, checking for remote camera
    firmware releases, monitoring batch camera upgrade progress, and triggering upgrades.
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
        Get capability parameters and range limits for IPC FTP / Online Upgrade.

        :return: Dict containing channel_max, online_upgrade toggle, ftp_auto_upgrade,
                 check_for_updates, button definitions, and channel slot schemas.
        """

        response = self._client._request(
            "/API/IPCMaintaint/FtpIpcUpgrade/Range",
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
        Retrieve current IPC FTP upgrade settings and per-channel upgrade telemetry.

        :return: Dict containing online_upgrade, ftp_auto_upgrade, check_for_updates,
                 and per-channel upgrade statuses (sup_ftp_auto_upgrade, ftp_ipc_new_ver).
        """

        response = self._client._request(
            "/API/IPCMaintaint/FtpIpcUpgrade/Get",
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
        online_upgrade: bool | None = None,
        ftp_auto_upgrade: bool | None = None,
        check_for_updates: bool | None = None,
        channel_info: dict[str, Any] | None = None,
        **kwargs,
    ) -> dict[str, Any]:
        """
        Update IPC FTP / Online Upgrade configuration.

        :param online_upgrade: Enable online upgrade protocol.
        :param ftp_auto_upgrade: Enable automated FTP camera firmware upgrade.
        :param check_for_updates: Enable automatic firmware update checking prompt.
        :param channel_info: Per-channel configuration overrides.
        :return: Device response payload.
        """

        current = self.get()
        payload = dict(current)

        if online_upgrade is not None:
            payload["online_upgrade"] = online_upgrade
        if ftp_auto_upgrade is not None:
            payload["ftp_auto_upgrade"] = ftp_auto_upgrade
        if check_for_updates is not None:
            payload["check_for_updates"] = check_for_updates
        if channel_info is not None:
            payload["channel_info"] = channel_info

        payload.update(kwargs)

        response = self._client._request(
            "/API/IPCMaintaint/FtpIpcUpgrade/Set",
            {
                "version": "1.0",
                "data": payload,
            },
        )

        return response.get(
            "data",
            {},
        )

    def check(
        self,
        check_chns: list[str],
        **kwargs,
    ) -> dict[str, Any]:
        """
        Trigger online firmware update check for specific IP camera channels.

        :param check_chns: List of channel names to check (e.g. ["CH1", "CH2"]).
        :return: Device response payload.
        """

        payload: dict[str, Any] = {
            "check_chns": check_chns,
        }
        payload.update(kwargs)

        response = self._client._request(
            "/API/IPCMaintaint/FtpIpcUpgrade/Check",
            {
                "version": "1.0",
                "data": payload,
            },
        )

        return response.get(
            "data",
            {},
        )

    def progress(
        self,
        upgrade_chns: list[str],
        **kwargs,
    ) -> dict[str, Any]:
        """
        Query the active firmware upgrade progress for target IP camera channels.

        :param upgrade_chns: List of channel names currently upgrading (e.g. ["CH1", "CH2"]).
        :return: Dict containing cur_ipc, upgrade_percent, upgrade_state, and upgrade_result.
        """

        payload: dict[str, Any] = {
            "upgrade_chns": upgrade_chns,
        }
        payload.update(kwargs)

        response = self._client._request(
            "/API/IPCMaintaint/FtpIpcUpgrade/Progress",
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
        upgrade_chns: list[str],
        **kwargs,
    ) -> dict[str, Any]:
        """
        Start online/FTP firmware upgrade for specified IP camera channels.

        :param upgrade_chns: List of channel names to upgrade (e.g. ["CH1", "CH2"]).
        :return: Device response payload.
        """

        payload: dict[str, Any] = {
            "upgrade_chns": upgrade_chns,
        }
        payload.update(kwargs)

        response = self._client._request(
            "/API/IPCMaintaint/FtpIpcUpgrade/Upgrade",
            {
                "version": "1.0",
                "data": payload,
            },
        )

        return response.get(
            "data",
            {},
        )
