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

PAGES = [
    "MainStream",
    "SubStream",
    "MobileStream",
    "EventStream",
]

for page in PAGES:
    print("=" * 60)
    print(f"Encode Page: {page} - Range")
    print("=" * 60)
    try:
        rng = cam.encode.range(page)
        pprint.pprint(rng, sort_dicts=False)
    except OptierSDKError as exc:
        print(f"[{page}] Range error/unsupported: {exc}")

    print()

    print("=" * 60)
    print(f"Encode Page: {page} - Get")
    print("=" * 60)
    try:
        cfg = cam.encode.get(page)
        pprint.pprint(cfg, sort_dicts=False)
    except OptierSDKError as exc:
        print(f"[{page}] Get error/unsupported: {exc}")

    print()

print("Note: Set API intentionally not executed against hardware.")
print()
print("Disconnecting...")

cam.disconnect()

print("Disconnected.")
