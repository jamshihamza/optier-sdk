from __future__ import annotations

from typing import Any


class ExceptionAlarmManager:
    """
    Alarm > Exception Configuration APIs.
    """

    def __init__(
        self,
        client,
    ) -> None:

        self._client = client

    def range(self) -> dict[str, Any]:
        """
        Get parameter range for Exception Alarm configuration.
        """

        response = self._client._request(
            "/API/AlarmConfig/Exception/Range",
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
        Get active Exception Alarm configuration.
        """

        response = self._client._request(
            "/API/AlarmConfig/Exception/Get",
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
        Set Exception Alarm configuration.
        """

        self._client._request(
            "/API/AlarmConfig/Exception/Set",
            {
                "version": "1.0",
                "data": kwargs,
            },
        )
