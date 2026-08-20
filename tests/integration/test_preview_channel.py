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
print("PreviewChannel Unified Sub-API Verification")
print("=" * 60)

# 1. Manual Alarm
print("\n--- 1. Manual Alarm (cam.preview_channel.manual_alarm) ---")
try:
    ma = cam.preview_channel.manual_alarm.get()
    print(f"Total manual alarm outputs: {len(ma)}")
    pprint.pprint(ma, sort_dicts=False)
except OptierSDKError as exc:
    print(f"Manual Alarm error: {exc}")

# 2. Floodlight & Audio Alarm
print("\n--- 2. Floodlight & Audio Alarm (cam.preview_channel.floodlight_audio_alarm) ---")
for ch in ["CH6", "CH29"]:
    try:
        fa = cam.preview_channel.floodlight_audio_alarm.get(channel=ch)
        print(f"[{ch}] Deterrence Status:")
        pprint.pprint(fa, sort_dicts=False)
    except OptierSDKError as exc:
        print(f"[{ch}] Floodlight/AudioAlarm error: {exc}")

# 3. PTZ
print("\n--- 3. PTZ Telemetry & Progress (cam.preview_channel.ptz) ---")
try:
    ptz = cam.preview_channel.ptz.get(channel="CH3")
    prog = cam.preview_channel.ptz.progress(channel="CH3")
    summary = {
        "channel": ptz.get("channel"),
        "speed": ptz.get("speed"),
        "current_cruise_mode": ptz.get("current_cruise_mode"),
        "total_preset_slots": len(ptz.get("preset_point_obj", [])),
        "progress": prog,
    }
    pprint.pprint(summary, sort_dicts=False)
except OptierSDKError as exc:
    print(f"PTZ error: {exc}")

# 4. DualTalk
print("\n--- 4. DualTalk (cam.preview_channel.dual_talk) ---")
try:
    dt = cam.preview_channel.dual_talk.get(channel="CH1")
    print("DualTalk response:")
    pprint.pprint(dt, sort_dicts=False)
except OptierSDKError as exc:
    print(f"DualTalk Get returned expected error/unsupported on tested NVR: {exc}")

print()
print("Note: Set/Control APIs intentionally not executed against hardware.")
print()
print("Disconnecting...")

cam.disconnect()

print("Disconnected.")
