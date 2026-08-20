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
            if any(s in k_lower for s in ("password", "secret", "token", "cipher", "peer_key", "key")) and v and not k.endswith("_empty"):
                clean[k] = "******"
            else:
                clean[k] = mask_sensitive(v)
        return clean
    elif isinstance(obj, list):
        return [mask_sensitive(elem) for elem in obj]
    return obj


print("=" * 60)
print("Record / Playback SearchMonth (All Channels - 08/01/2026)")
print("=" * 60)
try:
    month_data = cam.search_month.get(start_date="08/01/2026")
    is_has_rec = month_data.get("is_has_rec", [])
    active_days = [day + 1 for day, has_rec in enumerate(is_has_rec) if has_rec]
    print(f"Active recording days in month: {active_days}")
    pprint.pprint(month_data, sort_dicts=False)
except OptierSDKError as exc:
    print(f"SearchMonth Get error: {exc}")

print()
print("=" * 60)
print("Record / Playback SearchMonth (CH1 - 08/01/2026)")
print("=" * 60)
try:
    month_ch1 = cam.search_month.get(start_date="08/01/2026", channel=["CH1"])
    is_has_rec_ch1 = month_ch1.get("is_has_rec", [])
    active_days_ch1 = [day + 1 for day, has_rec in enumerate(is_has_rec_ch1) if has_rec]
    print(f"CH1 active recording days in month: {active_days_ch1}")
except OptierSDKError as exc:
    print(f"SearchMonth CH1 error: {exc}")

print()
print("=" * 60)
print("Record / Playback SearchMonth (Picture Search - 08/01/2026)")
print("=" * 60)
try:
    month_pic = cam.search_month.get(start_date="08/01/2026", search_type="Picture")
    is_has_rec_pic = month_pic.get("is_has_rec", [])
    active_days_pic = [day + 1 for day, has_rec in enumerate(is_has_rec_pic) if has_rec]
    print(f"Picture active days in month: {active_days_pic}")
except OptierSDKError as exc:
    print(f"SearchMonth Picture error: {exc}")

print()
print("Disconnecting...")

cam.disconnect()

print("Disconnected.")
