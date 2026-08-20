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
print("1. System Multi-User Accounts Range (/API/SystemConfig/User/Range)")
print("=" * 60)
try:
    range_res = cam.system_user.range()
    print("User Range Keys:", list(range_res.keys()))
    print("Support User Filter:", range_res.get("support_user_filter"))
except OptierSDKError as exc:
    print(f"SystemUser Range error: {exc}")

print()
print("=" * 60)
print("2. System Multi-User Accounts Get (/API/SystemConfig/User/Get)")
print("=" * 60)
try:
    get_res = cam.system_user.get()
    users = get_res.get("user_info", {})
    print(f"Total Available User Account Slots: {len(users)}")
    active_users = {k: v for k, v in users.items() if isinstance(v, dict) and (v.get("user_enable") or v.get("username") == "admin" or not v.get("password_empty"))}
    print(f"Configured / Active User Accounts ({len(active_users)}):")
    for k, v in active_users.items():
        print(f"  [{k}] Username: '{v.get('username')}' | Enabled: {v.get('user_enable')} | Login Limit: {v.get('login_num')} | Password Empty: {v.get('password_empty')}")
except OptierSDKError as exc:
    print(f"SystemUser Get error: {exc}")

print()
print("Disconnecting...")

cam.disconnect()

print("Disconnected.")
