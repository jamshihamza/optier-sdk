from __future__ import annotations

from typing import Any


class FloodlightAudioAlarmManager:
    """
    PreviewChannel > Floodlight & Audio Alarm (Active Deterrence White Light, Horn, Siren, Red/Blue Strobe) APIs.
    """

    def __init__(
        self,
        client,
    ) -> None:

        self._client = client

    def get(
        self,
        channel: str = "CH1",
        command_flag: bool = False,
        **kwargs,
    ) -> dict[str, Any]:
        """
        Get real-time floodlight, siren, and red/blue strobe status for a specific channel.
        """

        payload = {
            "channel": channel,
            "command_flag": command_flag,
        }
        payload.update(kwargs)

        response = self._client._request(
            "/API/PreviewChannel/Floodlight2AudioAlarm/Get",
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
        channel: str,
        **kwargs,
    ) -> None:
        """
        Set or control floodlight, siren, and red/blue strobe settings for a specific channel.
        """

        payload = {"channel": channel}
        payload.update(kwargs)

        self._client._request(
            "/API/PreviewChannel/Floodlight2AudioAlarm/Set",
            {
                "version": "1.0",
                "data": payload,
            },
        )
