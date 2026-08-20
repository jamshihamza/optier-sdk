from __future__ import annotations

from typing import Any


class PlaybackPageManager:
    """
    Record / Playback > Playback Page API.

    Provides comprehensive playback configuration parameters and capability ranges
    for Normal, Smart/AI, Picture, HumanVehicle, PidLcd, LicensePlate, FaceAttendance,
    and FaceAttribute playback modalities.
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
        Get capability parameters and range limits for all Record Playback modalities.

        :return: Dict containing capabilities for Normal, Smart, Picture, HumanVehicle,
                 PidLcd, LicensePlate, FaceAttendance, supportFaceAttr, and param_limit.
        """

        response = self._client._request(
            "/API/Playback/PlaybackPage/Range",
            {
                "version": "1.0",
                "data": {},
            },
        )

        return response.get(
            "data",
            {},
        )
