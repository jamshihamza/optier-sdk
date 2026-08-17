from __future__ import annotations

from typing import Any


class IOAlarmManager:
    """
    Alarm > IO Alarm (Alarm Input / Linkage) APIs.
    """

    def __init__(
        self,
        client,
    ) -> None:

        self._client = client

    def range(
        self,
        alarm_in: list[str] | None = None,
    ) -> dict[str, Any]:
        """
        Get parameter range for IO Alarm configuration.

        :param alarm_in: Optional list of alarm input channels, e.g. ["Local<-1", "IP_CH1<-1"].
        """

        data: dict[str, Any] = {}
        if alarm_in is not None:
            data["alarm_in"] = alarm_in

        response = self._client._request(
            "/API/AlarmConfig/IO/Range",
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
        alarm_in: list[str] | None = None,
    ) -> dict[str, Any]:
        """
        Get active IO Alarm configuration.

        :param alarm_in: Optional list of alarm input channels, e.g. ["Local<-1", "IP_CH1<-1"].
        """

        data: dict[str, Any] = {}
        if alarm_in is not None:
            data["alarm_in"] = alarm_in

        response = self._client._request(
            "/API/AlarmConfig/IO/Get",
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
        Set IO Alarm configuration.
        """

        self._client._request(
            "/API/AlarmConfig/IO/Set",
            {
                "version": "1.0",
                "data": kwargs,
            },
        )
