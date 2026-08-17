from __future__ import annotations

from typing import Any


class NetworkBaseManager:
    """
    Network > Network Base Configuration APIs.
    """

    def __init__(
        self,
        client,
    ) -> None:

        self._client = client

    def range(
        self,
        page_type: str | None = None,
    ) -> dict[str, Any]:
        """
        Get supported parameter range for Network Base.

        :param page_type: Optional page type, e.g. "net_general".
        """

        data: dict[str, Any] = {}
        if page_type is not None:
            data["page_type"] = page_type

        response = self._client._request(
            "/API/NetworkConfig/NetBase/Range",
            {
                "version": "1.0",
                "data": data,
            },
        )

        return response.get(
            "data",
            {},
        )

    def get(
        self,
        page_type: str | None = None,
    ) -> dict[str, Any]:
        """
        Get current Network Base configuration.

        :param page_type: Optional page type, e.g. "net_general".
        """

        data: dict[str, Any] = {}
        if page_type is not None:
            data["page_type"] = page_type

        response = self._client._request(
            "/API/NetworkConfig/NetBase/Get",
            {
                "version": "1.0",
                "data": data,
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
        Set Network Base configuration.
        """

        self._client._request(
            "/API/NetworkConfig/NetBase/Set",
            {
                "version": "1.0",
                "data": kwargs,
            },
        )
