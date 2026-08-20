from __future__ import annotations

from typing import Any


class DeveloperModeManager:
    """
    Maintenance > DeveloperMode API.

    Controls developer diagnostics, SSH debug access, debug print output locations
    (terminal/disk/shut off), IPC diagnostic log collection across channels, and
    diagnostic log bundle token/download operations.
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
        Get capability parameters and range limits for Developer Mode configuration.

        :return: Dict containing ssh_switch capabilities, export_disk_switch options,
                 export_days limits, timeout parameters, and channel_info structures.
        """

        response = self._client._request(
            "/API/Maintenance/DeveloperMode/Range",
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
        Retrieve current Developer Mode settings and diagnostic logging telemetry.

        :return: Dict containing ssh_switch status, export_disk_switch target,
                 export/delete capabilities, and per-channel log collection settings.
        """

        response = self._client._request(
            "/API/Maintenance/DeveloperMode/Get",
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
        ssh_switch: bool | None = None,
        export_disk_switch: str | None = None,
        export_days: str | None = None,
        **kwargs,
    ) -> dict[str, Any]:
        """
        Update Developer Mode configuration.

        :param ssh_switch: Enable/disable SSH debug shell access.
        :param export_disk_switch: Print output location ("Shut Off", "Output To Terminal", "Output To Disk").
        :param export_days: Number of days to export logs ("all", "1", "2", "3", "4", "5").
        :return: Device response payload.
        """

        current = self.get()
        payload = dict(current)

        if ssh_switch is not None:
            payload["ssh_switch"] = ssh_switch
        if export_disk_switch is not None:
            payload["export_disk_switch"] = export_disk_switch
        if export_days is not None:
            payload["export_days"] = export_days

        payload.update(kwargs)

        response = self._client._request(
            "/API/Maintenance/DeveloperMode/Set",
            {
                "version": "1.0",
                "data": payload,
            },
        )

        return response.get(
            "data",
            {},
        )

    def token(
        self,
        download_type: str = "NVR_Local",
        export_days: str = "all",
        channel: list[str] | None = None,
        **kwargs,
    ) -> dict[str, Any]:
        """
        Request download token for diagnostic log bundle.

        :param download_type: Log source ("NVR_Local" or "NVR_Ipc").
        :param export_days: Number of days ("all", "1", "2", "3", "4", "5").
        :param channel: Channel list when downloading IPC logs (e.g. ["CH1", "CH2"]).
        :return: Device response payload containing x-download-token.
        """

        payload: dict[str, Any] = {
            "download_type": download_type,
            "export_days": export_days,
        }

        if channel is not None:
            payload["channel"] = channel

        payload.update(kwargs)

        response = self._client._request(
            "/API/Maintenance/DeveloperMode/Token",
            {
                "version": "1.0",
                "data": payload,
            },
        )

        return response.get(
            "data",
            {},
        )

    def clear(
        self,
        delete_type: str = "NVR_Local",
        **kwargs,
    ) -> dict[str, Any]:
        """
        Clear diagnostic log files stored in disk.

        :param delete_type: Log target to clear ("NVR_Local" or "NVR_Ipc").
        :return: Device response payload.
        """

        payload: dict[str, Any] = {
            "delete_type": delete_type,
        }
        payload.update(kwargs)

        response = self._client._request(
            "/API/Maintenance/DeveloperMode/Clear",
            {
                "version": "1.0",
                "data": payload,
            },
        )

        return response.get(
            "data",
            {},
        )
