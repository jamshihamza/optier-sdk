from pathlib import Path
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

print("Connected successfully.")
print()

# --------------------------------------------------
# Current Status
# --------------------------------------------------

print("=" * 60)
print("Defogging Fan Status")
print("=" * 60)

status = cam.defogging_fan.get()

for key, value in status.items():
    print(f"{key:25}: {value}")

print()

# --------------------------------------------------
# Range
# --------------------------------------------------

print("=" * 60)
print("Defogging Fan Range")
print("=" * 60)

rng = cam.defogging_fan.range()

print(rng)

print()

# --------------------------------------------------
# Optional SET Test
# --------------------------------------------------
#
# Uncomment ONLY if you really want to
# change the device configuration.
#

# print("Enabling Defogging Fan...")
# cam.defogging_fan.set(True)
# print(cam.defogging_fan.get())
#
# print("Disabling Defogging Fan...")
# cam.defogging_fan.set(False)
# print(cam.defogging_fan.get())

print()
print("=" * 60)
print("Defogging Fan test completed successfully.")
print("=" * 60)

cam.disconnect()

print("Disconnected.")