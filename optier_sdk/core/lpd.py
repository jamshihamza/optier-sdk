from __future__ import annotations

from typing import Any


class LPDManager:
    """
    AI > Setup > License Plate Detection (LPD) API.

    Manages per-channel license plate detection rules, sensitivity thresholds,
    detection modes, enhancement levels, and alarm output linkages.
    """

    def __init__(
        self,
        client,
    ) -> None:

        self._client = client

    def range(
        self,
        channels: list[str] | None = None,
        page_type: str = "ChannelConfig",
        **kwargs,
    ) -> dict[str, Any]:
        """
        Get parameter range and limits for License Plate Detection.

        :param channels: Optional channel list filter (e.g. ['CH1', 'CH2']).
        :param page_type: 'ChannelConfig' or 'AlarmConfig'.
        :return: Dict containing channel capability limits and rules.
        """

        payload: dict[str, Any] = {
            "page_type": page_type,
        }
        if channels is not None:
            payload["channel"] = channels
        payload.update(kwargs)

        response = self._client._request(
            "/API/AI/Setup/LPD/Range",
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
        channels: list[str] | None = None,
        page_type: str = "ChannelConfig",
        **kwargs,
    ) -> dict[str, Any]:
        """
        Get active License Plate Detection configuration.

        :param channels: Optional channel list filter (e.g. ['CH1', 'CH2']).
        :param page_type: 'ChannelConfig' or 'AlarmConfig'.
        :return: Dict containing channel_info mapping with detection rules.
        """

        payload: dict[str, Any] = {
            "page_type": page_type,
        }
        if channels is not None:
            payload["channel"] = channels
        payload.update(kwargs)

        response = self._client._request(
            "/API/AI/Setup/LPD/Get",
            {
                "version": "1.0",
                "data": payload,
            },
        )

        return response.get(
            "data",
            {},
        )

    def set(
        self,
        channel_info: dict[str, Any],
        page_type: str = "ChannelConfig",
        **kwargs,
    ) -> dict[str, Any]:
        """
        Update License Plate Detection settings for specified channels.

        :param channel_info: Dict mapping channel keys (e.g. 'CH1') to detection settings.
        :param page_type: 'ChannelConfig' or 'AlarmConfig'.
        :return: Device response payload.
        """

        payload: dict[str, Any] = {
            "page_type": page_type,
            "channel_info": channel_info,
        }
        payload.update(kwargs)

        response = self._client._request(
            "/API/AI/Setup/LPD/Set",
            {
                "version": "1.0",
                "data": payload,
            },
        )

        return response.get(
            "data",
            {},
        )
