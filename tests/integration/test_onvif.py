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

print("=" * 60)
print("Network ONVIF Range")
print("=" * 60)

try:
    rng = cam.onvif.range()
    pprint.pprint(rng, sort_dicts=False)
except OptierSDKError as exc:
    print(f"Network ONVIF Range error: {exc}")

print()

print("=" * 60)
print("Network ONVIF Get")
print("=" * 60)

try:
    cfg = cam.onvif.get()
    # Safely mask any raw cipher or password fields if returned
    safe_cfg = {}
    for k, v in cfg.items():
        if k == "base_enc_password" and isinstance(v, dict):
            safe_cfg[k] = {
                sub_k: ("<REDACTED_KEY>" if "key" in sub_k or "cipher" in sub_k else sub_v)
                for sub_k, sub_v in v.items()
            }
        elif k == "password" and v:
            safe_cfg[k] = "<MASKED>"
        else:
            safe_cfg[k] = v
    pprint.pprint(safe_cfg, sort_dicts=False)
except OptierSDKError as exc:
    print(f"Network ONVIF Get error: {exc}")

print()
print("Note: Set API intentionally not executed against hardware.")
print()
print("Disconnecting...")

cam.disconnect()

print("Disconnected.")
