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

for ch_filter in [None, ["CH1", "CH3"]]:
    label = f"channels={ch_filter!r}"
    print("=" * 60)
    print(f"PTZ Linkage Range ({label})")
    print("=" * 60)
    try:
        rng = cam.ptz_linkage.range(channels=ch_filter)
        metadata = {k: v for k, v in rng.items() if k not in ["channel_info", "ptz_info"]}
        pprint.pprint(metadata, sort_dicts=False)
        ptz_info = rng.get("ptz_info", {})
        if isinstance(ptz_info, dict):
            print(f"PTZ info template type: {ptz_info.get('type')}, max_size: {ptz_info.get('max_size')}")
        ch_info = rng.get("channel_info", {})
        if isinstance(ch_info, dict):
            items = ch_info.get("items", {})
            print(f"Total Range channels: {len(items)}")
    except OptierSDKError as exc:
        print(f"PTZ Linkage Range ({label}) error: {exc}")

    print()
    print("=" * 60)
    print(f"PTZ Linkage Get ({label})")
    print("=" * 60)
    try:
        cfg = cam.ptz_linkage.get(channels=ch_filter)
        ch_info = cfg.get("channel_info", {})
        print(f"Total returned channels: {len(ch_info)}")
        configured_channels = {
            k: v for k, v in ch_info.items()
            if isinstance(v, dict) and "reason" not in v
        }
        unconfigured_channels = [
            k for k, v in ch_info.items()
            if isinstance(v, dict) and v.get("reason") == "Not configured"
        ]
        print(f"Configured PTZ Linkage channels ({len(configured_channels)}): {list(configured_channels.keys())}")
        if unconfigured_channels:
            print(f"Unconfigured channels count: {len(unconfigured_channels)}")

        for ch, ch_data in list(configured_channels.items())[:2]:
            print(f"\n--- {ch} PTZ Linkage ---")
            pprint.pprint({
                "switch": ch_data.get("switch"),
                "copy_ch": ch_data.get("copy_ch"),
                "ptz_info": ch_data.get("ptz_info"),
                "all_alarm_triggers": list(ch_data.get("all_alarm", {}).keys()),
            }, sort_dicts=False)
    except OptierSDKError as exc:
        print(f"PTZ Linkage Get ({label}) error: {exc}")
    print()

print("Note: Set API intentionally not executed against hardware.")
print()
print("Disconnecting...")

cam.disconnect()

print("Disconnected.")
