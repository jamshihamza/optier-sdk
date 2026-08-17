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
print("Auto Reboot Range")
print("=" * 60)

rng = cam.auto_reboot.range()
pprint.pprint(
    rng,
    sort_dicts=False,
)

print()

print("=" * 60)
print("Auto Reboot Configuration")
print("=" * 60)

cfg = cam.auto_reboot.get()

for key, value in cfg.items():
    print(f"{key:25}: {value}")

print()
print("Note: Set API intentionally not executed against hardware.")
print()
print("Disconnecting...")

cam.disconnect()

print("Disconnected.")
