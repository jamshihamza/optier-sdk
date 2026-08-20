from __future__ import annotations

from typing import Any


class PreviewPTZManager:
    """
    PreviewChannel > PTZ (Live View PTZ Runtime Status, Preset Navigation, and Motorized Zoom/Focus Control) APIs.
    """

    def __init__(
        self,
        client,
    ) -> None:

        self._client = client

    def get(
        self,
        channel: str = "CH1",
        disable_ManualHumanTrace: bool = False,
        current_cruise_mode: str = "Mode_Default_Cruise",
        zoom_step: int = 5,
        focus_step: int = 5,
        **kwargs,
    ) -> dict[str, Any]:
        """
        Get live PTZ capabilities, 255 preset points, cruise modes, and slider telemetry.
        """

        payload = {
            "channel": channel,
            "disable_ManualHumanTrace": disable_ManualHumanTrace,
            "current_cruise_mode": current_cruise_mode,
            "zoom_step": zoom_step,
            "focus_step": focus_step,
        }
        payload.update(kwargs)

        response = self._client._request(
            "/API/PreviewChannel/PTZ/Get",
            {
                "version": "1.0",
                "data": payload,
            },
        )

        return response.get(
            "data",
            {},
        )

    def progress(
        self,
        channel: str = "CH1",
        **kwargs,
    ) -> dict[str, Any]:
        """
        Poll real-time PTZ positioning and motorized lens movement progress.
        """

        payload = {"channel": channel}
        payload.update(kwargs)

        response = self._client._request(
            "/API/PreviewChannel/PTZ/Control/Progress",
            {
                "version": "1.0",
                "data": payload,
            },
        )

        return response.get(
            "data",
            {},
        )

    def control(
        self,
        channel: str = "CH1",
        cmd: str | None = None,
        **kwargs,
    ) -> None:
        """
        Send PTZ movement, zoom, focus, preset, or cruise command to a camera.
        """

        payload = {"channel": channel}
        if cmd is not None:
            payload["cmd"] = cmd
        payload.update(kwargs)

        self._client._request(
            "/API/PreviewChannel/PTZ/Control",
            {
                "version": "1.0",
                "data": payload,
            },
        )
