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

print("Connected.")
print()

print("=" * 60)
print("NTP Configuration")
print("=" * 60)

cfg = cam.ntp.get()

for key, value in cfg.items():
    print(f"{key:20}: {value}")

print()

print("=" * 60)
print("NTP Range")
print("=" * 60)

rng = cam.ntp.range()

print(rng)

print()
print("Disconnecting...")

cam.disconnect()

print("Disconnected.")