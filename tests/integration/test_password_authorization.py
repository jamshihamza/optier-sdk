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
print("1. Password Authorization Range")
print("=" * 60)
try:
    range_res = cam.password_authorization.range()
    print("Authorization Range Modes:", range_res.get("mode", {}).get("items", []))
    print("Available Security Questions Count:", len(range_res.get("questions", {}).get("items", [{}])[0].get("items", [])))
except OptierSDKError as exc:
    print(f"PasswordAuthorization Range error: {exc}")

print()
print("=" * 60)
print("2. Password Authorization Get")
print("=" * 60)
try:
    get_res = cam.password_authorization.get()
    print("Password Authorization Get Configuration:")
    pprint.pprint(get_res, sort_dicts=False)
except OptierSDKError as exc:
    print(f"PasswordAuthorization Get error: {exc}")

print()
print("Disconnecting...")

cam.disconnect()

print("Disconnected.")
