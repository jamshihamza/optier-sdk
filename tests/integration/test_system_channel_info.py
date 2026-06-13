from pathlib import Path
import pprint
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(PROJECT_ROOT))

from optier_sdk import Camera

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
print("System Channel Information")
print("=" * 60)

info = cam.channel_info.get()

pprint.pprint(
    info,
    sort_dicts=False,
)

print()

if "channel_max" in info:
    print(f"Channel Max : {info['channel_max']}")

print()

print("Disconnecting...")

cam.disconnect()

print("Disconnected.")