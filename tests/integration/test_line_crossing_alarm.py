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
    print(f"Line Crossing Alarm Range ({label})")
    print("=" * 60)
    try:
        rng = cam.line_crossing_alarm.range(page_type=ptype)
        pprint.pprint({k: v for k, v in rng.items() if k != "channel_info"}, sort_dicts=False)
        ch_items = rng.get("channel_info", {}).get("items", {})
        print(f"Total Range channels: {len(ch_items)}")
        for ch in ["CH1", "CH2", "CH3", "CH4"]:
            if ch in ch_items:
                print(f"  {ch}: {list(ch_items[ch].get('items', {}).keys())}")
                if "rule_info" in ch_items[ch].get("items", {}):
                    print(f"    rule_info items: {list(ch_items[ch]['items']['rule_info'].get('items', {}).keys())}")
    except OptierSDKError as exc:
        print(f"Line Crossing Alarm Range ({label}) error: {exc}")

    print()
    print("=" * 60)
    print(f"Line Crossing Alarm Get ({label})")
    print("=" * 60)
    try:
        cfg = cam.line_crossing_alarm.get(page_type=ptype)
        ch_info = cfg.get("channel_info", {})
        print(f"Total returned channel entries: {len(ch_info)}")
        active_channels = {
            k: v for k, v in ch_info.items()
            if isinstance(v, dict) and "reason" not in v and v.get("status") not in ["Offline", "Nonsupport"]
        }
        offline_channels = [k for k, v in ch_info.items() if isinstance(v, dict) and v.get("status") == "Offline"]
        unsupported_channels = [k for k, v in ch_info.items() if isinstance(v, dict) and v.get("status") == "Nonsupport"]
        unconfigured_channels = [k for k, v in ch_info.items() if isinstance(v, dict) and v.get("reason") == "Not configured"]

        print(f"Configured/Active LCD channels ({len(active_channels)}): {list(active_channels.keys())}")
        print(f"Offline channels count: {len(offline_channels)}")
        print(f"Nonsupport channels count: {len(unsupported_channels)}")
        print(f"Not configured channels count: {len(unconfigured_channels)}")

        for ch, ch_data in list(active_channels.items())[:3]:
            print(f"\n--- {ch} ---")
            summary = {
                k: v for k, v in ch_data.items()
                if k not in ["voice_prompts_time", "voice_prompts_index"]
            }
            pprint.pprint(summary, sort_dicts=False)
    except OptierSDKError as exc:
        print(f"Line Crossing Alarm Get ({label}) error: {exc}")
    print()

print("Note: Set API intentionally not executed against hardware.")
print()
print("Disconnecting...")

cam.disconnect()

print("Disconnected.")
