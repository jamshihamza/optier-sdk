from __future__ import annotations


class AutoRebootManager:
    """
    Maintenance Auto Reboot APIs.
    """

    def __init__(
        self,
        client,
    ) -> None:

        self._client = client

    def range(self) -> dict:
        """
        Get supported Auto Reboot parameter range.
        """

        response = self._client._request(
            "/API/Maintenance/AutoReboot/Range",
            {
                "version": "1.0",
                "data": {},
            },
        )

        return response.get(
            "data",
            {},
        )

    def get(self) -> dict:
        """
        Get current Auto Reboot configuration.
        """

        response = self._client._request(
            "/API/Maintenance/AutoReboot/Get",
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
        Set Auto Reboot configuration.
        """

        self._client._request(
            "/API/Maintenance/AutoReboot/Set",
            {
                "version": "1.0",
                "data": kwargs,
            },
        )
