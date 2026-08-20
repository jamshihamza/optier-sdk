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
print("1. AI Func Schedule Setup Range (/API/AI/Setup/AISchedule/Range)")
print("=" * 60)
try:
    range_res = cam.ai_schedule.range()
    print("AISchedule Range Keys:", list(range_res.keys()))
    print("channel_max:", range_res.get("channel_max"))
    print("support_copy:", range_res.get("support_copy"))
except OptierSDKError as exc:
    print(f"AISchedule Range error: {exc}")

print()
print("=" * 60)
print("2. AI Func Schedule Setup Get (/API/AI/Setup/AISchedule/Get)")
print("=" * 60)
try:
    get_res = cam.ai_schedule.get()
    channels = get_res.get("channel_info", {})
    print(f"AISchedule Configured Channels: {len(channels)}")
    if channels:
        first_k = list(channels.keys())[0]
        print(f"Sample {first_k} AI Func Schedule configuration:")
        pprint.pprint(channels[first_k], sort_dicts=False)
except OptierSDKError as exc:
    print(f"AISchedule Get error: {exc}")

print()
print("Disconnecting...")

cam.disconnect()

print("Disconnected.")
