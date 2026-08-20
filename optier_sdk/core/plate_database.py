from __future__ import annotations

from typing import Any


class PlateDatabaseManager:
    """
    AI > Recognition > Plates (License Plate Database & Vehicle Management) API.

    Manages enrolled vehicle license plate records, vehicle brands, models,
    plate colors, vehicle owner profiles, and watchlist group assignments.
    """

    def __init__(
        self,
        client,
    ) -> None:

        self._client = client

    def add(
        self,
        plate_info: list[dict[str, Any]],
        msg_id: Any | None = None,
        **kwargs,
    ) -> dict[str, Any]:
        """
        Enroll new vehicle license plates into the database.

        :param plate_info: List of vehicle plate dicts containing Id (plate number string, 1..15 chars),
                          GrpId (group ID), PlateColor (0: blue, 1: green, 2: yellow, 3: black, 4: white, 5: other),
                          CarBrand, CarType, Owner, IdCode, Phone, Domicile, Remark, EnableChnAlarm.
        :param msg_id: Optional message ID tracker.
        :return: Device response payload with Result array.
        """

        payload: dict[str, Any] = {
            "MsgId": msg_id,
            "PlateInfo": plate_info,
        }
        payload.update(kwargs)

        response = self._client._request(
            "/API/AI/Plates/Add",
            {
                "version": "1.0",
                "data": payload,
            },
        )

        return response.get(
            "data",
            {},
        )

    def modify(
        self,
        plate_info: list[dict[str, Any]],
        msg_id: Any | None = None,
        **kwargs,
    ) -> dict[str, Any]:
        """
        Modify existing license plate details and owner records.

        :param plate_info: List of plate dicts containing target Id and updated fields.
        :param msg_id: Optional message ID tracker.
        :return: Device response payload.
        """

        payload: dict[str, Any] = {
            "MsgId": msg_id,
            "PlateInfo": plate_info,
        }
        payload.update(kwargs)

        response = self._client._request(
            "/API/AI/Plates/Modify",
            {
                "version": "1.0",
                "data": payload,
            },
        )

        return response.get(
            "data",
            {},
        )

    def remove(
        self,
        plate_numbers: list[str],
        msg_id: Any | None = None,
        **kwargs,
    ) -> dict[str, Any]:
        """
        Remove license plate records from the database.

        :param plate_numbers: List of license plate number strings to delete.
        :param msg_id: Optional message ID tracker.
        :return: Device response payload.
        """

        plate_items = [{"Id": pid} for pid in plate_numbers]
        payload: dict[str, Any] = {
            "MsgId": msg_id,
            "PlateInfo": plate_items,
        }
        payload.update(kwargs)

        response = self._client._request(
            "/API/AI/Plates/Remove",
            {
                "version": "1.0",
                "data": payload,
            },
        )

        return response.get(
            "data",
            {},
        )

    def change_group(
        self,
        plate_numbers: list[str],
        new_group_id: int,
        msg_id: Any | None = None,
        **kwargs,
    ) -> dict[str, Any]:
        """
        Move license plates to a different watchlist group.

        :param plate_numbers: List of license plate number strings.
        :param new_group_id: Target group ID.
        :param msg_id: Optional message ID tracker.
        :return: Device response payload.
        """

        plate_items = [{"Id": pid, "GrpId": new_group_id} for pid in plate_numbers]
        payload: dict[str, Any] = {
            "MsgId": msg_id,
            "PlateInfo": plate_items,
        }
        payload.update(kwargs)

        response = self._client._request(
            "/API/AI/Plates/Change",
            {
                "version": "1.0",
                "data": payload,
            },
        )

        return response.get(
            "data",
            {},
        )
