from pathlib import Path
import sys
import time
import unittest
import uuid
import numpy as np

PROJECT_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(PROJECT_ROOT))

from optier_vms.domain import (
    Device,
    DeviceType,
    PixelFormat,
    StreamRequest,
    StreamState,
    StreamType,
    VideoFrame,
)
from optier_vms.media.interfaces import IFrameSink, IStreamSource, IVideoDecoder
from optier_vms.services import DeviceService, StreamService


class MockStreamSource(IStreamSource):

    def __init__(self, endpoint_name: str = "mock://stream", fail_open: bool = False):
        self._endpoint = endpoint_name
        self._fail_open = fail_open
        self._opened = False
        self._frame_count = 0

    @property
    def endpoint(self) -> str:
        return self._endpoint

    @property
    def is_opened(self) -> bool:
        return self._opened

    def open(self) -> bool:
        if self._fail_open:
            return False
        self._opened = True
        return True

    def read_frame(self):
        if not self._opened:
            return False, None
        time.sleep(0.01)  # 10ms frame interval
        self._frame_count += 1
        return True, np.zeros((360, 640, 3), dtype=np.uint8)

    def close(self) -> None:
        self._opened = False


class MockSink(IFrameSink):

    def __init__(self):
        self.received_frames: list[VideoFrame] = []

    def on_frame(self, frame: VideoFrame) -> None:
        self.received_frames.append(frame)


class TestStreamService(unittest.TestCase):

    def setUp(self):
        self.device_service = DeviceService()
        self.stream_service = StreamService(self.device_service)

        # Register a mock device
        self.dev = self.device_service.add_device(
            name="Mock NVR",
            host="127.0.0.1",
            username="admin",
            password="pwd",
            device_type=DeviceType.NVR,
        )

    def tearDown(self):
        self.stream_service.stop_all()

    def test_start_and_stream_frames(self):
        req = StreamRequest(device_id=self.dev.id, channel_index=1, stream_type=StreamType.SUB)
        mock_source = MockStreamSource(endpoint_name="mock://ch1")
        sink = MockSink()

        session = self.stream_service.start_stream(
            request=req,
            sink=sink,
            custom_source=mock_source,
            buffer_capacity=2,
        )

        self.assertIsNotNone(session)
        self.assertEqual(session.channel_index, 1)

        # Wait for worker to acquire frames
        time.sleep(0.1)

        self.assertIn(session.state, (StreamState.CONNECTED, StreamState.STREAMING))
        self.assertGreater(session.metrics.frames_decoded, 0)
        self.assertGreater(len(sink.received_frames), 0)

        # Check latest frame retrieval
        latest = self.stream_service.get_latest_frame(req)
        self.assertIsNotNone(latest)
        self.assertEqual(latest.width, 640)
        self.assertEqual(latest.height, 360)

        # Stop stream
        stopped = self.stream_service.stop_stream(req)
        self.assertTrue(stopped)
        self.assertEqual(session.state, StreamState.DISCONNECTED)

    def test_stream_failure_isolation(self):
        req1 = StreamRequest(device_id=self.dev.id, channel_index=1)
        req2 = StreamRequest(device_id=self.dev.id, channel_index=2)

        good_source = MockStreamSource(endpoint_name="mock://good")
        bad_source = MockStreamSource(endpoint_name="mock://bad", fail_open=True)

        session1 = self.stream_service.start_stream(req1, custom_source=good_source)
        session2 = self.stream_service.start_stream(req2, custom_source=bad_source)

        time.sleep(0.08)

        # Stream 1 must be STREAMING / CONNECTED
        self.assertIn(session1.state, (StreamState.CONNECTED, StreamState.STREAMING))

        # Stream 2 failed and entered RECONNECTING
        self.assertEqual(session2.state, StreamState.RECONNECTING)
        self.assertGreaterEqual(session2.metrics.reconnect_count, 1)

        # Failure of Stream 2 must NOT affect Stream 1
        self.assertGreater(session1.metrics.frames_decoded, 0)


if __name__ == "__main__":
    unittest.main()
