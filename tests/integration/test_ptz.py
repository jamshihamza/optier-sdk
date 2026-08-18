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
print("Channel PTZ Range")
print("=" * 60)
try:
    rng = cam.ptz.range()
    summary = {
        "channel_max": rng.get("channel_max"),
        "support_copy": rng.get("support_copy"),
    }
    pprint.pprint(summary, sort_dicts=False)
except OptierSDKError as exc:
    print(f"Channel PTZ Range error: {exc}")

print()
print("=" * 60)
print("Channel PTZ Get")
print("=" * 60)
try:
    cfg = cam.ptz.get()
    channel_info = cfg.get("channel_info", {})
    configured_channels = {
        k: v
        for k, v in channel_info.items()
        if "reason" not in v
    }
    unsupported_channels = {
        k: v
        for k, v in channel_info.items()
        if v.get("reason") == "Not support"
    }
    not_configured_channels = {
        k: v
        for k, v in channel_info.items()
        if v.get("reason") == "Not configured"
    }

    print(f"Total Channels: {len(channel_info)}")
    print(f"PTZ-Configured Channels: {len(configured_channels)}")
    print(f"Fixed / Unsupported Channels: {len(unsupported_channels)}")
    print(f"Not Configured Channels: {len(not_configured_channels)}")
    print()

    print("Sample Configured PTZ Channels:")
    for ch_name in ["CH2", "CH3", "CH36"]:
        if ch_name in configured_channels:
            print(f"\n[{ch_name}]")
            pprint.pprint(mask_sensitive(configured_channels[ch_name]), sort_dicts=False)

except OptierSDKError as exc:
    print(f"Channel PTZ Get error: {exc}")

print()
print("Note: Set API intentionally not executed against hardware.")
print()
print("Disconnecting...")

cam.disconnect()

print("Disconnected.")
