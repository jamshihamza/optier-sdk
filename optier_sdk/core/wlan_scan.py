from __future__ import annotations

from typing import Any


class WLANScanManager:
    """
    Network > WLAN Scan / Wi-Fi Client & AP Management APIs.
    """

    def __init__(
        self,
        client,
    ) -> None:

        self._client = client

    def scan(
        self,
    ) -> dict[str, Any]:
        """
        Scan for nearby wireless networks.
        """

        response = self._client._request(
            "/API/NetworkConfig/ScanWlan/Scan",
            {
                "version": "1.0",
                "data": {},
            },
        )

        return response.get(
            "data",
            {},
        )

    def join(
        self,
        **kwargs,
    ) -> None:
        """
        Join a wireless Wi-Fi network.
        """

        self._client._request(
            "/API/NetworkConfig/ScanWlan/Join",
            {
                "version": "1.0",
                "data": kwargs,
            },
        )

    def set_wifi_sta_param(
        self,
        **kwargs,
    ) -> None:
        """
        Set Wi-Fi station parameters.
        """

        self._client._request(
            "/API/APNetworkCfg/WifiStaParam/Set",
            {
                "version": "1.0",
                "data": kwargs,
            },
        )
