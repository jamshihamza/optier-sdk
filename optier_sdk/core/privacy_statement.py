from __future__ import annotations

from typing import Any


class PrivacyStatementManager:
    """
    System > Privacy Statement API.

    Retrieves system privacy statement configuration and the remote statement
    file identifier displayed to client applications.
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
        Get capability parameters and range limits for System Privacy Statement.

        :return: Dict containing statement_file_name length constraints.
        """

        response = self._client._request(
            "/API/SystemConfig/Statement/Range",
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
        Retrieve the current system privacy statement configuration.

        :return: Dict containing statement_file_name (e.g. "privacy_statement").
        """

        response = self._client._request(
            "/API/SystemConfig/Statement/Get",
            {
                "version": "1.0",
                "data": {},
            },
        )

        return response.get(
            "data",
            {},
        )
