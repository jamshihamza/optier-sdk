from __future__ import annotations

from typing import Any


class FaceDatabaseManager:
    """
    AI > Recognition > Faces (Face Database & Person Management) API.

    Manages registered face person records, enrolled face profile pictures (Base64),
    feature extraction, biometric metadata, and person watchlist assignments.
    """

    def __init__(
        self,
        client,
    ) -> None:

        self._client = client

    def add(
        self,
        face_info: list[dict[str, Any]],
        msg_id: Any | None = None,
        **kwargs,
    ) -> dict[str, Any]:
        """
        Enroll new face person records into the face database.

        :param face_info: List of person dicts containing GrpId, Image1 (base64), Name,
                          Sex (0: male, 1: female), Age, IdCode, Phone, Email, etc.
        :param msg_id: Optional message ID tracker.
        :return: Device response payload with created face IDs and MD5 hashes.
        """

        payload: dict[str, Any] = {
            "MsgId": msg_id,
            "Count": len(face_info),
            "FaceInfo": face_info,
        }
        payload.update(kwargs)

        response = self._client._request(
            "/API/AI/Faces/Add",
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
        face_info: list[dict[str, Any]],
        msg_id: Any | None = None,
        **kwargs,
    ) -> dict[str, Any]:
        """
        Update existing face person records.

        :param face_info: List of person dicts containing Id and updated fields.
        :param msg_id: Optional message ID tracker.
        :return: Device response payload.
        """

        payload: dict[str, Any] = {
            "MsgId": msg_id,
            "Count": len(face_info),
            "FaceInfo": face_info,
        }
        payload.update(kwargs)

        response = self._client._request(
            "/API/AI/Faces/Modify",
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
        face_ids: list[int],
        msg_id: Any | None = None,
        **kwargs,
    ) -> dict[str, Any]:
        """
        Remove face person records from the database.

        :param face_ids: List of face IDs to delete.
        :param msg_id: Optional message ID tracker.
        :return: Device response payload.
        """

        face_items = [{"Id": fid} for fid in face_ids]
        payload: dict[str, Any] = {
            "MsgId": msg_id,
            "Count": len(face_items),
            "FaceInfo": face_items,
        }
        payload.update(kwargs)

        response = self._client._request(
            "/API/AI/Faces/Remove",
            {
                "version": "1.0",
                "data": payload,
            },
        )

        return response.get(
            "data",
            {},
        )

    def get_images_feature(
        self,
        images: list[str],
        **kwargs,
    ) -> dict[str, Any]:
        """
        Extract facial feature eigenvalue vector from base64 image data.

        :param images: List of Base64 encoded JPEG image strings.
        :return: Dict containing FeatureVersion, Features array, and Results codes.
        """

        payload: dict[str, Any] = {
            "Images": images,
        }
        payload.update(kwargs)

        response = self._client._request(
            "/API/AI/Faces/GetImagesFeature",
            {
                "version": "1.0",
                "data": payload,
            },
        )

        return response.get(
            "data",
            {},
        )
