from __future__ import annotations

from typing import Any


class FDAttendanceManager:
    """
    AI > Face Attendance (NVR Dedicated Staff Attendance & Time Tracking) API.

    Manages NVR face recognition attendance reporting, shift schedules,
    working days, on-duty/off-duty times, email dispatch, and monitoring channel bindings.
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
        Get parameter range and capabilities for Face Attendance.

        :return: Dict containing supported modes (Day, Week, Month), channel limits, and group options.
        """

        response = self._client._request(
            "/API/AI/FDAttendance/Range",
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
        **kwargs,
    ) -> dict[str, Any]:
        """
        Get active Face Attendance configuration and shift settings.

        :return: Dict containing fd_atd_info mapping.
        """

        response = self._client._request(
            "/API/AI/FDAttendance/Get",
            {
                "version": "1.0",
                "data": {},
            },
        )

        return response.get(
            "data",
            {},
        )

    def set(
        self,
        fd_atd_info: dict[str, Any],
        **kwargs,
    ) -> dict[str, Any]:
        """
        Update Face Attendance settings.

        :param fd_atd_info: Dict containing attendance rules (enable, mode, on_duty_time,
                            off_duty_time, working_days, channel, group, send_email).
        :return: Device response payload.
        """

        payload: dict[str, Any] = {
            "fd_atd_info": fd_atd_info,
        }
        payload.update(kwargs)

        response = self._client._request(
            "/API/AI/FDAttendance/Set",
            {
                "version": "1.0",
                "data": payload,
            },
        )

        return response.get(
            "data",
            {},
        )
