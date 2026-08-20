from __future__ import annotations

from typing import Any


class RecordInfoManager:
    """
    System > Record Information API.

    Queries real-time recording runtime telemetry across all channels,
    including record state (On/Off), record switch enable state, active stream type,
    live recording resolution, frame rate (FPS), and recording bitrate.
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
        Retrieve live recording status and stream telemetry for all camera channels.

        :return: Dict containing channel_info mapping with per-channel record_state,
                 record_switch, stream_type, resolution, fps, bitrate, and channel_max.
        """

        response = self._client._request(
            "/API/SystemInfo/Record/Get",
            {
                "version": "1.0",
                "data": {},
            },
        )

        return response.get(
            "data",
            {},
        )