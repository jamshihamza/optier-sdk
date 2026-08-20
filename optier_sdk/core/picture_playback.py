from __future__ import annotations

from typing import Any


class PicturePlaybackManager:
    """
    Record / Playback > Pic Playback (Snapshot search and base64 image retrieval) API.
    """

    def __init__(
        self,
        client,
    ) -> None:

        self._client = client

    def search(
        self,
        start_date: str,
        end_date: str,
        channel: list[str] | str | None = None,
        start_time: str = "00:00:00",
        end_time: str = "23:59:59",
        record_type: int = 524287,
        record_type_ex: list[int] | None = None,
        pic_sort: int = 0,
        **kwargs,
    ) -> dict[str, Any]:
        """
        Search for recorded snapshot pictures across channels and date/time intervals.

        :param start_date: Search start date in MM/DD/YYYY format (e.g. "08/01/2026").
        :param end_date: Search end date in MM/DD/YYYY format (e.g. "08/20/2026").
        :param channel: Optional channel string or list of channel strings (e.g. ["CH1"]). Defaults to ["CH1"].
        :param start_time: Search start time in hh:mm:ss format (default "00:00:00").
        :param end_time: Search end time in hh:mm:ss format (default "23:59:59").
        :param record_type: Snapshot record type bitmask (default 524287).
        :param record_type_ex: 64-bit record type extension array (default [4294967295]).
        :param pic_sort: 0 for sequential order, 1 for reverse sequence.
        :return: Dict containing overload flag, all_pic_num, and all_pic_info token list.
        """

        if channel is None:
            channels = ["CH1"]
        elif isinstance(channel, str):
            channels = [channel]
        else:
            channels = list(channel)

        if record_type_ex is None:
            record_type_ex = [4294967295]

        payload = {
            "channel": channels,
            "start_date": start_date,
            "start_time": start_time,
            "end_date": end_date,
            "end_time": end_time,
            "record_type": record_type,
            "record_type_ex": record_type_ex,
            "pic_sort": pic_sort,
        }
        payload.update(kwargs)

        response = self._client._request(
            "/API/Playback/Picture/Get",
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
        pic_info: str,
        **kwargs,
    ) -> dict[str, Any]:
        """
        Retrieve specific picture metadata and base64-encoded image content by pic_info token.

        :param pic_info: Picture token string obtained from search().
        :return: Dict containing picture object with channel, timestamp, and base64 image data.
        """

        payload = {"pic_info": pic_info}
        payload.update(kwargs)

        response = self._client._request(
            "/API/Playback/Picture/Get",
            {
                "version": "1.0",
                "data": payload,
            },
        )

        return response.get("data", {}).get("picture", {})
