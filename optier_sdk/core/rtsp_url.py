from __future__ import annotations


class RtspUrlManager:
    """
    Preview / RTSP URL APIs.
    """

    def __init__(
        self,
        client,
    ) -> None:

        self._client = client

    def get(
        self,
        channels: list[str] | None = None,
    ) -> dict:
        """
        Get RTSP URLs.

        Examples:

            cam.rtsp_url.get()

            cam.rtsp_url.get(
                channels=["CH1"],
            )

            cam.rtsp_url.get(
                channels=["CH1", "CH2"],
            )
        """

        data: dict = {}

        if channels is not None:
            data["channel"] = channels

        response = self._client._request(
            "/API/Preview/StreamUrl/Get",
            {
                "version": "1.0",
                "data": data,
            },
        )

        return response.get(
            "data",
            {},
        )

    def get_channel(
        self,
        channel: str,
    ) -> dict | None:
        """
        Convenience helper.

        Example:

            cam.rtsp_url.get_channel("CH1")
        """

        info = self.get(
            channels=[channel],
        )

        items = info.get(
            "channel_info",
            [],
        )

        if not items:
            return None

        return items[0]