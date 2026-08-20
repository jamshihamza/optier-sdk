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
print("1. Linkage Schedule Range (FloodLight / Siren)")
print("=" * 60)
try:
    range_res = cam.linkage_schedule.range(page_type="FloodLight")
    print("Linkage Schedule FloodLight Range Keys:", list(range_res.keys()))
except OptierSDKError as exc:
    print(f"LinkageSchedule Range error: {exc}")

print()
print("=" * 60)
print("2. Linkage Schedule Get (FloodLight / Siren)")
print("=" * 60)
try:
    get_res = cam.linkage_schedule.get(page_type="FloodLight")
    channels = get_res.get("channel_info", {})
    print(f"Linkage Schedule FloodLight Channels: {len(channels)}")
except OptierSDKError as exc:
    print(f"LinkageSchedule Get error: {exc}")

print()
print("Disconnecting...")

cam.disconnect()

print("Disconnected.")
