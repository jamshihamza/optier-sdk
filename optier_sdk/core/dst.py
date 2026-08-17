from __future__ import annotations


class DSTManager:
    """
    System DST (Daylight Saving Time) APIs.
    """

    def __init__(
        self,
        client,
    ) -> None:

        self._client = client

    def range(self) -> dict:
        """
        Get supported DST parameter range.
        """

        response = self._client._request(
            "/API/SystemConfig/DST/Range",
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
        """
        Get current DST configuration.
        """

        response = self._client._request(
            "/API/SystemConfig/DST/Get",
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
        """
        Set DST configuration.
        """

        self._client._request(
            "/API/SystemConfig/DST/Set",
            {
                "version": "1.0",
                "data": kwargs,
            },
        )
