from pathlib import Path
import sys
import unittest
import uuid
import numpy as np

PROJECT_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(PROJECT_ROOT))

from optier_vms.domain import (
    PixelFormat,
    StreamMetrics,
    StreamRequest,
    StreamSession,
    StreamState,
    StreamType,
    VideoFrame,
)


class TestMediaDomain(unittest.TestCase):

    def test_stream_request_key(self):
        dev_id = uuid.uuid4()
        req = StreamRequest(device_id=dev_id, channel_index=5, stream_type=StreamType.SUB)
        self.assertEqual(req.stream_key, f"{dev_id}:CH5:sub")

    def test_video_frame_properties(self):
        fake_data = np.zeros((720, 1280, 3), dtype=np.uint8)
        frame = VideoFrame(
            width=1280,
            height=720,
            pixel_format=PixelFormat.BGR24,
            frame_number=42,
            data=fake_data,
        )
        self.assertEqual(frame.width, 1280)
        self.assertEqual(frame.height, 720)
        self.assertEqual(frame.pixel_format, PixelFormat.BGR24)
        self.assertEqual(frame.frame_number, 42)
        self.assertEqual(frame.byte_size, 1280 * 720 * 3)
        self.assertAlmostEqual(frame.aspect_ratio, 16 / 9, places=2)

    def test_stream_metrics_tracking(self):
        metrics = StreamMetrics()
        self.assertEqual(metrics.frames_received, 0)
        self.assertEqual(metrics.frames_decoded, 0)

        metrics.record_received()
        metrics.record_received()
        metrics.record_decoded()
        metrics.record_drop(3)
        metrics.record_decode_error()
        metrics.record_reconnect()

        self.assertEqual(metrics.frames_received, 2)
        self.assertEqual(metrics.frames_decoded, 1)
        self.assertEqual(metrics.dropped_frames, 3)
        self.assertEqual(metrics.decode_errors, 1)
        self.assertEqual(metrics.reconnect_count, 1)
        self.assertIsNotNone(metrics.last_frame_timestamp)

    def test_stream_session_state(self):
        dev_id = uuid.uuid4()
        session = StreamSession(
            device_id=dev_id,
            channel_index=1,
            stream_type=StreamType.MAIN,
            endpoint="rtsp://***:***@192.168.1.100:80/live",
            state=StreamState.STREAMING,
        )
        self.assertTrue(session.is_active)
        session.state = StreamState.DISCONNECTED
        self.assertFalse(session.is_active)


if __name__ == "__main__":
    unittest.main()
