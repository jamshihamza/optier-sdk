from __future__ import annotations

from typing import Any


class FTPManager:
    """
    Network > FTP (FTP Server, Picture/Video Upload & Connectivity Test) APIs.
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
        Get parameter range for FTP configuration.
        """

        response = self._client._request(
            "/API/NetworkConfig/Ftp/Range",
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
        Get active FTP configuration.
        """

        response = self._client._request(
            "/API/NetworkConfig/Ftp/Get",
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
        Set FTP configuration.
        """

        self._client._request(
            "/API/NetworkConfig/Ftp/Set",
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
        Test FTP connection.
        """

        response = self._client._request(
            "/API/NetworkConfig/Ftp/Test",
            {
                "version": "1.0",
                "data": kwargs,
            },
        )

        return response.get(
            "data",
            {},
        )
