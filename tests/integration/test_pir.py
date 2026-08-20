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
print("1. PIR Alarm Range (/API/AlarmConfig/PIR/Range)")
print("=" * 60)
try:
    range_res = cam.pir.range()
    print("PIR Range Keys:", list(range_res.keys()))
    print("channel_max:", range_res.get("channel_max"))
except OptierSDKError as exc:
    print(f"PIR Range error: {exc}")

print()
print("=" * 60)
print("2. PIR Alarm Get (/API/AlarmConfig/PIR/Get)")
print("=" * 60)
try:
    get_res = cam.pir.get()
    channels = get_res.get("channel_info", {})
    print(f"PIR Configured Channels: {len(channels)}")
except OptierSDKError as exc:
    print(f"PIR Get error: {exc}")

print()
print("Disconnecting...")

cam.disconnect()

print("Disconnected.")
