from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass(slots=True)
class ChannelInfo:
    """
    Represents a single channel returned by
    Login/ChannelInfo/Get.
    """

    channel: str

    channel_name: str

    channel_alias: str

    connect_status: str

    videoloss: bool

    ability: list[str] = field(default_factory=list)

    intelligent_ability: list[str] = field(default_factory=list)

    alarm_in_num: int = 0

    alarm_out_num: int = 0

    show_ptz_setting: bool = False

    talk_audio_ability: list[str] = field(default_factory=list)

    wireless_ipc_type: int | None = None

    extra: dict[str, Any] = field(default_factory=dict)

    @classmethod
    def from_dict(
        cls,
        data: dict[str, Any],
    ) -> "ChannelInfo":
        return cls(
            channel=data.get("channel", ""),
            channel_name=data.get(
                "channel_name",
                "",
            ),
            channel_alias=data.get(
                "channel_alias",
                "",
            ),
            connect_status=data.get(
                "connect_status",
                "",
            ),
            videoloss=bool(
                data.get(
                    "videoloss",
                    False,
                )
            ),
            ability=list(
                data.get("ability") or []
            ),
            intelligent_ability=list(
                data.get(
                    "intelligent_ability"
                )
                or []
            ),
            alarm_in_num=data.get(
                "alarm_in_num",
                0,
            ),
            alarm_out_num=data.get(
                "alarm_out_num",
                0,
            ),
            show_ptz_setting=bool(
                data.get(
                    "show_ptz_setting",
                    False,
                )
            ),
            talk_audio_ability=list(
                data.get(
                    "talk_audio_ability"
                )
                or []
            ),
            wireless_ipc_type=data.get(
                "wireless_ipc_type",
            ),
            extra=data.copy(),
        )