from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from enum import Enum
import hashlib
import uuid
from typing import Any


class ForensicTagType(str, Enum):
    LICENSE_PLATE = "LICENSE_PLATE"
    PERSON_FACE = "PERSON_FACE"
    VEHICLE_BRAND = "VEHICLE_BRAND"
    VEHICLE_COLOR = "VEHICLE_COLOR"
    PERSON_GENDER = "PERSON_GENDER"
    PERSON_AGE = "PERSON_AGE"
    CUSTOM = "CUSTOM"


@dataclass
class ForensicTag:
    """
    Forensic metadata tag attached to an evidence package.
    """

    tag_type: ForensicTagType = ForensicTagType.CUSTOM
    key: str = "tag"
    value: str = ""
    confidence: float | None = None


@dataclass
class EvidenceItem:
    """
    VMS Evidence Locker Domain Model.

    Represents a sealed, packaged piece of forensic evidence (snapshot, video clip,
    or AI metadata) with cryptographic checksum validation.
    """

    id: uuid.UUID = field(default_factory=uuid.uuid4)
    device_id: uuid.UUID = field(default_factory=uuid.uuid4)
    channel_index: int = 1
    title: str = "Evidence Incident"
    notes: str = ""
    created_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
    start_time: datetime | None = None
    end_time: datetime | None = None
    snapshot_base64: str | None = None
    video_file_path: str | None = None
    forensic_tags: list[ForensicTag] = field(default_factory=list)
    sha256_checksum: str | None = None
    exported_by: str = "System"
    metadata: dict[str, Any] = field(default_factory=dict)

    def calculate_checksum(self, data_bytes: bytes) -> str:
        """
        Calculate and assign SHA-256 integrity checksum for evidence authenticity.
        """
        checksum = hashlib.sha256(data_bytes).hexdigest()
        self.sha256_checksum = checksum
        return checksum

    def add_tag(self, tag_type: ForensicTagType, key: str, value: str, confidence: float | None = None) -> None:
        """
        Append a forensic tag to this evidence item.
        """
        self.forensic_tags.append(ForensicTag(tag_type=tag_type, key=key, value=value, confidence=confidence))
