from __future__ import annotations

from typing import Any


class SearchRecordManager:
    """
    Record / Playback > SearchRecord (Granular playback file segment and snapshot search) API.
    """

    def __init__(
        self,
        client,
    ) -> None:

        self._client = client

    def range(
        self,
        **kwargs,
    ) -> dict[str, Any]:
        """
        Get SearchRecord capability range including supported channels, stream modes, and record type limits.
        """

        payload = {}
        payload.update(kwargs)

        response = self._client._request(
            "/API/Playback/SearchRecord/Range",
            {
                "version": "1.0",
                "data": payload,
            },
        )

        return response.get(
            "data",
            {},
        )

    def search(
        self,
        start_date: str,
        end_date: str,
        channel: list[str] | str | None = None,
        start_time: str = "00:00:00",
        end_time: str = "23:59:59",
        record_type: int = 4294967295,
        record_type_ex: list[int] | None = None,
        stream_mode: str = "Mainstream",
        smart_region: list[int] | None = None,
        enable_smart_search: int = 0,
        **kwargs,
    ) -> list[list[dict[str, Any]]]:
        """
        Search granular video recording segments or pictures across channels and date/time intervals.

        :param start_date: Search start date in MM/DD/YYYY format (e.g. "08/20/2026").
        :param end_date: Search end date in MM/DD/YYYY format (e.g. "08/20/2026").
        :param channel: Channel or list of channels (e.g. ["CH1"], ["CH1", "CH2"]). Defaults to ["CH1"].
        :param start_time: Search start time in hh:mm:ss format (default "00:00:00").
        :param end_time: Search end time in hh:mm:ss format (default "23:59:59").
        :param record_type: Recording type bitmask (default 4294967295 / AllRecord).
        :param record_type_ex: Recording type 64-bit extension array (default [4294967295]).
        :param stream_mode: "Mainstream" or "Substream" (default "Mainstream").
        :param smart_region: Smart playback filter area array (15x22 grid).
        :param enable_smart_search: 1 to enable smart motion region filtering, 0 otherwise.
        :return: List of channel record segment lists.
        """

        if channel is None:
            channels = ["CH1"]
        elif isinstance(channel, str):
            channels = [channel]
        else:
            channels = list(channel)

        if record_type_ex is None:
            record_type_ex = [4294967295]

        if smart_region is None:
            smart_region = []

        payload = {
            "channel": channels,
            "start_date": start_date,
            "start_time": start_time,
            "end_date": end_date,
            "end_time": end_time,
            "record_type": record_type,
            "record_type_ex": record_type_ex,
            "stream_mode": stream_mode,
            "smart_region": smart_region,
            "enable_smart_search": enable_smart_search,
        }
        payload.update(kwargs)

        response = self._client._request(
            "/API/Playback/SearchRecord/Search",
            {
                "version": "1.0",
                "data": payload,
            },
        )

        return response.get("data", {}).get("record", [])