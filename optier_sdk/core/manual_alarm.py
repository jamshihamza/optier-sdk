from __future__ import annotations

from typing import Any


class ManualAlarmManager:
    """
    PreviewChannel > Manual Alarm (Live Manual Alarm Output & Siren Triggering) APIs.
    """

    def __init__(
        self,
        client,
    ) -> None:

        self._client = client

    def get(
        self,
    ) -> dict[str, Any]:
        """
        Get real-time manual alarm output states across local and IP channels.
        """

        response = self._client._request(
            "/API/PreviewChannel/ManualAlarm/Get",
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
        Trigger or clear manual alarm outputs.
        """

        self._client._request(
            "/API/PreviewChannel/ManualAlarm/Set",
            {
                "version": "1.0",
                "data": kwargs,
            },
        )
