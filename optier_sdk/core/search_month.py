from __future__ import annotations

from typing import Any


class SearchMonthManager:
    """
    Record / Playback > SearchMonth (Monthly calendar search for recorded footage and snapshots) API.
    """

    def __init__(
        self,
        client,
    ) -> None:

        self._client = client

    def get(
        self,
        start_date: str,
        channel: list[str] | str | None = None,
        stream_type: str = "Mainstream",
        search_type: str = "Record",
        **kwargs,
    ) -> dict[str, Any]:
        """
        Get monthly playback availability calendar array for a specified date and channels.

        :param start_date: Search start date in MM/DD/YYYY format (e.g. "08/01/2026").
        :param channel: Optional channel name or list of channel names. Empty list/None searches all channels.
        :param stream_type: "Mainstream" or "Substream".
        :param search_type: "Record", "Picture", "FD", "PVD", "PidLcd", "Repeat", "FaceAttendance".
        """

        if channel is None:
            channels = []
        elif isinstance(channel, str):
            channels = [channel]
        else:
            channels = list(channel)

        payload = {
            "start_date": start_date,
            "channel": channels,
            "stream_type": stream_type,
            "search_type": search_type,
        }
        payload.update(kwargs)

        response = self._client._request(
            "/API/Playback/SearchMonth/Get",
            {
                "version": "1.0",
                "data": payload,
            },
        )

        return response.get(
            "data",
            {},
        )
