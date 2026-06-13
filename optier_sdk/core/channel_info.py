from __future__ import annotations


class SystemChannelInfoManager:
    """
    System -> Channel Information APIs.
    """

    def __init__(
        self,
        client,
    ) -> None:

        self._client = client

    def get(self) -> dict:

        response = self._client._request(
            "/API/SystemInfo/Channel/Get",
            {
                "version": "1.0",
                "data": {},
            },
        )

        return response.get(
            "data",
            {},
        )