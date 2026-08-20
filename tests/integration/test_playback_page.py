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
print("Record / Playback Playback Page Range")
print("=" * 60)
try:
    page_res = cam.playback_page.range()
    print("Playback Page Modalities Discovered:")
    for modality, val in page_res.items():
        if isinstance(val, dict):
            print(f"  - {modality}: keys={list(val.keys())}")
        else:
            print(f"  - {modality}: {val}")

    print("\nNormal Playback Record Color Mappings:")
    pprint.pprint(page_res.get("Normal", {}).get("recordColorArr", {}), sort_dicts=False)

    print("\nSmart/AI Playback Event Color Mappings:")
    pprint.pprint(page_res.get("Smart", {}).get("recordColorArr", {}), sort_dicts=False)

    print("\nFace Attendance Schedule Configuration:")
    pprint.pprint(page_res.get("FaceAttendance", {}), sort_dicts=False)
except OptierSDKError as exc:
    print(f"PlaybackPage Range error: {exc}")

print()
print("Disconnecting...")

cam.disconnect()

print("Disconnected.")
