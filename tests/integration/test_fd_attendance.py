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
print("1. Face Attendance Setup Range (/API/AI/FDAttendance/Range)")
print("=" * 60)
try:
    range_res = cam.fd_attendance.range()
    print("FDAttendance Range Keys:", list(range_res.keys()))
    modes = range_res.get("fd_atd_info", {}).get("items", {}).get("mode", {}).get("items", [])
    print("Supported Attendance Modes:", modes)
except OptierSDKError as exc:
    print(f"FDAttendance Range error: {exc}")

print()
print("=" * 60)
print("2. Face Attendance Setup Get (/API/AI/FDAttendance/Get)")
print("=" * 60)
try:
    get_res = cam.fd_attendance.get()
    print("FDAttendance Get Result:")
    pprint.pprint(get_res, sort_dicts=False)
except OptierSDKError as exc:
    print(f"FDAttendance Get error: {exc}")

print()
print("Disconnecting...")

cam.disconnect()

print("Disconnected.")
