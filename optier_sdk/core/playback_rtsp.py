from __future__ import annotations

from urllib.parse import urlencode


class PlaybackRtspManager:
    """
    Playback RTSP URL builder.
    """

    def __init__(
        self,
        client,
    ) -> None:

        self._client = client

    def url(
        self,
        *,
        channel: int,
        starttime: str,
        endtime: str,
        subtype: int = 0,
        localtime: bool | None = None,
    ) -> str:
        """
        Build playback RTSP URL.

        Example:

            rtsp://ip:554/rtsp/playback?...
        """

        params = {
            "channel": channel,
            "subtype": subtype,
            "starttime": starttime,
            "endtime": endtime,
        }

        #
        # Backend NVR/DVR only.
        #

        if localtime is not None:
            params["localtime"] = (
                "true"
                if localtime
                else "false"
            )

        query = urlencode(params)

        return (
            f"rtsp://"
            f"{self._client.host}"
            f":554"
            f"/rtsp/playback?"
            f"{query}"
        )