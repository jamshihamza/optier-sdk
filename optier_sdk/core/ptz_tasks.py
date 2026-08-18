from __future__ import annotations

from typing import Any


class PTZTasksManager:
    """
    Channel > Scheduled Tasks (PTZ Scheduled Cruise / Tour Tasks) APIs.
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
        Get parameter range for PTZ Scheduled Tasks.
        """

        response = self._client._request(
            "/API/Schedules/PtzTasks/Range",
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
        **kwargs,
    ) -> dict[str, Any]:
        """
        Get active PTZ Scheduled Tasks configuration.
        """

        response = self._client._request(
            "/API/Schedules/PtzTasks/Get",
            {
                "version": "1.0",
                "data": kwargs,
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
        Set PTZ Scheduled Tasks parameters.
        """

        self._client._request(
            "/API/Schedules/PtzTasks/Set",
            {
                "version": "1.0",
                "data": kwargs,
            },
        )
