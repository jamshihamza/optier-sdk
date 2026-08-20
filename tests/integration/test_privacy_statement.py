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
print("System Privacy Statement Range")
print("=" * 60)
try:
    range_res = cam.privacy_statement.range()
    print("Privacy Statement Range Summary:")
    print(f"Statement file name limits: {range_res.get('statement_file_name')}")
except OptierSDKError as exc:
    print(f"PrivacyStatement Range error: {exc}")

print()
print("=" * 60)
print("System Privacy Statement Get")
print("=" * 60)
try:
    get_res = cam.privacy_statement.get()
    print("Privacy Statement Current Configuration:")
    pprint.pprint({
        "statement_file_name": get_res.get("statement_file_name"),
    }, sort_dicts=False)
except OptierSDKError as exc:
    print(f"PrivacyStatement Get error: {exc}")

print()
print("Disconnecting...")

cam.disconnect()

print("Disconnected.")
