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
print("FTP Range")
print("=" * 60)
try:
    rng = cam.ftp.range()
    pprint.pprint(rng, sort_dicts=False)
except OptierSDKError as exc:
    print(f"FTP Range error: {exc}")

print()
print("=" * 60)
print("FTP Get")
print("=" * 60)
try:
    cfg = cam.ftp.get()
    # Mask any password if present
    safe_cfg = {
        k: ("******" if "password" in k.lower() and v and k != "password_empty" else v)
        for k, v in cfg.items()
    }
    pprint.pprint(safe_cfg, sort_dicts=False)
except OptierSDKError as exc:
    print(f"FTP Get error: {exc}")

print()
print("Note: Set and Test APIs intentionally not executed against hardware.")
print()
print("Disconnecting...")

cam.disconnect()

print("Disconnected.")
