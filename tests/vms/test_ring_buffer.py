from pathlib import Path
import sys
import threading
import time
import unittest

PROJECT_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(PROJECT_ROOT))

from optier_vms.domain.media import PixelFormat, VideoFrame
from optier_vms.media.ring_buffer import BoundedFrameBuffer


def create_dummy_frame(frame_num: int) -> VideoFrame:
    return VideoFrame(
        width=640,
        height=360,
        pixel_format=PixelFormat.BGR24,
        frame_number=frame_num,
        data=b"\x00" * 100,
    )


class TestRingBuffer(unittest.TestCase):

    def test_buffer_initial_state(self):
        buf = BoundedFrameBuffer[VideoFrame](maxsize=1)
        self.assertEqual(buf.capacity, 1)
        self.assertEqual(buf.size, 0)
        self.assertTrue(buf.is_empty)
        self.assertFalse(buf.is_closed)
        self.assertEqual(buf.dropped_count, 0)

    def test_single_producer_single_consumer(self):
        buf = BoundedFrameBuffer[VideoFrame](maxsize=2)
        f1 = create_dummy_frame(1)
        f2 = create_dummy_frame(2)

        self.assertTrue(buf.push(f1))
        self.assertTrue(buf.push(f2))
        self.assertEqual(buf.size, 2)
        self.assertEqual(buf.dropped_count, 0)

        out1 = buf.get(timeout=0.1)
        self.assertIsNotNone(out1)
        self.assertEqual(out1.frame_number, 1)

        out2 = buf.get(timeout=0.1)
        self.assertIsNotNone(out2)
        self.assertEqual(out2.frame_number, 2)

        self.assertEqual(buf.size, 0)

    def test_buffer_overwrite_and_drop_tracking(self):
        # Buffer capacity = 1 (Latest Frame Buffer)
        buf = BoundedFrameBuffer[VideoFrame](maxsize=1)

        f1 = create_dummy_frame(1)
        f2 = create_dummy_frame(2)
        f3 = create_dummy_frame(3)

        buf.push(f1)
        self.assertEqual(buf.size, 1)
        self.assertEqual(buf.dropped_count, 0)

        # Push f2: overwrites f1
        buf.push(f2)
        self.assertEqual(buf.size, 1)
        self.assertEqual(buf.dropped_count, 1)

        # Push f3: overwrites f2
        buf.push(f3)
        self.assertEqual(buf.size, 1)
        self.assertEqual(buf.dropped_count, 2)

        # Consumer should get latest frame (f3)
        latest = buf.get(timeout=0.1)
        self.assertIsNotNone(latest)
        self.assertEqual(latest.frame_number, 3)
        self.assertEqual(buf.size, 0)

    def test_peek_operation(self):
        buf = BoundedFrameBuffer[VideoFrame](maxsize=2)
        self.assertIsNone(buf.peek())

        f1 = create_dummy_frame(10)
        buf.push(f1)

        peeked = buf.peek()
        self.assertIsNotNone(peeked)
        self.assertEqual(peeked.frame_number, 10)
        self.assertEqual(buf.size, 1)  # Peek does not consume

    def test_consumer_timeout_on_empty(self):
        buf = BoundedFrameBuffer[VideoFrame](maxsize=1)
        start = time.time()
        res = buf.get(timeout=0.05)
        elapsed = time.time() - start
        self.assertIsNone(res)
        self.assertGreaterEqual(elapsed, 0.04)

    def test_close_unblocks_waiting_consumer(self):
        buf = BoundedFrameBuffer[VideoFrame](maxsize=1)
        result_holder = []

        def consumer():
            f = buf.get(timeout=2.0)
            result_holder.append(f)

        th = threading.Thread(target=consumer)
        th.start()
        time.sleep(0.05)
        buf.close()
        th.join(timeout=1.0)

        self.assertEqual(len(result_holder), 1)
        self.assertIsNone(result_holder[0])
        self.assertTrue(buf.is_closed)

    def test_concurrent_producer_consumer(self):
        buf = BoundedFrameBuffer[VideoFrame](maxsize=1)
        received_frames = []
        stop_flag = threading.Event()

        def producer():
            idx = 0
            while not stop_flag.is_set():
                buf.push(create_dummy_frame(idx))
                idx += 1
                time.sleep(0.001)

        def consumer():
            while not stop_flag.is_set():
                f = buf.get(timeout=0.01)
                if f is not None:
                    received_frames.append(f.frame_number)

        p_th = threading.Thread(target=producer)
        c_th = threading.Thread(target=consumer)

        p_th.start()
        c_th.start()

        time.sleep(0.1)
        stop_flag.set()
        buf.close()

        p_th.join()
        c_th.join()

        self.assertGreater(len(received_frames), 0)
        self.assertGreater(buf.pushed_count, 0)


if __name__ == "__main__":
    unittest.main()
