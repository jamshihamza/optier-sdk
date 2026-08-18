from __future__ import annotations

from typing import Any


class VoiceAssistantManager:
    """
    Network > Voice Assistant / Smart Home (Amazon Alexa, Google Assistant) APIs.
    """

    def __init__(
        self,
        client,
    ) -> None:

        self._client = client

    def range(
        self,
        smart_home_page: str | None = None,
    ) -> dict[str, Any]:
        """
        Get parameter range for Voice Assistant configuration.

        :param smart_home_page: Voice assistant type ("Amazon", "Google").
        """

        payload: dict[str, Any] = {}
        if smart_home_page is not None:
            payload["SmartHomePage"] = smart_home_page

        response = self._client._request(
            "/API/NetworkConfig/SMARTHOME/Range",
            {
                "version": "1.0",
                "data": payload,
            },
        )

        return response.get(
            "data",
            {},
        )

    def get(
        self,
        smart_home_page: str | None = None,
    ) -> dict[str, Any]:
        """
        Get active Voice Assistant configuration.

        :param smart_home_page: Voice assistant type ("Amazon", "Google").
        """

        payload: dict[str, Any] = {}
        if smart_home_page is not None:
            payload["SmartHomePage"] = smart_home_page

        response = self._client._request(
            "/API/NetworkConfig/SMARTHOME/Get",
            {
                "version": "1.0",
                "data": payload,
            },
        )

        return response.get(
            "data",
            {},
        )

    def control(
        self,
        **kwargs,
    ) -> None:
        """
        Control Voice Assistant binding and stream settings.
        """

        self._client._request(
            "/API/NetworkConfig/SMARTHOME/Control",
            {
                "version": "1.0",
                "data": kwargs,
            },
        )

    def set(
        self,
        **kwargs,
    ) -> None:
        """
        Set / control Voice Assistant configuration.
        """

        self.control(**kwargs)
