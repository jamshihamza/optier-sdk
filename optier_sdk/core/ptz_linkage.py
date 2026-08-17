from __future__ import annotations

from typing import Any


class PTZLinkageManager:
    """
    Alarm > PTZ Linkage (Alarm-to-PTZ Preset Linkage) APIs.
    """

    def __init__(
        self,
        client,
    ) -> None:

        self._client = client

    def range(
        self,
        channels: list[str] | None = None,
    ) -> dict[str, Any]:
        """
        Get parameter range for PTZ Linkage configuration.

        :param channels: Optional list of channel identifiers, e.g. ["CH1", "CH3"].
        """

        data: dict[str, Any] = {}
        if channels is not None:
            data["channel"] = channels

        response = self._client._request(
            "/API/AlarmConfig/PTZLinkage/Range",
            {
                "version": "1.0",
                "data": data,
            },
        )

        return response.get(
            "data",
            {},
        )

    def get(
        self,
        channels: list[str] | None = None,
    ) -> dict[str, Any]:
        """
        Get active PTZ Linkage configuration.

        :param channels: Optional list of channel identifiers, e.g. ["CH1", "CH3"].
        """

        data: dict[str, Any] = {}
        if channels is not None:
            data["channel"] = channels

        response = self._client._request(
            "/API/AlarmConfig/PTZLinkage/Get",
            {
                "version": "1.0",
                "data": data,
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
        Set PTZ Linkage configuration.
        """

        self._client._request(
            "/API/AlarmConfig/PTZLinkage/Set",
            {
                "version": "1.0",
                "data": kwargs,
            },
        )
