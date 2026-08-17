from __future__ import annotations

from typing import Any


class RecordConfigManager:
    """
    Record > Record Configuration APIs.
    """

    def __init__(
        self,
        client,
    ) -> None:

        self._client = client

    def range(self) -> dict[str, Any]:
        """
        Get parameter range for Record Configuration across channels.
        """

        response = self._client._request(
            "/API/RecordConfig/Range",
            {
                "version": "1.0",
                "data": {},
            },
        )

        return response.get(
            "data",
            {},
        )

    def get(self) -> dict[str, Any]:
        """
        Get active Record Configuration across channels.
        """

        response = self._client._request(
            "/API/RecordConfig/Get",
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
        Set Record Configuration.
        """

        self._client._request(
            "/API/RecordConfig/Set",
            {
                "version": "1.0",
                "data": kwargs,
            },
        )
