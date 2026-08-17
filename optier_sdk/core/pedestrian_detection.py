from __future__ import annotations

from typing import Any


class PedestrianDetectionManager:
    """
    Alarm / Intelligent Video Analytics > Pedestrian Detection (PD) APIs.
    """

    def __init__(
        self,
        client,
    ) -> None:

        self._client = client

    def range(
        self,
        page_type: str | None = "AlarmConfig",
    ) -> dict[str, Any]:
        """
        Get parameter range for Pedestrian Detection configuration across channels.

        :param page_type: Optional page type, e.g. "AlarmConfig", "ChannelConfig", "AllConfig", or None.
        """

        data: dict[str, Any] = {}
        if page_type is not None:
            data["page_type"] = page_type

        response = self._client._request(
            "/API/AlarmConfig/Intelligent/PD/Range",
            {
                "version": "1.0",
                "data": data,
            },
        )

        return response.get(
            "data",
            {},
        )

    def get(
        self,
        page_type: str | None = "AlarmConfig",
    ) -> dict[str, Any]:
        """
        Get active Pedestrian Detection configuration across channels.

        :param page_type: Optional page type, e.g. "AlarmConfig", "ChannelConfig", "AllConfig", or None.
        """

        data: dict[str, Any] = {}
        if page_type is not None:
            data["page_type"] = page_type

        response = self._client._request(
            "/API/AlarmConfig/Intelligent/PD/Get",
            {
                "version": "1.0",
                "data": data,
            },
        )

        return response.get(
            "data",
            {},
        )

    def set(
        self,
        **kwargs,
    ) -> None:
        """
        Set Pedestrian Detection configuration.
        """

        self._client._request(
            "/API/AlarmConfig/Intelligent/PD/Set",
            {
                "version": "1.0",
                "data": kwargs,
            },
        )
