from __future__ import annotations

from typing import Any


class LoginDeviceInfo:
    """
    Wrapper around the OEM Login DeviceInfo response.

    Frequently used fields are exposed as convenient
    properties while all OEM-specific fields remain
    available through the raw dictionary.

    This design keeps the SDK forward-compatible with
    future firmware versions without requiring a large
    dataclass containing hundreds of fields.
    """

    def __init__(
        self,
        raw: dict[str, Any],
    ) -> None:
        # Keep an internal copy so callers cannot
        # accidentally modify our state.
        self._raw: dict[str, Any] = raw.copy()

    # ------------------------------------------------------------------
    # Frequently used properties
    # ------------------------------------------------------------------

    @property
    def channel_num(self) -> int | None:
        return self._raw.get("channel_num")

    @property
    def analog_channel_num(self) -> int | None:
        return self._raw.get("analog_channel_num")

    @property
    def device_type(self) -> str | None:
        return self._raw.get("device_type")

    @property
    def mac_addr(self) -> str | None:
        return self._raw.get("mac_addr")

    @property
    def preview_num(self) -> int | None:
        return self._raw.get("preview_num")

    @property
    def support_face_config(self) -> bool:
        return bool(
            self._raw.get(
                "support_face_config",
                False,
            )
        )

    @property
    def support_human_vehicle_search(self) -> bool:
        return bool(
            self._raw.get(
                "support_human_vehicle_search",
                False,
            )
        )

    @property
    def support_heat_map(self) -> bool:
        return bool(
            self._raw.get(
                "support_heat_map",
                False,
            )
        )

    @property
    def support_ai_cc(self) -> bool:
        return bool(
            self._raw.get(
                "support_ai_cc",
                False,
            )
        )

    @property
    def support_repeat_visitor(self) -> bool:
        return bool(
            self._raw.get(
                "support_repeat_visitor",
                False,
            )
        )

    @property
    def support_face_attendance(self) -> bool:
        return bool(
            self._raw.get(
                "support_face_attendance",
                False,
            )
        )

    # ------------------------------------------------------------------
    # Raw OEM response access
    # ------------------------------------------------------------------

    @property
    def raw(self) -> dict[str, Any]:
        """
        Returns a copy of the OEM response.
        """
        return self._raw.copy()

    def to_dict(self) -> dict[str, Any]:
        """
        Returns a copy of the OEM response.
        """
        return self._raw.copy()

    # ------------------------------------------------------------------
    # Dictionary-style helpers
    # ------------------------------------------------------------------

    def get(
        self,
        key: str,
        default: Any = None,
    ) -> Any:
        return self._raw.get(key, default)

    def keys(self):
        return self._raw.keys()

    def values(self):
        return self._raw.values()

    def items(self):
        return self._raw.items()

    def __getitem__(
        self,
        key: str,
    ) -> Any:
        return self._raw[key]

    def __contains__(
        self,
        key: str,
    ) -> bool:
        return key in self._raw

    def __len__(self) -> int:
        return len(self._raw)

    # ------------------------------------------------------------------
    # Representation
    # ------------------------------------------------------------------

    def __repr__(self) -> str:
        return (
            "LoginDeviceInfo("
            f"device_type={self.device_type!r}, "
            f"channel_num={self.channel_num!r})"
        )