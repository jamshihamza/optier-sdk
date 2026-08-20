from pathlib import Path
import pprint
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(PROJECT_ROOT))

from optier_sdk import Camera
from optier_sdk.exceptions import OptierSDKError

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
print("1. License Plate Detection Setup Range")
print("=" * 60)
try:
    range_res = cam.lpd.range()
    print("LPD Range Keys:", list(range_res.keys()))
    print(f"LPD channel_max: {range_res.get('channel_max')}")
except OptierSDKError as exc:
    print(f"LPD Range error: {exc}")

print()
print("=" * 60)
print("2. License Plate Detection Setup Get")
print("=" * 60)
try:
    get_res = cam.lpd.get()
    channels = get_res.get("channel_info", {})
    print(f"Total LPD configured channels: {len(channels)}")
    online_channels = {k: v for k, v in channels.items() if v.get("status") != "Offline" and v.get("status") != "Nonsupport"}
    print(f"Online LPD Channels ({len(online_channels)}):")
    for k in list(online_channels.keys())[:3]:
        ch = online_channels[k]
        print(f"  - {k}: switch={ch.get('switch')} | sensitivity={ch.get('sensitivity')} | snap_mode={ch.get('snap_mode')} | detection_type={ch.get('detection_type')}")
except OptierSDKError as exc:
    print(f"LPD Get error: {exc}")

print()
print("Disconnecting...")

cam.disconnect()

print("Disconnected.")
