from __future__ import annotations

from ..models.system_info import SystemInfo


class SystemInfoManager:
    """
    System Information APIs.
    """

    def __init__(
        self,
        client,
    ) -> None:

        self._client = client

    def get(self) -> SystemInfo:
        """
        Get System Information.
        """

        response = self._client._request(
            "/API/SystemInfo/Base/Get",
            {
                "version": "1.0",
                "data": {},
            },
        )

        return SystemInfo.from_dict(
            response.get(
                "data",
                {},
            )
        )