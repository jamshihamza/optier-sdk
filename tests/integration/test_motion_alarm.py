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

for ptype in ["AlarmConfig", "ChannelConfig", "AllConfig", None]:
    label = f"page_type={ptype!r}"
    print("=" * 60)
    print(f"Motion Alarm Range ({label})")
    print("=" * 60)
    try:
        rng = cam.motion_alarm.range(page_type=ptype)
        pprint.pprint({k: v for k, v in rng.items() if k != "channel_info"}, sort_dicts=False)
        print("Sample CH1/CH2 Range items:")
        ch_items = rng.get("channel_info", {}).get("items", {})
        for ch in ["CH1", "CH2", "CH3"]:
            if ch in ch_items:
                print(f"  {ch}: {list(ch_items[ch].get('items', {}).keys())}")
    except OptierSDKError as exc:
        print(f"Motion Alarm Range ({label}) error: {exc}")

    print()
    print("=" * 60)
    print(f"Motion Alarm Get ({label})")
    print("=" * 60)
    try:
        cfg = cam.motion_alarm.get(page_type=ptype)
        active_channels = {
            k: v for k, v in cfg.get("channel_info", {}).items()
            if isinstance(v, dict) and "reason" not in v and v.get("status") != "Offline"
        }
        print(f"Total returned channel entries: {len(cfg.get('channel_info', {}))}")
        print(f"Active/Configured channels found: {list(active_channels.keys())}")
        print("Active channel details:")
        for ch, ch_data in list(active_channels.items())[:3]:
            print(f"--- {ch} ---")
            # print summary without dumping large region byte strings
            summary = {
                k: v for k, v in ch_data.items()
                if k not in ["region_setting", "voice_prompts_time", "voice_prompts_index", "schedule"]
            }
            pprint.pprint(summary, sort_dicts=False)
            if "region_setting" in ch_data:
                print(f"  region_setting lines: {len(ch_data['region_setting'])}")
            if "schedule" in ch_data:
                print(f"  schedule entries: {len(ch_data['schedule'])}")
    except OptierSDKError as exc:
        print(f"Motion Alarm Get ({label}) error: {exc}")
    print()

print("Note: Set API intentionally not executed against hardware.")
print()
print("Disconnecting...")

cam.disconnect()

print("Disconnected.")
