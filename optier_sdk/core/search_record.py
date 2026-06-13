from __future__ import annotations


class SearchRecordManager:
    """
    Playback Search Record APIs.
    """

    def __init__(
        self,
        client,
    ) -> None:

        self._client = client

    def range(self) -> dict:

        response = self._client._request(
            "/API/Playback/SearchRecord/Range",
            {
                "version": "1.0",
                "data": {},
            },
        )

        return response.get(
            "data",
            {},
        )

    def search(
        self,
        **kwargs,
    ) -> dict:

        response = self._client._request(
            "/API/Playback/SearchRecord/Search",
            {
                "version": "1.0",
                "data": kwargs,
            },
        )

        return response.get(
            "data",
            {},
        )