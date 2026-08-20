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
print("PreviewChannel PTZ Get (Speed Dome CH3)")
print("=" * 60)
try:
    ptz_ch3 = cam.preview_ptz.get(channel="CH3")
    preset_obj = ptz_ch3.get("preset_point_obj", [])
    configured_presets = [p for p in preset_obj if p.get("add")]
    summary_ch3 = {
        "channel": ptz_ch3.get("channel"),
        "speed": ptz_ch3.get("speed"),
        "current_cruise_mode": ptz_ch3.get("current_cruise_mode"),
        "total_preset_slots": len(preset_obj),
        "configured_presets_count": len(configured_presets),
        "watch_mode_mode": ptz_ch3.get("watch_mode_mode"),
        "line_scan_area": ptz_ch3.get("line_scan_area"),
        "line_scan_speed": ptz_ch3.get("line_scan_speed"),
        "belt_times_use": ptz_ch3.get("belt_times_use"),
    }
    pprint.pprint(summary_ch3, sort_dicts=False)
except OptierSDKError as exc:
    print(f"CH3 PTZ Get error: {exc}")

print()
print("=" * 60)
print("PreviewChannel PTZ Progress (CH3 & CH1)")
print("=" * 60)
for ch in ["CH3", "CH1"]:
    try:
        prog = cam.preview_ptz.progress(channel=ch)
        print(f"\n[{ch}] Progress:")
        pprint.pprint(prog, sort_dicts=False)
    except OptierSDKError as exc:
        print(f"[{ch}] Progress error: {exc}")

print()
print("Note: Control API intentionally not executed against hardware.")
print()
print("Disconnecting...")

cam.disconnect()

print("Disconnected.")
