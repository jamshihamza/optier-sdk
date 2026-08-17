from __future__ import annotations

from typing import Any


class EncodeManager:
    """
    Stream > Encode Configuration APIs.

    Supports MainStream, SubStream, MobileStream, and EventStream pages.
    """

    SUPPORTED_PAGES = (
        "MainStream",
        "SubStream",
        "MobileStream",
        "EventStream",
    )

    def __init__(
        self,
        client,
    ) -> None:

        self._client = client

    def range(
        self,
        page: str = "MainStream",
    ) -> dict[str, Any]:
        """
        Get parameter range for the specified stream page.

        :param page: "MainStream", "SubStream", "MobileStream", or "EventStream"
        """

        response = self._client._request(
            f"/API/StreamConfig/{page}/Range",
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
        page: str = "MainStream",
    ) -> dict[str, Any]:
        """
        Get active encoding parameters for the specified stream page.

        :param page: "MainStream", "SubStream", "MobileStream", or "EventStream"
        """

        response = self._client._request(
            f"/API/StreamConfig/{page}/Get",
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
        page: str = "MainStream",
        **kwargs,
    ) -> None:
        """
        Set encoding parameters for the specified stream page.

        :param page: "MainStream", "SubStream", "MobileStream", or "EventStream"
        """

        self._client._request(
            f"/API/StreamConfig/{page}/Set",
            {
                "version": "1.0",
                "data": kwargs,
            },
        )
