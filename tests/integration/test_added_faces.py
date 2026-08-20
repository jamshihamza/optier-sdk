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
print("1. Enrolled Face Database Search (/API/AI/AddedFaces/Search)")
print("=" * 60)
try:
    search_res = cam.added_faces.search(face_info=[])
    print("AddedFaces Search Result:")
    pprint.pprint(search_res, sort_dicts=False)
except OptierSDKError as exc:
    print(f"AddedFaces Search error: {exc}")

print()
print("=" * 60)
print("2. Enrolled Face Database GetByIndex (/API/AI/AddedFaces/GetByIndex)")
print("=" * 60)
try:
    idx_res = cam.added_faces.get_by_index(start_index=0, count=5, simple_info=1)
    print("AddedFaces GetByIndex Result:")
    pprint.pprint(idx_res, sort_dicts=False)
except OptierSDKError as exc:
    print(f"AddedFaces GetByIndex error: {exc}")

print()
print("=" * 60)
print("3. Enrolled Face Database GetId (/API/AI/AddedFaces/GetId)")
print("=" * 60)
try:
    id_res = cam.added_faces.get_id(group_ids=[1, 2, 3])
    print("AddedFaces GetId Result:")
    pprint.pprint(id_res, sort_dicts=False)
except OptierSDKError as exc:
    print(f"AddedFaces GetId error: {exc}")

print()
print("Disconnecting...")

cam.disconnect()

print("Disconnected.")
