from __future__ import annotations

from typing import Any


class DisarmingManager:
    """
    Alarm > Disarming (One-Key Disarm / Linkage Suppression) APIs.
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
        Get parameter range for Disarming configuration.
        """

        response = self._client._request(
            "/API/AlarmConfig/Disarming/Range",
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
        Get active Disarming configuration and channel schedules.
        """

        response = self._client._request(
            "/API/AlarmConfig/Disarming/Get",
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
        Set Disarming configuration.
        """

        self._client._request(
            "/API/AlarmConfig/Disarming/Set",
            {
                "version": "1.0",
                "data": kwargs,
            },
        )
