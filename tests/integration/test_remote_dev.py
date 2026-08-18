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
print("RemoteDev / Broadcast IPC Range")
print("=" * 60)
try:
    rng = cam.remote_dev.range()
    dev_info = rng.get("device_info", {})
    summary = {
        "device_info_type": dev_info.get("type"),
        "min_size": dev_info.get("min_size"),
        "max_size": dev_info.get("max_size"),
    }
    pprint.pprint(summary, sort_dicts=False)
except OptierSDKError as exc:
    print(f"RemoteDev Range error: {exc}")

print()
print("=" * 60)
print("RemoteDev / Broadcast IPC Search")
print("=" * 60)
try:
    search_res = cam.remote_dev.search()
    devices = search_res.get("device_info", [])
    print(f"Total Discovered IPCs via Broadcast Search: {len(devices)}")
    if devices:
        for idx, dev in enumerate(devices[:5], 1):
            print(f"\n[Discovered Device #{idx}]")
            pprint.pprint(mask_sensitive(dev), sort_dicts=False)
except OptierSDKError as exc:
    print(f"RemoteDev Search error: {exc}")

print()
print("Note: RemoteDev Set API intentionally not executed against hardware.")
print()
print("Disconnecting...")

cam.disconnect()

print("Disconnected.")
