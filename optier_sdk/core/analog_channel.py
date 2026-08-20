from __future__ import annotations

from typing import Any


class AnalogChannelManager:
    """
    Channel > Analog Channel (Analog/BNC/Coaxial Channel Configuration on DVR/XVR/Hybrid devices) APIs.
    """

    def __init__(
        self,
        client,
    ) -> None:

        self._client = client

    def range(
        self,
        page_type: str = "ChannelConfig",
        **kwargs,
    ) -> dict[str, Any]:
        """
        Get parameter range for Analog Channel configuration.
        """

        payload = {"page_type": page_type}
        payload.update(kwargs)

        response = self._client._request(
            "/API/ChannelConfig/AnalogChannel/Range",
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
        page_type: str = "ChannelConfig",
        **kwargs,
    ) -> dict[str, Any]:
        """
        Get active Analog Channel parameters.
        """

        payload = {"page_type": page_type}
        payload.update(kwargs)

        response = self._client._request(
            "/API/ChannelConfig/AnalogChannel/Get",
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
        **kwargs,
    ) -> None:
        """
        Set Analog Channel parameters.
        """

        self._client._request(
            "/API/ChannelConfig/AnalogChannel/Set",
            {
                "version": "1.0",
                "data": kwargs,
            },
        )
