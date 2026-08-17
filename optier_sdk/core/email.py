from __future__ import annotations

from typing import Any


class EmailManager:
    """
    Network > Email (SMTP Notification & Alarm Email Dispatch) APIs.
    """

    def __init__(
        self,
        client,
    ) -> None:

        self._client = client

    def range(
        self,
    ) -> dict[str, Any]:
        """
        Get parameter range for Email configuration.
        """

        response = self._client._request(
            "/API/NetworkConfig/Email/Range",
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
    ) -> dict[str, Any]:
        """
        Get active Email configuration.
        """

        response = self._client._request(
            "/API/NetworkConfig/Email/Get",
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
        Set Email configuration.
        """

        self._client._request(
            "/API/NetworkConfig/Email/Set",
            {
                "version": "1.0",
                "data": kwargs,
            },
        )

    def test(
        self,
        **kwargs,
    ) -> dict[str, Any]:
        """
        Test Email configuration.
        """

        response = self._client._request(
            "/API/NetworkConfig/Email/Test",
            {
                "version": "1.0",
                "data": kwargs,
            },
        )

        return response.get(
            "data",
            {},
        )
