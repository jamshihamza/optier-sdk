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

for alarm_in_val in [None, ["Local<-1", "Local<-2"]]:
    label = f"alarm_in={alarm_in_val!r}"
    print("=" * 60)
    print(f"IO Alarm Range ({label})")
    print("=" * 60)
    try:
        rng = cam.io_alarm.range(alarm_in=alarm_in_val)
        pprint.pprint({k: v for k, v in rng.items() if k != "channel_info"}, sort_dicts=False)
        ch_items = rng.get("channel_info", {}).get("items", {})
        print(f"Total Range alarm input ports: {len(ch_items)}")
        for ch in list(ch_items.keys())[:5]:
            print(f"  {ch}: {list(ch_items[ch].get('items', {}).keys())}")
    except OptierSDKError as exc:
        print(f"IO Alarm Range ({label}) error: {exc}")

    print()
    print("=" * 60)
    print(f"IO Alarm Get ({label})")
    print("=" * 60)
    try:
        cfg = cam.io_alarm.get(alarm_in=alarm_in_val)
        ch_info = cfg.get("channel_info", {})
        metadata = {k: v for k, v in cfg.items() if k != "channel_info"}
        if metadata:
            print(f"Metadata: {metadata}")
        print(f"Total returned alarm input ports: {len(ch_info)}")
        active_ports = {
            k: v for k, v in ch_info.items()
            if isinstance(v, dict) and "reason" not in v and v.get("status") not in ["Offline", "Nonsupport", "NotSupport"]
        }
        offline_ports = [k for k, v in ch_info.items() if isinstance(v, dict) and v.get("status") == "Offline"]
        unconfigured_ports = [k for k, v in ch_info.items() if isinstance(v, dict) and v.get("reason") == "Not configured"]

        print(f"Configured/Active IO Alarm ports ({len(active_ports)}): {list(active_ports.keys())}")
        print(f"Offline ports count: {len(offline_ports)}")
        print(f"Not configured ports count: {len(unconfigured_ports)}")

        for port, port_data in list(active_ports.items())[:3]:
            print(f"\n--- {port} ---")
            summary = {
                k: v for k, v in port_data.items()
                if k not in ["voice_prompts_time", "voice_prompts_index", "schedule"]
            }
            pprint.pprint(summary, sort_dicts=False)
    except OptierSDKError as exc:
        print(f"IO Alarm Get ({label}) error: {exc}")
    print()

print("Note: Set API intentionally not executed against hardware.")
print()
print("Disconnecting...")

cam.disconnect()

print("Disconnected.")
