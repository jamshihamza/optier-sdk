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
print("Maintenance IPC Upgrade Range")
print("=" * 60)
try:
    range_res = cam.ipc_upgrade.range()
    print("IPC Upgrade Range Summary:")
    print(f"Channel max: {range_res.get('channel_max')}")
    print(f"Password limits: {range_res.get('password')}")
    channels = list(range_res.get("channel_info", {}).get("items", {}).keys())
    print(f"Configured IPC upgrade channel slots: {len(channels)} (channels: {channels})")
except OptierSDKError as exc:
    print(f"IPCUpgrade Range error: {exc}")

print()
print("=" * 60)
print("Maintenance IPC Upgrade Get")
print("=" * 60)
try:
    get_res = cam.ipc_upgrade.get()
    channels = get_res.get("channel_info", {})
    print(f"IPC Upgrade Total Channels: {len(channels)}")
    online = {k: v for k, v in channels.items() if v.get("state") == "On-line"}
    print(f"Online IPC Cameras ({len(online)}):")
    pprint.pprint(dict(list(online.items())[:5]), sort_dicts=False)
except OptierSDKError as exc:
    print(f"IPCUpgrade Get error: {exc}")

print()
print("Disconnecting...")

cam.disconnect()

print("Disconnected.")
