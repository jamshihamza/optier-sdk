from __future__ import annotations

from typing import Any


class FaceSearchManager:
    """
    AI > Recognition > SnapedFaces (Face Search, Event History & Matching) API.

    Executes forensic face searches against captured face snapshots,
    queries match confidence scores, retrieves snapshot images, and polls
    real-time face alarm events.
    """

    def __init__(
        self,
        client,
    ) -> None:

        self._client = client

    def get_vhd_log_count(
        self,
        start_time: str,
        end_time: str,
        channels: list[int] | None = None,
        types: list[int] | None = None,
        engine: int = 0,
        **kwargs,
    ) -> dict[str, Any]:
        """
        Get captured VHD face and object count within a time range.

        :param start_time: Start time string (format: 'YYYY-MM-DD HH:MM:SS').
        :param end_time: End time string (format: 'YYYY-MM-DD HH:MM:SS').
        :param channels: List of channel indexes (empty list means all channels).
        :param types: List of object types (0: face, 1: human figure, 2: vehicle, etc.).
        :param engine: Search engine index (0 or 1).
        :return: Dict containing Result code and Count array.
        """

        payload: dict[str, Any] = {
            "MsgId": None,
            "StartTime": start_time,
            "EndTime": end_time,
            "Chn": channels if channels is not None else [],
            "Type": types if types is not None else [0, 1, 2],
            "Engine": engine,
        }
        payload.update(kwargs)

        response = self._client._request(
            "/API/AI/VhdLogCount/Get",
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
        start_time: str,
        end_time: str,
        channels: list[int] | None = None,
        group_id: int = 0,
        similarity: int = 70,
        engine: int = 0,
        **kwargs,
    ) -> dict[str, Any]:
        """
        Execute snapshot face search / match task.

        :param start_time: Search start timestamp (format: 'YYYY-MM-DD HH:MM:SS').
        :param end_time: Search end timestamp (format: 'YYYY-MM-DD HH:MM:SS').
        :param channels: List of channel numbers (empty list means all channels).
        :param group_id: Target Face group ID (0 means all groups).
        :param similarity: Minimum match similarity threshold (0..100).
        :param engine: Search engine index (0 or 1).
        :return: Dict containing Result and total Count of matching faces.
        """

        payload: dict[str, Any] = {
            "MsgId": None,
            "StartTime": start_time,
            "EndTime": end_time,
            "Chn": channels if channels is not None else [],
            "GrpId": group_id,
            "Similarity": similarity,
            "Engine": engine,
        }
        payload.update(kwargs)

        response = self._client._request(
            "/API/AI/SnapedFaces/Search",
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
        Cancel active snapshot face search task.

        :param engine: Search engine index (0 or 1).
        :return: Device response payload.
        """

        payload: dict[str, Any] = {
            "MsgId": None,
            "Engine": engine,
        }
        payload.update(kwargs)

        response = self._client._request(
            "/API/AI/SnapedFaces/StopSearch",
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
        matched_faces: int = 0,
        simple_info: int = 0,
        with_face_image: int = 0,
        with_body_image: int = 0,
        with_background: int = 0,
        with_feature: int = 0,
        engine: int = 0,
        **kwargs,
    ) -> dict[str, Any]:
        """
        Retrieve paginated face search results by index.

        :param start_index: Starting pagination offset (e.g. 0, 20, 40).
        :param count: Number of face records to retrieve per page.
        :param matched_faces: 1 to get matched watchlist faces, 0 to get captured faces.
        :param simple_info: 1 for brief metadata summary, 0 for complete metadata.
        :param with_face_image: 1 to include Base64 face crop image, 0 to omit.
        :param with_body_image: 1 to include Base64 body crop image, 0 to omit.
        :param with_background: 1 to include Base64 full scene image, 0 to omit.
        :param with_feature: 1 to include eigenvalue vector, 0 to omit.
        :param engine: Search engine index (0 or 1).
        :return: Dict containing TotalCount and SnapedFaceInfo list.
        """

        payload: dict[str, Any] = {
            "MsgId": None,
            "Engine": engine,
            "MatchedFaces": matched_faces,
            "StartIndex": start_index,
            "Count": count,
            "SimpleInfo": simple_info,
            "WithFaceImage": with_face_image,
            "WithBodyImage": with_body_image,
            "WithBackgroud": with_background,
            "WithFeature": with_feature,
        }
        payload.update(kwargs)

        response = self._client._request(
            "/API/AI/SnapedFaces/GetByIndex",
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
        with_face_image: int = 0,
        with_body_image: int = 0,
        with_background: int = 0,
        with_feature: int = 0,
        engine: int = 0,
        **kwargs,
    ) -> dict[str, Any]:
        """
        Retrieve specific captured face records by unique UUID.

        :param uuids: List of unique face record UUID strings.
        :param with_face_image: 1 to include Base64 face crop image, 0 to omit.
        :param with_body_image: 1 to include Base64 body crop image, 0 to omit.
        :param with_background: 1 to include Base64 full scene image, 0 to omit.
        :param with_feature: 1 to include eigenvalue vector, 0 to omit.
        :param engine: Search engine index.
        :return: Dict containing SnapedFaceInfo matching requested UUIDs.
        """

        payload: dict[str, Any] = {
            "MsgId": None,
            "Engine": engine,
            "UUIds": uuids,
            "WithFaceImage": with_face_image,
            "WithBodyImage": with_body_image,
            "WithBackgroud": with_background,
            "WithFeature": with_feature,
        }
        payload.update(kwargs)

        response = self._client._request(
            "/API/AI/SnapedFaces/GetById",
            {
                "version": "1.0",
                "data": payload,
            },
        )

        return response.get(
            "data",
            {},
        )

    def get_realtime_alarm(
        self,
        **kwargs,
    ) -> dict[str, Any]:
        """
        Poll real-time AI captured face/object events and cross-counting alarms.

        :return: Dict containing FaceInfo, SnapedObjInfo, and CCScenarioRTInfo real-time data.
        """

        response = self._client._request(
            "/API/AI/processAlarm/Get",
            {
                "version": "1.0",
                "data": {},
            },
        )

        return response.get(
            "data",
            {},
        )
