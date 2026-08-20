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
print("1. Snaped License Plate Search (/API/AI/SnapedObjects/SearchPlate)")
print("=" * 60)
search_count = 0
try:
    search_res = cam.plate_search.search(
        start_time="2026-08-01 00:00:00",
        end_time="2026-08-20 23:59:59",
    )
    print("License Plate Search Result:")
    pprint.pprint(search_res, sort_dicts=False)
    search_count = search_res.get("Count", 0)
except OptierSDKError as exc:
    print(f"License Plate Search error: {exc}")

if search_count > 0:
    print()
    print("=" * 60)
    print("2. Snaped License Plate GetByIndex (/API/AI/SnapedObjects/GetByIndex)")
    print("=" * 60)
    try:
        idx_res = cam.plate_search.get_by_index(
            start_index=0,
            count=min(search_count, 3),
            with_object_image=0,
            with_background=0,
        )
        plates = idx_res.get("SnapedObjInfo", [])
        print(f"Retrieved {len(plates)} license plate records:")
        for p in plates:
            print(f"  - UUID: {p.get('UUId')} | Channel: {p.get('StrChn', p.get('Chn'))} | Plate: {p.get('Plate')} | Matched: {p.get('MatchedPlate')} | StartTime: {p.get('StartTime')}")
    except OptierSDKError as exc:
        print(f"GetByIndex error: {exc}")

print()
print("Disconnecting...")

cam.disconnect()

print("Disconnected.")
