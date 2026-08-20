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
print("1. Face / VHD Log Count (/API/AI/VhdLogCount/Get)")
print("=" * 60)
try:
    vhd_res = cam.face_search.get_vhd_log_count(
        start_time="2026-08-01 00:00:00",
        end_time="2026-08-20 23:59:59",
    )
    print("VHD Log Count:")
    pprint.pprint(vhd_res, sort_dicts=False)
except OptierSDKError as exc:
    print(f"VHD Log Count error: {exc}")

print()
print("=" * 60)
print("2. Snaped Faces Search (/API/AI/SnapedFaces/Search)")
print("=" * 60)
search_count = 0
try:
    search_res = cam.face_search.search(
        start_time="2026-08-01 00:00:00",
        end_time="2026-08-20 23:59:59",
        similarity=70,
    )
    print("Snaped Faces Search Result:")
    pprint.pprint(search_res, sort_dicts=False)
    search_count = search_res.get("Count", 0)
except OptierSDKError as exc:
    print(f"Snaped Faces Search error: {exc}")

if search_count > 0:
    print()
    print("=" * 60)
    print("3. Snaped Faces GetByIndex (/API/AI/SnapedFaces/GetByIndex)")
    print("=" * 60)
    try:
        idx_res = cam.face_search.get_by_index(
            start_index=0,
            count=min(search_count, 5),
            with_face_image=0,
            with_body_image=0,
            with_background=0,
            with_feature=0,
        )
        faces = idx_res.get("SnapedFaceInfo", [])
        print(f"Retrieved {len(faces)} face search records:")
        for f in faces:
            print(f"  - UUID: {f.get('UUId')} | Channel: {f.get('StrChn', f.get('Chn'))} | SnapId: {f.get('SnapId')} | Score: {f.get('Score')} | StartTime: {f.get('StartTime')}")
    except OptierSDKError as exc:
        print(f"GetByIndex error: {exc}")

print()
print("=" * 60)
print("4. Real-time AI Process Alarm (/API/AI/processAlarm/Get)")
print("=" * 60)
try:
    rt_res = cam.face_search.get_realtime_alarm()
    print("Real-time AI Process Alarm:")
    pprint.pprint(rt_res, sort_dicts=False)
except OptierSDKError as exc:
    print(f"Real-time Alarm error: {exc}")

print()
print("Disconnecting...")

cam.disconnect()

print("Disconnected.")
