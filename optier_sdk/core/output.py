from __future__ import annotations

from typing import Any


class OutputManager:
    """
    System > Output API.

    Manages hardware HDMI/VGA local video output display resolutions,
    multi-monitor capabilities (including 4K and 8K display modes),
    and output display settings.
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
        Get supported local display output resolutions and hardware guidelines.

        :return: Dict containing supported output resolutions for LIVE-OUT (e.g. 1080P, 4K, 8K)
                 and display port connection tips.
        """

        response = self._client._request(
            "/API/SystemConfig/Output/Range",
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
        Retrieve current active local video output display resolution.

        :return: Dict containing current LIVE-OUT output_resolution setting.
        """

        response = self._client._request(
            "/API/SystemConfig/Output/Get",
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
        output: dict[str, Any] | None = None,
        output_resolution: str | None = None,
        **kwargs,
    ) -> dict[str, Any]:
        """
        Update local video output display resolution.

        :param output: Full output configuration dict (e.g. {"LIVE-OUT": {"output_resolution": "4K(3840x2160)@60HZ"}}).
        :param output_resolution: Helper parameter to directly set the LIVE-OUT output resolution.
        :return: Device response payload.
        """

        if output is not None:
            payload = {"output": output}
        elif output_resolution is not None:
            payload = {
                "output": {
                    "LIVE-OUT": {
                        "output_resolution": output_resolution,
                    }
                }
            }
        else:
            payload = {"output": self.get().get("output", {})}

        payload.update(kwargs)

        response = self._client._request(
            "/API/SystemConfig/Output/Set",
            {
                "version": "1.0",
                "data": payload,
            },
        )

        return response.get(
            "data",
            {},
        )