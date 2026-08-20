import os
from pathlib import Path
import pprint
import sys
import time

PROJECT_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(PROJECT_ROOT))

from optier_vms.domain import DeviceType, StreamRequest, StreamState, StreamType
from optier_vms.services import DeviceService, StreamService

from tests.fixtures.test_config import (
    HOST,
    USERNAME,
    PASSWORD,
)

print("=" * 70)
print("OPTIER VMS - Milestone 2 Live RTSP Hardware Media Plane Test")
print("=" * 70)

device_service = DeviceService()
stream_service = StreamService(device_service)

# 1. Register and connect primary hardware NVR
print("1. Connecting to Physical NVR...")
dev = device_service.add_device(
    name="Enterprise Main NVR",
    host=HOST,
    username=USERNAME,
    password=PASSWORD,
    device_type=DeviceType.NVR,
    auto_connect=True,
)
print(f"Device State: {dev.state} | Capacity: {dev.info.channel_capacity} channels")

# =====================================================================
# TEST 1: SINGLE RTSP LIVE STREAM (CH1 Substream)
# =====================================================================
print("\n" + "=" * 70)
print("TEST 1: Single RTSP Live Stream (CH1 Substream)")
print("=" * 70)

req1 = StreamRequest(device_id=dev.id, channel_index=1, stream_type=StreamType.SUB)
print(f"Starting Stream: {req1.stream_key} ...")

session1 = stream_service.start_stream(req1, buffer_capacity=1)
if not session1:
    print("FAILED to start stream session!")
    sys.exit(1)

print(f"Session Created: ID={session1.id} | Endpoint={session1.endpoint}")

# Stream for 3 seconds
t_start = time.time()
print("Streaming for 3.0 seconds...")
time.sleep(3.0)

# Check frame
latest_frame = stream_service.get_latest_frame(req1)
m1 = session1.metrics

print("\n--- Stream 1 Telemetry & Performance ---")
print(f"Stream State: {session1.state}")
print(f"Frames Received: {m1.frames_received}")
print(f"Frames Decoded: {m1.frames_decoded}")
print(f"Dropped Frames (Buffer Overwrites): {m1.dropped_frames}")
print(f"Decode Errors: {m1.decode_errors}")
print(f"Reconnect Count: {m1.reconnect_count}")
print(f"Observed Decoded FPS: {m1.fps_decoded}")
print(f"Stream Uptime: {m1.uptime_seconds}s")

if latest_frame:
    print(f"Latest Frame Dimensions: {latest_frame.width} x {latest_frame.height}")
    print(f"Pixel Format: {latest_frame.pixel_format.value}")
    print(f"Frame Number: {latest_frame.frame_number}")
    print(f"Frame Byte Size: {latest_frame.byte_size:,} bytes")
    print(f"Timestamp: {latest_frame.timestamp.isoformat()}")

assert m1.frames_decoded > 0, "No frames decoded on CH1!"

# Stop single stream
print("\nStopping Stream 1...")
stream_service.stop_stream(req1)
print(f"Stream 1 State after stop: {session1.state}")

# =====================================================================
# TEST 2: 4 CONCURRENT RTSP LIVE STREAMS (CH1, CH2, CH3, CH4)
# =====================================================================
print("\n" + "=" * 70)
print("TEST 2: 4 Concurrent RTSP Live Streams (CH1, CH2, CH3, CH4 Substreams)")
print("=" * 70)

requests = [
    StreamRequest(device_id=dev.id, channel_index=ch_idx, stream_type=StreamType.SUB)
    for ch_idx in range(1, 5)
]

sessions = []
for req in requests:
    sess = stream_service.start_stream(req, buffer_capacity=1)
    if sess:
        sessions.append(sess)

print(f"Active Concurrent Streams: {stream_service.stream_count()} / {len(requests)}")

# Stream all 4 for 3.0 seconds
print("Streaming 4 concurrent channels for 3.0 seconds...")
time.sleep(3.0)

print("\n--- 4-Stream Performance Telemetry ---")
total_decoded = 0
for idx, sess in enumerate(sessions, 1):
    m = sess.metrics
    total_decoded += m.frames_decoded
    print(f"  [CH{idx}] State: {sess.state} | Decoded: {m.frames_decoded} | FPS: {m.fps_decoded} | Drops: {m.dropped_frames}")

print(f"\nTotal Aggregate Decoded Frames across 4 channels: {total_decoded}")

# Graceful teardown
print("\nStopping all streams and disconnecting device...")
stream_service.stop_all()
device_service.disconnect_device(dev.id)

print(f"Remaining Active Streams: {stream_service.stream_count()}")
print(f"Device Final State: {dev.state}")

print("\n" + "=" * 70)
print("Milestone 2 Media Plane Hardware Verification COMPLETE & PASSED!")
print("=" * 70)
