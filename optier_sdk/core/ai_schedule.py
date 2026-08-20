from __future__ import annotations

from typing import Any


class AIScheduleManager:
    """
    AI > Setup > AI Func Schedule API.

    Manages time-based scheduling of AI functions (Human/Vehicle Detection,
    Face Recognition, LPR, Perimeter Intrusion, Line Crossing, Crowd Density)
    across all device channels.
    """

    def __init__(
        self,
        client,
    ) -> None:

        self._client = client

    def range(
        self,
        channels: list[str] | None = None,
        **kwargs,
    ) -> dict[str, Any]:
        """
        Get parameter range and channel capabilities for AI function scheduling.

        :param channels: Optional channel list filter (e.g. ['CH1', 'CH2']).
        :return: Dict containing channel_max, support_copy, and channel capability definitions.
        """

        payload: dict[str, Any] = {}
        if channels is not None:
            payload["channel"] = channels
        payload.update(kwargs)

        response = self._client._request(
            "/API/AI/Setup/AISchedule/Range",
            {
                "version": "1.0",
                "data": payload,
            },
        )

        return response.get(
            "data",
            {},
        )

    def get(
        self,
        channels: list[str] | None = None,
        **kwargs,
    ) -> dict[str, Any]:
        """
        Get active AI function schedule configuration across channels.

        :param channels: Optional channel list filter.
        :return: Dict containing channel_info with scheduled AI function time blocks.
        """

        payload: dict[str, Any] = {}
        if channels is not None:
            payload["channel"] = channels
        payload.update(kwargs)

        response = self._client._request(
            "/API/AI/Setup/AISchedule/Get",
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
        channel_info: dict[str, Any],
        **kwargs,
    ) -> dict[str, Any]:
        """
        Update AI function schedules for specified channels.

        :param channel_info: Dict mapping channel keys to AI schedule configurations.
        :return: Device response payload.
        """

        payload: dict[str, Any] = {
            "channel_info": channel_info,
        }
        payload.update(kwargs)

        response = self._client._request(
            "/API/AI/Setup/AISchedule/Set",
            {
                "version": "1.0",
                "data": payload,
            },
        )

        return response.get(
            "data",
            {},
        )
