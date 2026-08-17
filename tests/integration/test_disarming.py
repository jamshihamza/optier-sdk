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
print("Disarming Range")
print("=" * 60)
try:
    rng = cam.disarming.range()
    summary = {k: v for k, v in rng.items() if k != "channel_info"}
    pprint.pprint(summary, sort_dicts=False)
    ch_info = rng.get("channel_info", {})
    print(f"Total Range channel schedule entries: {len(ch_info.get('items', {}))}")
except OptierSDKError as exc:
    print(f"Disarming Range error: {exc}")

print()
print("=" * 60)
print("Disarming Get")
print("=" * 60)
try:
    cfg = cam.disarming.get()
    summary = {k: v for k, v in cfg.items() if k != "channel_info"}
    pprint.pprint(summary, sort_dicts=False)
    ch_info = cfg.get("channel_info", {})
    print(f"Total Disarming configured channel schedules: {len(ch_info)}")
    for ch in list(ch_info.keys())[:3]:
        print(f"\n--- {ch} Schedule ---")
        sched = ch_info[ch].get("disarming_schedule", [])
        if sched:
            print(f"  schedule_type: {sched[0].get('schedule_type')}")
            week = sched[0].get("week", [])
            print(f"  days configured: {[d.get('day') for d in week]}")
            if week:
                print(f"  sample day ({week[0].get('day')}) intervals count: {len(week[0].get('time', []))}")
except OptierSDKError as exc:
    print(f"Disarming Get error: {exc}")

print()
print("Note: Set API intentionally not executed against hardware.")
print()
print("Disconnecting...")

cam.disconnect()

print("Disconnected.")
