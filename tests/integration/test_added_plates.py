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
print("1. Enrolled License Plates GetCount (/API/AI/AddedPlates/GetCount)")
print("=" * 60)
try:
    cnt_res = cam.added_plates.get_count(group_ids=[1, 2, 3])
    print("AddedPlates GetCount Result:")
    pprint.pprint(cnt_res, sort_dicts=False)
except OptierSDKError as exc:
    print(f"AddedPlates GetCount error: {exc}")

print()
print("=" * 60)
print("2. Enrolled License Plates GetId (/API/AI/AddedPlates/GetId)")
print("=" * 60)
try:
    id_res = cam.added_plates.get_id(group_ids=[1, 2, 3])
    print("AddedPlates GetId Result:")
    pprint.pprint(id_res, sort_dicts=False)
except OptierSDKError as exc:
    print(f"AddedPlates GetId error: {exc}")

print()
print("Disconnecting...")

cam.disconnect()

print("Disconnected.")
