from __future__ import annotations

from typing import Any


class CombinationAlarmManager:
    """
    Alarm > Combination Alarm (Joint Multi-Sensor Alarm Linkage) API.

    Configures multi-sensor event triggers (Motion, PIR, IO, Perimeter Intrusion,
    Line Crossing, Face Detection, Face Recognition, LPR, Crowd Density, Queue Detection)
    and routes them to physical and network alarm actions:
    alarm out relays, recording channels, email alerts, fullscreen pops, buzzers,
    FTP/cloud video/snapshot uploads, audio voice prompts, and HTTP webhooks.
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
        Get parameter range and capabilities for joint combination alarm linkage.

        :param channels: Optional channel list filter (e.g. ['CH1', 'CH2']).
        :return: Dict containing channel_max, support_copy, and channel capability definitions.
        """

        payload: dict[str, Any] = {}
        if channels is not None:
            payload["channel"] = channels
        payload.update(kwargs)

        response = self._client._request(
            "/API/AlarmConfig/Combination/Range",
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
        Get active combination alarm linkage configuration across channels.

        :param channels: Optional channel list filter (e.g. ['CH1', 'CH2']).
        :return: Dict containing channel_info with joint trigger rules, linkages, and outputs.
        """

        payload: dict[str, Any] = {}
        if channels is not None:
            payload["channel"] = channels
        payload.update(kwargs)

        response = self._client._request(
            "/API/AlarmConfig/Combination/Get",
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
        Update joint combination alarm linkage configuration for specified channels.

        :param channel_info: Dict mapping channel keys (e.g. 'CH1') to combination settings
                             (enable_alarm, combination_configure, alarm_out, latch_time,
                              record_enable, record_channel, post_recording, send_email,
                              buzzer, full_screen, voice_prompts_index, http_listening).
        :return: Device response payload.
        """

        payload: dict[str, Any] = {
            "channel_info": channel_info,
        }
        payload.update(kwargs)

        response = self._client._request(
            "/API/AlarmConfig/Combination/Set",
            {
                "version": "1.0",
                "data": payload,
            },
        )

        return response.get(
            "data",
            {},
        )
