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
print("Device Navigation & Page Permissions (/API/Login/DevicePage/Get)")
print("=" * 60)
try:
    get_res = cam.device_page.get()
    main_menus = get_res.get("main", [])
    print(f"Device Navigation Main Sections ({len(main_menus)}):")
    for m in main_menus:
        title = m.get("title")
        submenus = [s.get("title") for s in m.get("sub", [])]
        print(f"  - {title}: {submenus}")
except OptierSDKError as exc:
    print(f"DevicePage Get error: {exc}")

print()
print("Disconnecting...")

cam.disconnect()

print("Disconnected.")
