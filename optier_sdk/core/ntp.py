from __future__ import annotations


class NTPManager:
    """
    System NTP APIs.
    """

    def __init__(
        self,
        client,
    ) -> None:

        self._client = client

    def range(self) -> dict:

        response = self._client._request(
            "/API/SystemConfig/NTP/Range",
            {
                "version": "1.0",
                "data": {},
            },
        )

        return response.get(
            "data",
            {},
        )

    def get(self) -> dict:

        response = self._client._request(
            "/API/SystemConfig/NTP/Get",
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
        **kwargs,
    ) -> None:

        self._client._request(
            "/API/SystemConfig/NTP/Set",
            {
                "version": "1.0",
                "data": kwargs,
            },
        )