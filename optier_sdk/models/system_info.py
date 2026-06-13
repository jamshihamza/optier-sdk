from __future__ import annotations

from typing import Any


class SystemInfo:
    """
    Wrapper around OEM SystemInfo response.

    Frequently used fields are exposed as
    convenient properties while all OEM
    fields remain available.
    """

    def __init__(
        self,
        raw: dict[str, Any],
    ) -> None:

        self._raw = raw.copy()

    @classmethod
    def from_dict(
        cls,
        data: dict[str, Any],
    ) -> "SystemInfo":

        return cls(data)

    @property
    def device_id(self) -> str | None:

        return self._raw.get("device_id")

    @property
    def device_name(self) -> str | None:

        return self._raw.get("device_name")

    @property
    def device_type(self) -> str | None:

        return self._raw.get("device_type")

    @property
    def hardware_version(self) -> str | None:

        return self._raw.get(
            "hardware_version"
        )

    @property
    def software_version(self) -> str | None:

        return self._raw.get(
            "software_version"
        )

    @property
    def build_time(self) -> str | None:

        return self._raw.get(
            "build_time"
        )

    @property
    def ie_client_version(self) -> str | None:

        return self._raw.get(
            "ie_client_version"
        )

    @property
    def raw(self) -> dict[str, Any]:

        return self._raw.copy()

    def __getitem__(
        self,
        key: str,
    ) -> Any:

        return self._raw[key]

    def get(
        self,
        key: str,
        default: Any = None,
    ) -> Any:

        return self._raw.get(
            key,
            default,
        )

    def __repr__(self) -> str:

        return (
            "SystemInfo("
            f"device_name={self.device_name!r}, "
            f"device_type={self.device_type!r})"
        )