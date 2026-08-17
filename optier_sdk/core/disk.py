from __future__ import annotations

from typing import Any


class DiskManager:
    """
    Storage > Disk Configuration APIs.
    """

    def __init__(
        self,
        client,
    ) -> None:

        self._client = client

    def range(self) -> dict[str, Any]:
        """
        Get parameter range for Disk configuration.
        """

        response = self._client._request(
            "/API/StorageConfig/Disk/Range",
            {
                "version": "1.0",
                "data": {},
            },
        )

        return response.get(
            "data",
            {},
        )

    def get(self) -> dict[str, Any]:
        """
        Get active Disk configuration and storage status.
        """

        response = self._client._request(
            "/API/StorageConfig/Disk/Get",
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
        Set Disk configuration.
        """

        self._client._request(
            "/API/StorageConfig/Disk/Set",
            {
                "version": "1.0",
                "data": kwargs,
            },
        )

    def control(
        self,
        **kwargs,
    ) -> None:
        """
        Control hard drive or network disk parameters.
        """

        self._client._request(
            "/API/StorageConfig/Disk/Control",
            {
                "version": "1.0",
                "data": kwargs,
            },
        )

    def format(
        self,
        **kwargs,
    ) -> None:
        """
        Format specified hard disk(s).
        """

        self._client._request(
            "/API/StorageConfig/Disk/Format",
            {
                "version": "1.0",
                "data": kwargs,
            },
        )

    def progress(self) -> dict[str, Any]:
        """
        Query hard disk format progress.
        """

        try:
            response = self._client._request(
                "/API/StorageConfig/Disk/Format/Progress",
                {
                    "version": "1.0",
                    "data": {},
                },
            )
        except Exception:
            response = self._client._request(
                "/API/StorageConfig/Disk/Progress",
                {
                    "version": "1.0",
                    "data": {},
                },
            )

        return response.get(
            "data",
            {},
        )
