from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(PROJECT_ROOT))

from optier_sdk import Camera

from tests.fixtures.test_config import (
    HOST_NVR,
    USERNAME_NVR,
    PASSWORD_NVR,
)

cam = Camera(
    host=HOST_NVR,
    username=USERNAME_NVR,
    password=PASSWORD_NVR,
)

print("Connecting...")
cam.connect()

print()

dt = cam.datetime.get()

print("=" * 60)
print("Current Device Date/Time")
print("=" * 60)

for k, v in dt.items():
    print(f"{k}: {v}")

print()

rng = cam.datetime.range()

print("=" * 60)
print("Range")
print("=" * 60)

print(rng)

cam.disconnect()

print()
print("Done.")