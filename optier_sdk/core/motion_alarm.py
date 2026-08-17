from __future__ import annotations

from typing import Any


class MotionAlarmManager:
    """
    Alarm > Motion Alarm Configuration APIs.
    """

    def __init__(
        self,
        client,
    ) -> None:

        self._client = client

    def range(
        self,
        page_type: str | None = "AlarmConfig",
    ) -> dict[str, Any]:
        """
        Get parameter range for Motion Alarm configuration across channels.

        :param page_type: Optional page type, e.g. "AlarmConfig", "ChannelConfig", "AllConfig", or None for empty.
        """

        data: dict[str, Any] = {}
        if page_type is not None:
            data["page_type"] = page_type

        response = self._client._request(
            "/API/AlarmConfig/Motion/Range",
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
        page_type: str | None = "AlarmConfig",
    ) -> dict[str, Any]:
        """
        Get active Motion Alarm configuration across channels.

        :param page_type: Optional page type, e.g. "AlarmConfig", "ChannelConfig", "AllConfig", or None for empty.
        """

        data: dict[str, Any] = {}
        if page_type is not None:
            data["page_type"] = page_type

        response = self._client._request(
            "/API/AlarmConfig/Motion/Get",
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
        Set Motion Alarm configuration.
        """

        self._client._request(
            "/API/AlarmConfig/Motion/Set",
            {
                "version": "1.0",
                "data": kwargs,
            },
        )
