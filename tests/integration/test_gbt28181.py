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
            if any(s in k_lower for s in ("password", "secret", "token", "enc_password", "key", "peer_key", "cipher")) and v and not k.endswith("_empty"):
                clean[k] = "******"
            else:
                clean[k] = mask_sensitive(v)
        return clean
    elif isinstance(obj, list):
        return [mask_sensitive(elem) for elem in obj]
    return obj


print("=" * 60)
print("GB/T 28181 Range")
print("=" * 60)
try:
    rng = cam.gbt28181.range()
    pprint.pprint(rng, sort_dicts=False)
except OptierSDKError as exc:
    print(f"GB/T 28181 Range error: {exc}")
    print("Note: OEM Network GB/T 28181 API is unsupported / inactive on this NVR firmware.")

print()
print("=" * 60)
print("GB/T 28181 Get")
print("=" * 60)
try:
    cfg = cam.gbt28181.get()
    pprint.pprint(mask_sensitive(cfg), sort_dicts=False)
except OptierSDKError as exc:
    print(f"GB/T 28181 Get error: {exc}")
    print("Note: OEM Network GB/T 28181 API is unsupported / inactive on this NVR firmware.")

print()
print("Note: Set API intentionally not executed against hardware.")
print()
print("Disconnecting...")

cam.disconnect()

print("Disconnected.")
