from __future__ import annotations

from typing import Any


class AddedFacesManager:
    """
    AI > Recognition > AddedFaces (Enrolled Face Database Query & Forensics) API.

    Queries and enumerates enrolled person profile records from the device face library,
    supporting filtering by name, group, gender, age, ID number, and paginated retrieval
    with portraits, eigenvalues, and MD5 hashes.
    """

    def __init__(
        self,
        client,
    ) -> None:

        self._client = client

    def search(
        self,
        face_info: list[dict[str, Any]] | None = None,
        msg_id: Any | None = None,
        **kwargs,
    ) -> dict[str, Any]:
        """
        Execute query against enrolled face database records.

        :param face_info: Optional list of query filter dicts (e.g. [{'GrpId': 1, 'Name': 'Mike'}]).
        :param msg_id: Optional message ID tracker.
        :return: Device response payload.
        """

        payload: dict[str, Any] = {
            "MsgId": msg_id,
            "FaceInfo": face_info if face_info is not None else [],
        }
        payload.update(kwargs)

        response = self._client._request(
            "/API/AI/AddedFaces/Search",
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
        with_image: int = 0,
        with_feature: int = 0,
        need_md5: int = 0,
        msg_id: Any | None = None,
        **kwargs,
    ) -> dict[str, Any]:
        """
        Retrieve paginated enrolled face records from the face database.

        :param start_index: Pagination starting index (e.g. 0, 20, 40).
        :param count: Number of face records to retrieve per page.
        :param simple_info: 1 for abbreviated summary (Id, GrpId, Name), 0 for full profile.
        :param with_image: 1 to include Base64 portrait image, 0 to omit.
        :param with_feature: 1 to include Base64 facial eigenvalue, 0 to omit.
        :param need_md5: 1 to calculate and return image MD5, 0 to omit.
        :param msg_id: Optional message ID tracker.
        :return: Dict containing Result, Count, and FaceInfo list.
        """

        payload: dict[str, Any] = {
            "Msgid": msg_id,
            "StartIndex": start_index,
            "count": count,
            "SimpleInfo": simple_info,
            "WithImage": with_image,
            "WithFeature": with_feature,
            "NeedMD5": need_md5,
        }
        payload.update(kwargs)

        response = self._client._request(
            "/API/AI/AddedFaces/GetByIndex",
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
        face_ids: list[int],
        with_image: int = 0,
        with_feature: int = 0,
        msg_id: Any | None = None,
        **kwargs,
    ) -> dict[str, Any]:
        """
        Retrieve full enrolled face profile details for specific Face IDs.

        :param face_ids: List of enrolled face IDs.
        :param with_image: 1 to include Base64 portrait image, 0 to omit.
        :param with_feature: 1 to include Base64 facial eigenvalue, 0 to omit.
        :param msg_id: Optional message ID tracker.
        :return: Dict containing FaceInfo matching requested IDs.
        """

        payload: dict[str, Any] = {
            "MsgId": msg_id,
            "FaceId": face_ids,
            "WithImage": with_image,
            "WithFeature": with_feature,
        }
        payload.update(kwargs)

        response = self._client._request(
            "/API/AI/AddedFaces/GetById",
            {
                "version": "1.0",
                "data": payload,
            },
        )

        return response.get(
            "data",
            {},
        )

    def get_id(
        self,
        group_ids: list[int] | None = None,
        msg_id: Any | None = None,
        **kwargs,
    ) -> dict[str, Any]:
        """
        Query enrolled face IDs filtered by group.

        :param group_ids: Optional list of group IDs to filter.
        :param msg_id: Optional message ID tracker.
        :return: Dict containing matching Face IDs list.
        """

        payload: dict[str, Any] = {
            "MsgId": msg_id,
        }
        if group_ids is not None:
            payload["GrpId"] = group_ids
        payload.update(kwargs)

        response = self._client._request(
            "/API/AI/AddedFaces/GetId",
            {
                "version": "1.0",
                "data": payload,
            },
        )

        return response.get(
            "data",
            {},
        )
