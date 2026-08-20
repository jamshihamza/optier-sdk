from __future__ import annotations

from typing import Any


class AddedPlatesManager:
    """
    AI > Recognition > AddedPlates (Enrolled Vehicle Database Query & Forensics) API.

    Queries and enumerates enrolled vehicle license plate records from the device database,
    supporting counting, group filtering, plate number querying, and owner profile retrieval.
    """

    def __init__(
        self,
        client,
    ) -> None:

        self._client = client

    def get_count(
        self,
        group_ids: list[int] | None = None,
        plate_info: list[dict[str, Any]] | None = None,
        msg_id: Any | None = None,
        **kwargs,
    ) -> dict[str, Any]:
        """
        Get count of enrolled vehicle license plates matching filter criteria.

        :param group_ids: Optional list of group IDs to filter.
        :param plate_info: Optional list of query plate filter dicts.
        :param msg_id: Optional message ID tracker.
        :return: Dict containing matching enrolled plate count.
        """

        payload: dict[str, Any] = {
            "MsgId": msg_id,
        }
        if group_ids is not None:
            payload["GrpId"] = group_ids
        if plate_info is not None:
            payload["PlateInfo"] = plate_info
        payload.update(kwargs)

        response = self._client._request(
            "/API/AI/AddedPlates/GetCount",
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
        plate_info: list[dict[str, Any]] | None = None,
        msg_id: Any | None = None,
        **kwargs,
    ) -> dict[str, Any]:
        """
        Query enrolled license plate numbers matching filter criteria.

        :param group_ids: Optional list of group IDs to filter.
        :param plate_info: Optional list of query plate filter dicts.
        :param msg_id: Optional message ID tracker.
        :return: Dict containing matching PlatesId list.
        """

        payload: dict[str, Any] = {
            "MsgId": msg_id,
        }
        if group_ids is not None:
            payload["GrpId"] = group_ids
        if plate_info is not None:
            payload["PlateInfo"] = plate_info
        payload.update(kwargs)

        response = self._client._request(
            "/API/AI/AddedPlates/GetId",
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
        plate_numbers: list[str],
        msg_id: Any | None = None,
        **kwargs,
    ) -> dict[str, Any]:
        """
        Retrieve full enrolled vehicle owner records for specific license plate numbers.

        :param plate_numbers: List of license plate numbers.
        :param msg_id: Optional message ID tracker.
        :return: Dict containing PlateInfo list with owner details, vehicle brand, and color.
        """

        plate_items = [{"Id": pid} for pid in plate_numbers]
        payload: dict[str, Any] = {
            "MsgId": msg_id,
            "PlateInfo": plate_items,
        }
        payload.update(kwargs)

        response = self._client._request(
            "/API/AI/AddedPlates/GetById",
            {
                "version": "1.0",
                "data": payload,
            },
        )

        return response.get(
            "data",
            {},
        )
