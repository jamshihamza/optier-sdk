from __future__ import annotations

from typing import Any


class StorageCloudManager:
    """
    Storage > Cloud Storage API.

    Supports configuring cloud backup integration (Dropbox, Google Drive),
    managing cloud storage overwrite policies, video recording formats,
    per-channel cloud folder mappings, and OAuth access token management.
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
        Get capability parameters and range limits for Cloud Storage configuration.

        :return: Dict containing cloud_type options, cloud_status, overwrite policies,
                 video file formats, channel_max, and channel_info folder constraints.
        """

        response = self._client._request(
            "/API/StorageConfig/Cloud/Range",
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
        Retrieve current Cloud Storage configuration and telemetry.

        :return: Dict containing cloud_storage toggle, cloud_type, cloud_status,
                 capacity statistics (total_size, used_size, progress), overwrite mode,
                 video_type, and per-channel folder mappings.
        """

        response = self._client._request(
            "/API/StorageConfig/Cloud/Get",
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
        cloud_storage: bool | None = None,
        cloud_type: str | None = None,
        cloud_over_write: str | None = None,
        video_type: str | None = None,
        channel_info: dict[str, Any] | None = None,
        **kwargs,
    ) -> dict[str, Any]:
        """
        Update Cloud Storage settings.

        :param cloud_storage: Enable/disable cloud storage backup.
        :param cloud_type: Cloud service provider ("DROPBOX", "Google Drive").
        :param cloud_over_write: Cloud overwrite retention policy ("OFF", "Auto", "1Day", "3Days", "7Days", "14Days", "30Days", "90Days").
        :param video_type: Video recording container format ("RF", "AVI", "MP4").
        :param channel_info: Dictionary mapping channel names to folder configurations (e.g. {"CH1": {"folder_name": "CH1"}}).
        :return: Device response payload.
        """

        current = self.get()
        payload = dict(current)

        if cloud_storage is not None:
            payload["cloud_storage"] = cloud_storage
        if cloud_type is not None:
            payload["cloud_type"] = cloud_type
        if cloud_over_write is not None:
            payload["cloud_over_write"] = cloud_over_write
        if video_type is not None:
            payload["video_type"] = video_type
        if channel_info is not None:
            payload["channel_info"] = channel_info

        payload.update(kwargs)

        response = self._client._request(
            "/API/StorageConfig/Cloud/Set",
            {
                "version": "1.0",
                "data": payload,
            },
        )

        return response.get(
            "data",
            {},
        )

    def control(
        self,
        cloud_type: str = "DROPBOX",
        **kwargs,
    ) -> dict[str, Any]:
        """
        Initiate cloud provider OAuth authorization request.

        :param cloud_type: Cloud service provider ("DROPBOX" or "Google Drive").
        :return: Dict containing the OAuth authorization URL.
        """

        current = self.get()
        payload = dict(current)
        payload["cloud_type"] = cloud_type
        payload.update(kwargs)

        response = self._client._request(
            "/API/StorageConfig/Cloud/Control",
            {
                "version": "1.0",
                "data": payload,
            },
        )

        return response.get(
            "data",
            {},
        )

    def set_access_token(
        self,
        access_token: str,
    ) -> dict[str, Any]:
        """
        Submit OAuth access token after successful cloud provider activation.

        :param access_token: OAuth token string (1..128 characters).
        :return: Device response payload.
        """

        response = self._client._request(
            "/API/action/accesstoken",
            {
                "version": "1.0",
                "data": {
                    "accesstoken": access_token,
                },
            },
        )

        return response.get(
            "data",
            {},
        )
