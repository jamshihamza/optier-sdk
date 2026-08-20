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
print("1. Combination Alarm Range")
print("=" * 60)
try:
    range_res = cam.combination_alarm.range()
    print("Combination Alarm Range Keys:", list(range_res.keys()))
    print(f"channel_max: {range_res.get('channel_max')} | support_copy: {range_res.get('support_copy')}")
except OptierSDKError as exc:
    print(f"CombinationAlarm Range error: {exc}")

print()
print("=" * 60)
print("2. Combination Alarm Get")
print("=" * 60)
try:
    get_res = cam.combination_alarm.get()
    channels = get_res.get("channel_info", {})
    print(f"Total Combination configured channels: {len(channels)}")
    online_channels = {k: v for k, v in channels.items() if v.get("status") != "Offline" and v.get("status") != "Nonsupport"}
    print(f"Online Combination Channels ({len(online_channels)}):")
    for k in list(online_channels.keys())[:3]:
        ch = online_channels[k]
        print(f"  - {k}: enable_alarm={ch.get('enable_alarm')} | send_email={ch.get('send_email')} | buzzer={ch.get('buzzer')} | record_enable={ch.get('record_enable')}")
except OptierSDKError as exc:
    print(f"CombinationAlarm Get error: {exc}")

print()
print("Disconnecting...")

cam.disconnect()

print("Disconnected.")
