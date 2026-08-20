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
print("Account Rules & Password Complexity Get")
print("=" * 60)
try:
    res = cam.account_rules.get()
    print("Account Rules Policy:")
    for k, v in res.items():
        print(f"  [{k}] min_len={v.get('min_length')} | max_len={v.get('max_length')} | combos={v.get('character_combinations_num')} | not_same_user={v.get('not_same_username')}")
except OptierSDKError as exc:
    print(f"AccountRules Get error: {exc}")

print()
print("Disconnecting...")

cam.disconnect()

print("Disconnected.")
