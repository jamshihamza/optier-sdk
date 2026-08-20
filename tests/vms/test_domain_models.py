from pathlib import Path
import sys
import unittest
import uuid

PROJECT_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(PROJECT_ROOT))

from optier_vms.domain import (
    AICapability,
    CameraChannel,
    ChannelPermission,
    ConnectionState,
    Device,
    DeviceInfo,
    DeviceType,
    EvidenceItem,
    EventSeverity,
    EventType,
    ForensicTagType,
    Operation,
    Role,
    VMSEvent,
    VMSUser,
)


class TestVMSDomainModels(unittest.TestCase):

    def test_device_and_channel_creation(self):
        dev = Device(
            name="Main NVR",
            host="192.168.1.100",
            port=80,
            device_type=DeviceType.NVR,
            info=DeviceInfo(model="OPTIER-NVR32", channel_capacity=32),
        )
        self.assertEqual(dev.state, ConnectionState.DISCONNECTED)
        self.assertEqual(len(dev.channels), 0)

        for i in range(1, 33):
            ch = CameraChannel(
                device_id=dev.id,
                channel_index=i,
                name=f"Camera {i:02d}",
                online=True,
            )
            ch.ai_capabilities.add(AICapability.FACE_DETECTION)
            ch.ai_capabilities.add(AICapability.LICENSE_PLATE_DETECTION)
            dev.add_channel(ch)

        self.assertEqual(len(dev.channels), 32)
        self.assertEqual(dev.online_channel_count, 32)

        ch5 = dev.get_channel(5)
        self.assertIsNotNone(ch5)
        self.assertEqual(ch5.channel_key, "CH5")
        self.assertTrue(ch5.supports_ai(AICapability.FACE_DETECTION))
        self.assertFalse(ch5.supports_ai(AICapability.SOUND_DETECTION))

    def test_vms_event_lifecycle(self):
        event = VMSEvent(
            device_id=uuid.uuid4(),
            channel_index=1,
            event_type=EventType.FACE_MATCH,
            severity=EventSeverity.HIGH,
            description="VIP Enrolled Person Identified",
            metadata={"person_name": "Alice", "confidence": 0.98},
        )
        self.assertFalse(event.acknowledged)
        event.acknowledge()
        self.assertTrue(event.acknowledged)
        self.assertEqual(event.event_type, EventType.FACE_MATCH)

    def test_evidence_item_integrity(self):
        evidence = EvidenceItem(
            channel_index=2,
            title="Gate Intrusion Incident",
            notes="Unauthorized vehicle entry attempt",
        )
        fake_video_payload = b"\x00\x00\x00\x01\x67H.264_STREAM_TEST_PACKET"
        checksum = evidence.calculate_checksum(fake_video_payload)
        self.assertIsNotNone(checksum)
        self.assertEqual(len(checksum), 64)

        evidence.add_tag(ForensicTagType.LICENSE_PLATE, "plate_number", "KA01AB1234", 0.96)
        self.assertEqual(len(evidence.forensic_tags), 1)
        self.assertEqual(evidence.forensic_tags[0].value, "KA01AB1234")

    def test_vms_user_rbac_permissions(self):
        # 1. Admin has access to everything
        admin_user = VMSUser(username="superadmin", role=Role.ADMIN)
        self.assertTrue(admin_user.has_permission(Operation.DEVICE_CONFIG))
        self.assertTrue(admin_user.has_permission(Operation.PLAYBACK, channel_index=1))
        self.assertTrue(admin_user.has_permission(Operation.PTZ_CONTROL, channel_index=12))

        # 2. Operator with restricted per-channel permissions
        op_user = VMSUser(
            username="guard1",
            role=Role.OPERATOR,
            global_operations={Operation.LIVE_VIEW},
        )
        op_user.channel_permissions[1] = ChannelPermission(
            channel_index=1,
            allowed_operations={Operation.PTZ_CONTROL, Operation.MANUAL_RECORD},
        )

        # Global live view allowed on all channels
        self.assertTrue(op_user.has_permission(Operation.LIVE_VIEW))
        self.assertTrue(op_user.has_permission(Operation.LIVE_VIEW, channel_index=5))

        # PTZ only allowed on CH1
        self.assertTrue(op_user.has_permission(Operation.PTZ_CONTROL, channel_index=1))
        self.assertFalse(op_user.has_permission(Operation.PTZ_CONTROL, channel_index=2))

        # Device config forbidden for operator
        self.assertFalse(op_user.has_permission(Operation.DEVICE_CONFIG))

        # Disabled user has zero permissions
        op_user.enabled = False
        self.assertFalse(op_user.has_permission(Operation.LIVE_VIEW))


if __name__ == "__main__":
    unittest.main()
