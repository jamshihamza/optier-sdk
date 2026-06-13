from __future__ import annotations


class LogManager:
    """
    Maintenance Log APIs.
    """

    def __init__(self, client) -> None:
        self._client = client

    def range(self) -> dict:

        response = self._client._request(
            "/API/Maintenance/Log/Range",
            {
                "version": "1.0",
                "data": {},
            },
        )

        return response.get("data", {})

    def search(
        self,
        *,
        start_date: str,
        start_time: str,
        end_date: str,
        end_time: str,
        main_type: str = "All",
        sub_type: str = "All",
    ) -> list[dict]:

        response = self._client._request(
            "/API/Maintenance/Log/Search",
            {
                "version": "1.0",
                "data": {
                    "start_date": start_date,
                    "start_time": start_time,
                    "end_date": end_date,
                    "end_time": end_time,
                    "main_type": main_type,
                    "sub_type": sub_type,
                },
            },
        )

        return response.get("data", {}).get("log", [])