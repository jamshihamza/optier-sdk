from __future__ import annotations

from typing import Any


class RTSPManager:
    """
    Network > RTSP (RTSP Streaming Server Configuration) APIs.
    Note: IPC-specific in OEM specification; DVR/NVR devices return not_found.
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
        Get parameter range for RTSP server configuration.
        """

        response = self._client._request(
            "/API/NetworkConfig/Rtsp/Range",
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
        Get active RTSP server configuration.
        """

        response = self._client._request(
            "/API/NetworkConfig/Rtsp/Get",
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
        Set RTSP server configuration.
        """

        self._client._request(
            "/API/NetworkConfig/Rtsp/Set",
            {
                "version": "1.0",
                "data": kwargs,
            },
        )
