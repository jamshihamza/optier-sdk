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
print("Channel Protocol Manage Range")
print("=" * 60)
try:
    rng = cam.protocol_manage.range()
    proto_items = rng.get("protocol_info", {}).get("items", {})
    print(f"Total Configurable Custom Protocol Slots: {len(proto_items)}")
    if "protocol1" in proto_items:
        p1_schema = proto_items["protocol1"].get("items", {})
        print("\n[Protocol 1 Range Schema]")
        pprint.pprint(p1_schema, sort_dicts=False)
except OptierSDKError as exc:
    print(f"Channel Protocol Manage Range error: {exc}")

print()
print("=" * 60)
print("Channel Protocol Manage Get")
print("=" * 60)
try:
    cfg = cam.protocol_manage.get()
    proto_info = cfg.get("protocol_info", {})
    print(f"Total Custom Protocols Configured: {len(proto_info)}")
    print("\nSample Custom Protocols:")
    for proto_key in ["protocol1", "protocol2"]:
        if proto_key in proto_info:
            print(f"\n[{proto_key}]")
            pprint.pprint(mask_sensitive(proto_info[proto_key]), sort_dicts=False)
except OptierSDKError as exc:
    print(f"Channel Protocol Manage Get error: {exc}")

print()
print("Note: Set API intentionally not executed against hardware.")
print()
print("Disconnecting...")

cam.disconnect()

print("Disconnected.")
