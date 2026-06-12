from __future__ import annotations

from typing import Any


class LoginDeviceInfo:
    """
    Wrapper around OEM Login DeviceInfo response.

    Unknown fields remain accessible through
    the raw dictionary.
    """

    def __init__(
        self,
        raw: dict[str, Any],
    ) -> None:

        self.raw = raw

    @property
    def channel_num(self) -> int | None:

        return self.raw.get("channel_num")

    @property
    def analog_channel_num(self) -> int | None:

        return self.raw.get(
            "analog_channel_num"
        )

    @property
    def device_type(self) -> str | None:

        return self.raw.get(
            "device_type"
        )

    @property
    def mac_addr(self) -> str | None:

        return self.raw.get(
            "mac_addr"
        )

    @property
    def preview_num(self) -> int | None:

        return self.raw.get(
            "preview_num"
        )

    @property
    def support_face_config(self) -> bool:

        return bool(
            self.raw.get(
                "support_face_config",
                False,
            )
        )

    @property
    def support_human_vehicle_search(
        self,
    ) -> bool:

        return bool(
            self.raw.get(
                "support_human_vehicle_search",
                False,
            )
        )

    @property
    def support_heat_map(self) -> bool:

        return bool(
            self.raw.get(
                "support_heat_map",
                False,
            )
        )

    @property
    def support_ai_cc(self) -> bool:

        return bool(
            self.raw.get(
                "support_ai_cc",
                False,
            )
        )

    @property
    def support_repeat_visitor(
        self,
    ) -> bool:

        return bool(
            self.raw.get(
                "support_repeat_visitor",
                False,
            )
        )

    @property
    def support_face_attendance(
        self,
    ) -> bool:

        return bool(
            self.raw.get(
                "support_face_attendance",
                False,
            )
        )

    def __getitem__(
        self,
        key: str,
    ) -> Any:

        return self.raw[key]

    def get(
        self,
        key: str,
        default=None,
    ):

        return self.raw.get(
            key,
            default,
        )

    def __repr__(self) -> str:

        return (
            f"LoginDeviceInfo("
            f"device_type={self.device_type!r}, "
            f"channel_num={self.channel_num!r})"
        )