from __future__ import annotations


class GeneralManager:
    """
    System General APIs.
    """

    def __init__(
        self,
        client,
    ) -> None:

        self._client = client

    def range(self) -> dict:

        response = self._client._request(
            "/API/SystemConfig/General/Range",
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
            "/API/SystemConfig/General/Get",
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
            "/API/SystemConfig/General/Set",
            {
                "version": "1.0",
                "data": kwargs,
            },
        )