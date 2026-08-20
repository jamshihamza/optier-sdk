from __future__ import annotations

from typing import Any


class PIRManager:
    """
    Alarm > PIR Alarm API.

    Manages Passive Infrared (PIR) body temperature motion detection alarms,
    sensitivities, schedules, and linkage outputs.
    """

    def __init__(
        self,
        client,
    ) -> None:

        self._client = client

    def range(
        self,
        channels: list[str] | None = None,
        page_type: str = "ChannelConfig",
        **kwargs,
    ) -> dict[str, Any]:
        """
        Get PIR alarm parameter range and capabilities.

        :param channels: Optional channel filter list (e.g. ['CH1', 'CH2']).
        :param page_type: 'ChannelConfig' or 'AlarmConfig'.
        :return: Dict containing channel_max and capability definitions.
        """

        payload: dict[str, Any] = {
            "page_type": page_type,
        }
        if channels is not None:
            payload["channel"] = channels
        payload.update(kwargs)

        response = self._client._request(
            "/API/AlarmConfig/PIR/Range",
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
        page_type: str = "ChannelConfig",
        **kwargs,
    ) -> dict[str, Any]:
        """
        Get active PIR alarm settings across channels.

        :param channels: Optional channel filter list.
        :param page_type: 'ChannelConfig' or 'AlarmConfig'.
        :return: Dict containing channel_info mapping with PIR settings.
        """

        payload: dict[str, Any] = {
            "page_type": page_type,
        }
        if channels is not None:
            payload["channel"] = channels
        payload.update(kwargs)

        response = self._client._request(
            "/API/AlarmConfig/PIR/Get",
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
        page_type: str = "ChannelConfig",
        **kwargs,
    ) -> dict[str, Any]:
        """
        Update PIR alarm configuration for specified channels.

        :param channel_info: Dict mapping channel keys to PIR settings.
        :param page_type: 'ChannelConfig' or 'AlarmConfig'.
        :return: Device response payload.
        """

        payload: dict[str, Any] = {
            "page_type": page_type,
            "channel_info": channel_info,
        }
        payload.update(kwargs)

        response = self._client._request(
            "/API/AlarmConfig/PIR/Set",
            {
                "version": "1.0",
                "data": payload,
            },
        )

        return response.get(
            "data",
            {},
        )
