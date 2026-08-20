from __future__ import annotations

from typing import Any


class LinkageScheduleManager:
    """
    Alarm > Linkage Schedule API.

    Manages active alarm deterrent schedules (FloodLight, Siren, EnforcerLight)
    defining time periods during which alarm actions are armable or disarmed.
    """

    def __init__(
        self,
        client,
    ) -> None:

        self._client = client

    def range(
        self,
        page_type: str = "FloodLight",
        channels: list[str] | None = None,
        **kwargs,
    ) -> dict[str, Any]:
        """
        Get linkage schedule range and capabilities.

        :param page_type: 'FloodLight', 'Siren', or 'EnforcerLight'.
        :param channels: Optional channel list filter (e.g. ['CH1', 'CH2']).
        :return: Dict containing linkage schedule limits.
        """

        payload: dict[str, Any] = {
            "page_type": page_type,
        }
        if channels is not None:
            payload["channel"] = channels
        payload.update(kwargs)

        response = self._client._request(
            "/API/AlarmConfig/Schedule/Range",
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
        page_type: str = "FloodLight",
        channels: list[str] | None = None,
        **kwargs,
    ) -> dict[str, Any]:
        """
        Get active linkage schedule settings.

        :param page_type: 'FloodLight', 'Siren', or 'EnforcerLight'.
        :param channels: Optional channel list filter (e.g. ['CH1', 'CH2']).
        :return: Dict containing channel_info mapping with schedule time periods.
        """

        payload: dict[str, Any] = {
            "page_type": page_type,
        }
        if channels is not None:
            payload["channel"] = channels
        payload.update(kwargs)

        response = self._client._request(
            "/API/AlarmConfig/Schedule/Get",
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
        page_type: str = "FloodLight",
        **kwargs,
    ) -> dict[str, Any]:
        """
        Update linkage schedule time periods for specified channels.

        :param channel_info: Dict mapping channel keys to schedule time periods.
        :param page_type: 'FloodLight', 'Siren', or 'EnforcerLight'.
        :return: Device response payload.
        """

        payload: dict[str, Any] = {
            "page_type": page_type,
            "channel_info": channel_info,
        }
        payload.update(kwargs)

        response = self._client._request(
            "/API/AlarmConfig/Schedule/Set",
            {
                "version": "1.0",
                "data": payload,
            },
        )

        return response.get(
            "data",
            {},
        )
