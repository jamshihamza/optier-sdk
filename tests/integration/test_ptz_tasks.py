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


def mask_sensitive(obj):
    if isinstance(obj, dict):
        clean = {}
        for k, v in obj.items():
            k_lower = k.lower()
            if any(s in k_lower for s in ("password", "secret", "token", "cipher", "peer_key", "key")) and v and not k.endswith("_empty"):
                clean[k] = "******"
            else:
                clean[k] = mask_sensitive(v)
        return clean
    elif isinstance(obj, list):
        return [mask_sensitive(elem) for elem in obj]
    return obj


print("=" * 60)
print("Channel Scheduled Tasks / PTZ Tasks Range")
print("=" * 60)
try:
    rng = cam.ptz_tasks.range()
    summary = {
        "channel_max": rng.get("channel_max"),
        "supported_channels": list(rng.get("channel_info", {}).get("items", {}).keys()),
    }
    pprint.pprint(summary, sort_dicts=False)
except OptierSDKError as exc:
    print(f"Channel PTZ Tasks Range error: {exc}")

print()
print("=" * 60)
print("Channel Scheduled Tasks / PTZ Tasks Get")
print("=" * 60)
try:
    cfg = cam.ptz_tasks.get()
    channel_info = cfg.get("channel_info", {})
    print(f"PTZ Channels with Scheduled Cruise Tasks: {len(channel_info)}")
    for ch_name, ch_data in channel_info.items():
        print(f"\n[{ch_name} PTZ Scheduled Tasks]")
        task_summary = {
            "schedule_tasks_enable": ch_data.get("schedule_tasks_enable"),
            "belt_times_use": ch_data.get("belt_times_use"),
            "tasks_recovery_times": ch_data.get("tasks_recovery_times"),
            "total_schedule_modes": len(ch_data.get("schedule", [])),
            "schedule_types": [s.get("schedule_type") for s in ch_data.get("schedule", [])],
        }
        pprint.pprint(task_summary, sort_dicts=False)
except OptierSDKError as exc:
    print(f"Channel PTZ Tasks Get error: {exc}")

print()
print("Note: Set API intentionally not executed against hardware.")
print()
print("Disconnecting...")

cam.disconnect()

print("Disconnected.")
