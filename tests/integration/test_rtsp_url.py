from pathlib import Path
import pprint
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(PROJECT_ROOT))

from optier_sdk import Camera

from tests.fixtures.test_config import (
    HOST,
    USERNAME,
    PASSWORD,
)

print("=" * 60)
print("Connecting...")
print("=" * 60)

cam = Camera(
    host=HOST,
    username=USERNAME,
    password=PASSWORD,
)

cam.connect()

print("Connected.")
print()

print("=" * 60)
print("RTSP URLs (All Channels)")
print("=" * 60)

info = cam.rtsp_url.get()
print()
print("=" * 60)
print("CH1")
print("=" * 60)

ch1 = cam.rtsp_url.get_channel("CH1")

pprint.pprint(
    ch1,
    sort_dicts=False,
)

pprint.pprint(
    info,
    sort_dicts=False,
)

print()

print("=" * 60)
print("RTSP URL (CH1 only)")
print("=" * 60)

info = cam.rtsp_url.get(
    channels=["CH1"],
)

pprint.pprint(
    info,
    sort_dicts=False,
)

print()
print("Disconnecting...")

cam.disconnect()

print("Disconnected.")