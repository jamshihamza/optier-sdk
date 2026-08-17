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
print("Network Base Range (default: data={})")
print("=" * 60)

try:
    rng_default = cam.network_base.range()
    pprint.pprint(rng_default, sort_dicts=False)
except OptierSDKError as exc:
    print(f"Network Base Range (default) error: {exc}")

print()

print("=" * 60)
print("Network Base Range (with page_type='net_general')")
print("=" * 60)

try:
    rng_general = cam.network_base.range(page_type="net_general")
    pprint.pprint(rng_general, sort_dicts=False)
except OptierSDKError as exc:
    print(f"Network Base Range (page_type) error: {exc}")

print()

print("=" * 60)
print("Network Base Get (default: data={})")
print("=" * 60)

try:
    cfg_default = cam.network_base.get()
    pprint.pprint(cfg_default, sort_dicts=False)
except OptierSDKError as exc:
    print(f"Network Base Get (default) error: {exc}")

print()

print("=" * 60)
print("Network Base Get (with page_type='net_general')")
print("=" * 60)

try:
    cfg_general = cam.network_base.get(page_type="net_general")
    pprint.pprint(cfg_general, sort_dicts=False)
except OptierSDKError as exc:
    print(f"Network Base Get (page_type) error: {exc}")

print()
print("Note: Set API intentionally not executed against hardware.")
print()
print("Disconnecting...")

cam.disconnect()

print("Disconnected.")
