from __future__ import annotations


class DateTimeManager:
    """
    System Date & Time APIs.
    """

    def __init__(self, client) -> None:

        self._client = client

    def get(self) -> dict:

        response = self._client._request(
            "/API/SystemConfig/DateTime/Get",
            {
                "version": "1.0",
                "data": {},
            },
        )

        return response.get("data", {})

    def range(self) -> dict:

        response = self._client._request(
            "/API/SystemConfig/DateTime/Range",
            {
                "version": "1.0",
                "data": {},
            },
        )

        return response.get("data", {})

    def set(
        self,
        **kwargs,
    ) -> None:

        self._client._request(
            "/API/SystemConfig/DateTime/Set",
            {
                "version": "1.0",
                "data": kwargs,
            },
        )