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
print("Channel Analog Channel Range")
print("=" * 60)
try:
    rng = cam.analog_channel.range()
    summary = {
        "channel_max": rng.get("channel_max"),
        "channel_info_present": "channel_info" in rng,
    }
    pprint.pprint(summary, sort_dicts=False)
except OptierSDKError as exc:
    print(f"Channel Analog Channel Range error: {exc}")

print()
print("=" * 60)
print("Channel Analog Channel Get")
print("=" * 60)
try:
    cfg = cam.analog_channel.get()
    channel_info = cfg.get("channel_info", {})
    print(f"Total Analog Channels Configured: {len(channel_info)}")
    if channel_info:
        for ch_name, ch_data in list(channel_info.items())[:4]:
            print(f"\n[{ch_name}]")
            pprint.pprint(ch_data, sort_dicts=False)
    else:
        print("No physical analog/BNC channels present (Device operates in pure IP NVR mode).")
except OptierSDKError as exc:
    print(f"Channel Analog Channel Get error: {exc}")

print()
print("Note: Set API intentionally not executed against hardware.")
print()
print("Disconnecting...")

cam.disconnect()

print("Disconnected.")
