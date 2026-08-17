from __future__ import annotations

from typing import Any


class SoundDetectionManager:
    """
    Alarm / Intelligent Video Analytics > Sound Detection APIs.
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
        Get parameter range for Sound Detection configuration across channels.

        :param page_type: Optional page type, e.g. "AlarmConfig", "ChannelConfig", "AllConfig", or None.
        """

        data: dict[str, Any] = {}
        if page_type is not None:
            data["page_type"] = page_type

        response = self._client._request(
            "/API/AlarmConfig/Intelligent/SoundDetection/Range",
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
        Get active Sound Detection configuration across channels.

        :param page_type: Optional page type, e.g. "AlarmConfig", "ChannelConfig", "AllConfig", or None.
        """

        data: dict[str, Any] = {}
        if page_type is not None:
            data["page_type"] = page_type

        response = self._client._request(
            "/API/AlarmConfig/Intelligent/SoundDetection/Get",
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
        Set Sound Detection configuration.
        """

        self._client._request(
            "/API/AlarmConfig/Intelligent/SoundDetection/Set",
            {
                "version": "1.0",
                "data": kwargs,
            },
        )
