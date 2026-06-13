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

print("Connecting...")

cam = Camera(
    host=HOST_NVR,
    username=USERNAME_NVR,
    password=PASSWORD_NVR,
)

cam.connect()

print("Connected.")

print("Capturing snapshot...")

image = cam.snapshot.get(
    channel="CH1",
    snapshot_resolution="1280x720",
)

with open("snapshot.jpg", "wb") as f:
    f.write(image)

print("snapshot.jpg saved.")

cam.disconnect()

print("Done.")