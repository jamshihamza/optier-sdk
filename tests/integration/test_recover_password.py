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
            if any(s in k_lower for s in ("password", "secret", "token", "cipher", "peer_key", "key", "answer")) and v and not k.endswith("_empty"):
                clean[k] = "******"
            else:
                clean[k] = mask_sensitive(v)
        return clean
    elif isinstance(obj, list):
        return [mask_sensitive(elem) for elem in obj]
    return obj


print("=" * 60)
print("Login Recover Password Range")
print("=" * 60)
try:
    range_res = cam.recover_password.range()
    print("Password Recovery Range Summary:")
    print(f"Answer retrieval supported: {range_res.get('answer_flag')}")
    print(f"Certificate retrieval supported: {range_res.get('certificate_flag')}")
    print(f"Super password supported: {range_res.get('super_pwd_flag')}")
    print(f"Questions supported count: {range_res.get('questions', {}).get('size')}")
    print(f"Available question IDs: {range_res.get('questions', {}).get('items', [{}])[0].get('items')}")
    print(f"Email limits: {range_res.get('email')}")
except OptierSDKError as exc:
    print(f"RecoverPassword Range error: {exc}")

print()
print("=" * 60)
print("Login Recover Password Get")
print("=" * 60)
try:
    get_res = cam.recover_password.get()
    print("Password Recovery Current Configuration:")
    pprint.pprint({
        "questions": get_res.get("questions"),
    }, sort_dicts=False)
except OptierSDKError as exc:
    print(f"RecoverPassword Get error: {exc}")

print()
print("Disconnecting...")

cam.disconnect()

print("Disconnected.")
