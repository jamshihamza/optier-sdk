from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass(slots=True)
class LoginDeviceInfo:
    """
    Login DeviceInfo model.
    """

    channel_num: int | None = None

    analog_channel_num: int | None = None

    device_type: str | None = None

    mac_addr: str | None = None

    preview_num: int | None = None

    support_face_config: bool = False

    support_human_vehicle_search: bool = False

    support_heat_map: bool = False

    support_ai_cc: bool = False

    support_repeat_visitor: bool = False

    support_face_attendance: bool = False

    extra: dict[str, Any] = field(default_factory=dict)

    @classmethod
    def from_dict(
        cls,
        data: dict[str, Any],
    ) -> "LoginDeviceInfo":
        return cls(
            channel_num=data.get("channel_num"),
            analog_channel_num=data.get("analog_channel_num"),
            device_type=data.get("device_type"),
            mac_addr=data.get("mac_addr"),
            preview_num=data.get("preview_num"),
            support_face_config=data.get(
                "support_face_config",
                False,
            ),
            support_human_vehicle_search=data.get(
                "support_human_vehicle_search",
                False,
            ),
            support_heat_map=data.get(
                "support_heat_map",
                False,
            ),
            support_ai_cc=data.get(
                "support_ai_cc",
                False,
            ),
            support_repeat_visitor=data.get(
                "support_repeat_visitor",
                False,
            ),
            support_face_attendance=data.get(
                "support_face_attendance",
                False,
            ),
            extra=data.copy(),
        )