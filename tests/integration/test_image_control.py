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
print("Image Control Range")
print("=" * 60)

try:
    rng = cam.image_control.range()
    pprint.pprint(rng, sort_dicts=False)
except OptierSDKError as exc:
    print(f"Image Control Range error: {exc}")

print()

print("=" * 60)
print("Image Control Get")
print("=" * 60)

try:
    cfg = cam.image_control.get()
    pprint.pprint(cfg, sort_dicts=False)
except OptierSDKError as exc:
    print(f"Image Control Get error: {exc}")

print()
print("Note: Set and Default APIs intentionally not executed against hardware.")
print()
print("Disconnecting...")

cam.disconnect()

print("Disconnected.")
