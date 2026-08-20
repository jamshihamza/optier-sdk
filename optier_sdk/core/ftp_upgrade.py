from __future__ import annotations

from typing import Any


class FtpUpgradeManager:
    """
    Maintenance > FtpUpgrade API.

    Controls firmware upgrade server configuration (FTP/HTTP online upgrade),
    checking for remote firmware releases, querying upgrade progress, and
    triggering online firmware upgrades.
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
        Get capability parameters and range limits for FTP/Online Upgrade configuration.

        :return: Dict containing server address limits, port constraints, username/pwd lengths,
                 button visibility configurations, and version string specifications.
        """

        response = self._client._request(
            "/API/Maintenance/FtpUpgrade/Range",
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
        url_key: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        """
        Retrieve current online upgrade configuration.

        :param url_key: Optional encryption key object for IPC docking online upgrade URL retrieval.
        :return: Dict containing ftp_addr, ftp_port, username, user_pwd_empty, ftp_path,
                 check_for_updates, online_upgrade, and Upgrade_button status.
        """

        payload: dict[str, Any] = {}
        if url_key is not None:
            payload["url_key"] = url_key

        response = self._client._request(
            "/API/Maintenance/FtpUpgrade/Get",
            {
                "version": "1.0",
                "data": payload,
            },
        )

        return response.get(
            "data",
            {},
        )

    def set(
        self,
        ftp_addr: str | None = None,
        ftp_port: int | None = None,
        username: str | None = None,
        user_pwd: str | None = None,
        user_pwd_empty: bool | None = None,
        ftp_path: str | None = None,
        check_for_updates: bool | None = None,
        online_upgrade: bool | None = None,
        Upgrade_button: bool | None = None,
        **kwargs,
    ) -> dict[str, Any]:
        """
        Update online upgrade server configuration.

        :param ftp_addr: Upgrade server address (e.g. ftp://192.168.1.100:23/device/upgradePackage).
        :param ftp_port: Server port (default 21).
        :param username: Authentication username.
        :param user_pwd: Authentication password.
        :param user_pwd_empty: Whether password is empty.
        :param ftp_path: Upgrade file path.
        :param check_for_updates: Enable automatic check for updates.
        :param online_upgrade: Enable online upgrade feature.
        :param Upgrade_button: Upgrade button enablement state.
        :return: Device response payload.
        """

        current = self.get()
        payload = dict(current)

        if ftp_addr is not None:
            payload["ftp_addr"] = ftp_addr
        if ftp_port is not None:
            payload["ftp_port"] = ftp_port
        if username is not None:
            payload["username"] = username
        if user_pwd is not None:
            payload["user_pwd"] = user_pwd
        if user_pwd_empty is not None:
            payload["user_pwd_empty"] = user_pwd_empty
        if ftp_path is not None:
            payload["ftp_path"] = ftp_path
        if check_for_updates is not None:
            payload["check_for_updates"] = check_for_updates
        if online_upgrade is not None:
            payload["online_upgrade"] = online_upgrade
        if Upgrade_button is not None:
            payload["Upgrade_button"] = Upgrade_button

        payload.update(kwargs)

        response = self._client._request(
            "/API/Maintenance/FtpUpgrade/Set",
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
    ) -> dict[str, Any]:
        """
        Trigger online check for new firmware updates on configured server.

        :return: Dict containing has_new_firmware, cur_version, new_version, Upgrade_button, and lang_strs.
        """

        response = self._client._request(
            "/API/Maintenance/FtpUpgrade/Check",
            {
                "version": "1.0",
                "data": {},
            },
        )

        return response.get(
            "data",
            {},
        )

    def progress(
        self,
    ) -> dict[str, Any]:
        """
        Query the active online firmware upgrade progress.

        :return: Dict containing upgrade_percent (0..100), upgrade_state, and upgrade_result.
        """

        response = self._client._request(
            "/API/Maintenance/FtpUpgrade/Progress",
            {
                "version": "1.0",
                "data": {},
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
        Start firmware upgrade process from configured online package source.

        :return: Device response payload.
        """

        payload: dict[str, Any] = {}
        payload.update(kwargs)

        response = self._client._request(
            "/API/Maintenance/FtpUpgrade/Upgrade",
            {
                "version": "1.0",
                "data": payload,
            },
        )

        return response.get(
            "data",
            {},
        )
