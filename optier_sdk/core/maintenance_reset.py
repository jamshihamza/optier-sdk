from __future__ import annotations

from typing import Any


class MaintenanceResetManager:
    """
    Maintenance > Reset (Load Default Parameter) API.

    Controls system-wide factory default parameter restoration by functional
    category (channel, record, alarm, network, storage, system) with secondary
    authentication verification.
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
        Get capability parameters and category flags for System Reset (Load Default).

        :return: Dict containing category support flags (channel, record, alarm,
                 network, storage, system, secondary_authentication limits).
        """

        response = self._client._request(
            "/API/Maintenance/Reset/Range",
            {
                "version": "1.0",
                "data": {},
            },
        )

        return response.get(
            "data",
            {},
        )

    def reset_defaults(
        self,
        channel: bool | None = None,
        record: bool | None = None,
        alarm: bool | None = None,
        network: bool | None = None,
        storage: bool | None = None,
        system: bool | None = None,
        base_secondary_authentication: dict[str, Any] | None = None,
        **kwargs,
    ) -> dict[str, Any]:
        """
        Execute system parameter reset for selected configuration subsystems.

        :param channel: Reset channel-related parameters.
        :param record: Reset recording and storage schedule parameters.
        :param alarm: Reset alarm and event detection parameters.
        :param network: Reset network configuration parameters.
        :param storage: Reset storage-related configuration parameters.
        :param system: Reset general system parameters.
        :param base_secondary_authentication: Optional secondary authentication cipher payload.
        :return: Device response payload.
        """

        payload: dict[str, Any] = {}

        if channel is not None:
            payload["channel"] = channel
        if record is not None:
            payload["record"] = record
        if alarm is not None:
            payload["alarm"] = alarm
        if network is not None:
            payload["network"] = network
        if storage is not None:
            payload["storage"] = storage
        if system is not None:
            payload["system"] = system
        if base_secondary_authentication is not None:
            payload["base_secondary_authentication"] = base_secondary_authentication

        payload.update(kwargs)

        response = self._client._request(
            "/API/Maintenance/Reset/Set",
            {
                "version": "1.0",
                "data": payload,
            },
        )

        return response.get(
            "data",
            {},
        )
