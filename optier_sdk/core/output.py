from __future__ import annotations


class OutputManager:
    """
    System Output APIs.
    """

    def __init__(
        self,
        client,
    ) -> None:

        self._client = client

    def range(self) -> dict:

        response = self._client._request(
            "/API/SystemConfig/Output/Range",
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
            "/API/SystemConfig/Output/Get",
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
        output: dict,
    ) -> None:

        self._client._request(
            "/API/SystemConfig/Output/Set",
            {
                "version": "1.0",
                "data": {
                    "output": output,
                },
            },
        )