from __future__ import annotations


class DefoggingFanManager:
    """
    Maintenance > Defogging Fan APIs.
    """

    def __init__(self, client) -> None:
        self._client = client

    def get(self) -> dict:
        """
        Get current defogging fan configuration.
        """

        response = self._client._request(
            "/API/Maintenance/DefoggingFan/Get",
            {
                "version": "1.0",
                "data": {},
            },
        )

        return response.get("data", {})

    def range(self) -> dict:
        """
        Get supported parameter range.
        """

        response = self._client._request(
            "/API/Maintenance/DefoggingFan/Range",
            {
                "version": "1.0",
                "data": {},
            },
        )

        return response.get("data", {})

    def set(
        self,
        enabled: bool,
    ) -> None:
        """
        Enable or disable the defogging fan.
        """

        self._client._request(
            "/API/Maintenance/DefoggingFan/Set",
            {
                "version": "1.0",
                "data": {
                    "defogging_fan": enabled,
                },
            },
        )