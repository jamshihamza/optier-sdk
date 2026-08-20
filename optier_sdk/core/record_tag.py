from __future__ import annotations

from typing import Any


class RecordTagManager:
    """
    Record / Playback > Record Tag API.

    Allows querying, adding, deleting, and renaming timeline bookmark tags on recorded video.
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
        Get capability constraints and parameter range for Record Tag operations.

        :return: Dict containing tag limits, pre-play/post-play duration options, and channel list.
        """

        response = self._client._request(
            "/API/Playback/Tag/Range",
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
        start_date: str,
        end_date: str,
        channel: list[str] | str | None = None,
        start_time: str = "00:00:00",
        end_time: str = "23:59:59",
        keyword: str = "",
        **kwargs,
    ) -> dict[str, Any]:
        """
        Search for video recording tags across channels and date/time intervals.

        :param start_date: Search start date in MM/DD/YYYY format (e.g. "08/01/2026").
        :param end_date: Search end date in MM/DD/YYYY format (e.g. "08/20/2026").
        :param channel: Channel string or list of channel strings (e.g. ["CH1"]). Defaults to ["CH1"].
        :param start_time: Search start time in hh:mm:ss format (default "00:00:00").
        :param end_time: Search end time in hh:mm:ss format (default "23:59:59").
        :param keyword: Keyword filter string (default "").
        :return: Dict containing Pre-play, Post-play, all_tag_num, and all_tag_info list.
        """

        if channel is None:
            channels = ["CH1"]
        elif isinstance(channel, str):
            channels = [channel]
        else:
            channels = list(channel)

        payload = {
            "channel": channels,
            "start_date": start_date,
            "start_time": start_time,
            "end_date": end_date,
            "end_time": end_time,
            "Keyword": keyword,
        }
        payload.update(kwargs)

        response = self._client._request(
            "/API/Playback/Tag/Get",
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
        tag_name: str,
        tag_date: str,
        tag_time: str,
        channel: list[str] | str,
        label_id: int = 0,
        record_id: int = 0,
        operate: int = 0,
        **kwargs,
    ) -> dict[str, Any]:
        """
        Add, delete, or modify a recording tag.

        :param tag_name: Tag name string (1..39 characters).
        :param tag_date: Tag date in MM/DD/YYYY format.
        :param tag_time: Tag time in hh:mm:ss format.
        :param channel: Channel string or list of channel strings (e.g. ["CH1"]).
        :param label_id: Tag/Label identifier (default 0).
        :param record_id: Target recording clip identifier (default 0).
        :param operate: Operation code: 0=Set/Add, 1=Delete, 2=Change name.
        :return: Device response payload.
        """

        if isinstance(channel, str):
            channels = [channel]
        else:
            channels = list(channel)

        payload = {
            "Tag_name": tag_name,
            "Tag_date": tag_date,
            "Tag_time": tag_time,
            "channel": channels,
            "label_id": label_id,
            "record_id": record_id,
            "operate": operate,
        }
        payload.update(kwargs)

        response = self._client._request(
            "/API/Playback/Tag/Set",
            {
                "version": "1.0",
                "data": payload,
            },
        )

        return response.get(
            "data",
            {},
        )