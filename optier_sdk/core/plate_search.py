from __future__ import annotations

from typing import Any


class PlateSearchManager:
    """
    AI > Recognition > SnapedObjects / SearchPlate (LPR Search & Forensic History) API.

    Executes forensic vehicle license plate searches against captured snapshot records,
    supports fuzzy matching (MaxErrorCharCnt), plate group filters, and paginated record retrieval.
    """

    def __init__(
        self,
        client,
    ) -> None:

        self._client = client

    def search(
        self,
        start_time: str,
        end_time: str,
        channels: list[int] | None = None,
        alarm_groups: list[int] | None = None,
        plate_numbers: list[str] | None = None,
        max_error_chars: int = 3,
        sort_type: int = 0,
        engine: int = 0,
        **kwargs,
    ) -> dict[str, Any]:
        """
        Execute snapshot license plate search task.

        :param start_time: Start timestamp (format: 'YYYY-MM-DD HH:MM:SS').
        :param end_time: End timestamp (format: 'YYYY-MM-DD HH:MM:SS').
        :param channels: List of channel numbers (empty list searches all channels).
        :param alarm_groups: List of target Plate group IDs (e.g. [1, 2]).
        :param plate_numbers: List of search plate query strings (e.g. ['KL71N']).
        :param max_error_chars: Fuzzy matching tolerance (0..5 allowed differing characters).
        :param sort_type: 0 for Ascending, 1 for Descending, 2 for None.
        :param engine: Search engine index (0 or 1).
        :return: Dict containing Result and Count of matching plate events.
        """

        payload: dict[str, Any] = {
            "MsgId": None,
            "StartTime": start_time,
            "EndTime": end_time,
            "Chn": channels if channels is not None else [],
            "AlarmGroup": alarm_groups if alarm_groups is not None else [],
            "PlatesId": plate_numbers if plate_numbers is not None else [],
            "MaxErrorCharCnt": max_error_chars,
            "SortType": sort_type,
            "Engine": engine,
        }
        payload.update(kwargs)

        response = self._client._request(
            "/API/AI/SnapedObjects/SearchPlate",
            {
                "version": "1.0",
                "data": payload,
            },
        )

        return response.get(
            "data",
            {},
        )

    def stop_search(
        self,
        engine: int = 0,
        **kwargs,
    ) -> dict[str, Any]:
        """
        Cancel active snapshot object/plate search.

        :param engine: Search engine index (0 or 1).
        :return: Device response payload.
        """

        payload: dict[str, Any] = {
            "MsgId": None,
            "Engine": engine,
        }
        payload.update(kwargs)

        response = self._client._request(
            "/API/AI/SnapedObjects/StopSearch",
            {
                "version": "1.0",
                "data": payload,
            },
        )

        return response.get(
            "data",
            {},
        )

    def get_by_index(
        self,
        start_index: int = 0,
        count: int = 20,
        simple_info: int = 0,
        with_object_image: int = 0,
        with_background: int = 0,
        engine: int = 0,
        **kwargs,
    ) -> dict[str, Any]:
        """
        Retrieve paginated license plate search results by index.

        :param start_index: Starting pagination offset (e.g. 0, 20, 40).
        :param count: Number of plate records to retrieve per page.
        :param simple_info: 1 for brief metadata summary, 0 for full metadata.
        :param with_object_image: 1 to include Base64 vehicle/plate crop, 0 to omit.
        :param with_background: 1 to include Base64 full scene image, 0 to omit.
        :param engine: Search engine index (0 or 1).
        :return: Dict containing TotalCount and SnapedObjInfo list.
        """

        payload: dict[str, Any] = {
            "MsgId": None,
            "Engine": engine,
            "StartIndex": start_index,
            "Count": count,
            "SimpleInfo": simple_info,
            "WithObjectImage": with_object_image,
            "WithBackgroud": with_background,
        }
        payload.update(kwargs)

        response = self._client._request(
            "/API/AI/SnapedObjects/GetByIndex",
            {
                "version": "1.0",
                "data": payload,
            },
        )

        return response.get(
            "data",
            {},
        )

    def get_by_id(
        self,
        uuids: list[str],
        with_object_image: int = 0,
        with_background: int = 0,
        engine: int = 0,
        **kwargs,
    ) -> dict[str, Any]:
        """
        Retrieve specific captured license plate records by unique UUID.

        :param uuids: List of unique record UUID strings.
        :param with_object_image: 1 to include Base64 crop image, 0 to omit.
        :param with_background: 1 to include Base64 full scene image, 0 to omit.
        :param engine: Search engine index.
        :return: Dict containing SnapedObjInfo matching requested UUIDs.
        """

        payload: dict[str, Any] = {
            "MsgId": None,
            "Engine": engine,
            "UUIds": uuids,
            "WithObjectImage": with_object_image,
            "WithBackgroud": with_background,
        }
        payload.update(kwargs)

        response = self._client._request(
            "/API/AI/SnapedObjects/GetById",
            {
                "version": "1.0",
                "data": payload,
            },
        )

        return response.get(
            "data",
            {},
        )
