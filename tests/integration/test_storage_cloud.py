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
print("Storage Cloud Storage Range")
print("=" * 60)
try:
    range_res = cam.storage_cloud.range()
    print("Cloud Storage Range Summary:")
    print(f"Supported cloud types: {range_res.get('cloud_type', {}).get('items')}")
    print(f"Supported cloud statuses: {range_res.get('cloud_status', {}).get('items')}")
    print(f"Overwrite policies: {range_res.get('cloud_over_write', {}).get('items')}")
    print(f"Video file types: {range_res.get('video_type', {}).get('items')}")
    print(f"Channel max: {range_res.get('channel_max')}")
    channels = list(range_res.get("channel_info", {}).get("items", {}).keys())
    print(f"Channel folder configuration slots: {len(channels)} (first 5: {channels[:5]})")
except OptierSDKError as exc:
    print(f"StorageCloud Range error: {exc}")

print()
print("=" * 60)
print("Storage Cloud Storage Get")
print("=" * 60)
try:
    get_res = cam.storage_cloud.get()
    print("Cloud Storage Current Configuration:")
    pprint.pprint({
        "cloud_storage": get_res.get("cloud_storage"),
        "cloud_type": get_res.get("cloud_type"),
        "cloud_status": get_res.get("cloud_status"),
        "total_size": get_res.get("total_size"),
        "used_size": get_res.get("used_size"),
        "progress": get_res.get("progress"),
        "cloud_over_write": get_res.get("cloud_over_write"),
        "video_type": get_res.get("video_type"),
        "channel_count": len(get_res.get("channel_info", {})),
    }, sort_dicts=False)
except OptierSDKError as exc:
    print(f"StorageCloud Get error: {exc}")

print()
print("Disconnecting...")

cam.disconnect()

print("Disconnected.")
