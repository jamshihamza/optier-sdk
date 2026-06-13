from __future__ import annotations


class RecordTagManager:
    """
    Playback Record Tag APIs.
    """

    def __init__(
        self,
        client,
    ) -> None:

        self._client = client

    def range(self) -> dict:

        response = self._client._request(
            "/API/Playback/Tag/Range",
            {
                "version": "1.0",
                "data": {},
            },
        )

        return response.get(
            "data",
            {},
        )

    def get(
        self,
        **kwargs,
    ) -> dict:

        response = self._client._request(
            "/API/Playback/Tag/Get",
            {
                "version": "1.0",
                "data": kwargs,
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
            "/API/Playback/Tag/Set",
            {
                "version": "1.0",
                "data": kwargs,
            },
        )