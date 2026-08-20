from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
import uuid


class Role(str, Enum):
    ADMIN = "ADMIN"
    SUPERVISOR = "SUPERVISOR"
    OPERATOR = "OPERATOR"
    INVESTIGATOR = "INVESTIGATOR"
    GUEST = "GUEST"


class Operation(str, Enum):
    LIVE_VIEW = "LIVE_VIEW"
    PLAYBACK = "PLAYBACK"
    PTZ_CONTROL = "PTZ_CONTROL"
    MANUAL_RECORD = "MANUAL_RECORD"
    FORENSIC_SEARCH = "FORENSIC_SEARCH"
    EVIDENCE_EXPORT = "EVIDENCE_EXPORT"
    ALARM_CONTROL = "ALARM_CONTROL"
    DEVICE_CONFIG = "DEVICE_CONFIG"
    USER_MANAGEMENT = "USER_MANAGEMENT"


@dataclass
class ChannelPermission:
    """
    Per-channel permission granting allowed VMS operations.
    """

    channel_index: int
    allowed_operations: set[Operation] = field(default_factory=set)

    def can_perform(self, operation: Operation) -> bool:
        return operation in self.allowed_operations


@dataclass
class VMSUser:
    """
    VMS User Account and RBAC Profile Model.
    """

    id: uuid.UUID = field(default_factory=uuid.uuid4)
    username: str = "operator"
    role: Role = Role.OPERATOR
    enabled: bool = True
    global_operations: set[Operation] = field(default_factory=set)
    channel_permissions: dict[int, ChannelPermission] = field(default_factory=dict)

    def has_permission(self, operation: Operation, channel_index: int | None = None) -> bool:
        """
        Evaluate whether the user is authorized to perform an operation globally or on a specific channel.
        """
        if not self.enabled:
            return False

        if self.role == Role.ADMIN:
            return True

        if operation in self.global_operations:
            return True

        if channel_index is not None and channel_index in self.channel_permissions:
            return self.channel_permissions[channel_index].can_perform(operation)

        return False
