from __future__ import annotations

from typing import Any


class SNMPManager:
    """
    Network > SNMP (Simple Network Management Protocol & Trap Dispatch) APIs.
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
        Get parameter range for SNMP configuration.
        """

        response = self._client._request(
            "/API/NetworkConfig/Snmp/Range",
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
        Get active SNMP configuration.
        """

        response = self._client._request(
            "/API/NetworkConfig/Snmp/Get",
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
        Set SNMP configuration.
        """

        self._client._request(
            "/API/NetworkConfig/Snmp/Set",
            {
                "version": "1.0",
                "data": kwargs,
            },
        )
