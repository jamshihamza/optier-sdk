from __future__ import annotations

from typing import Any


class DevicePageManager:
    """
    Login > DevicePage (Remote Setting Navigation & UI Permissions) API.

    Retrieves device remote configuration menu structure and authorized functional pages
    for dynamically building VMS navigation sidebars and permission trees.
    """

    def __init__(
        self,
        client,
    ) -> None:

        self._client = client

    def get(
        self,
        **kwargs,
    ) -> dict[str, Any]:
        """
        Get hierarchical list of functional modules, menus, and configuration pages supported by the device.

        :return: Dict containing main menu list with sub-menus and pages.
        """

        response = self._client._request(
            "/API/Login/DevicePage/Get",
            {
                "version": "1.0",
                "data": {},
            },
        )

        return response.get(
            "data",
            {},
        )
