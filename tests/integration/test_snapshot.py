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

print("Connecting...")

cam = Camera(
    host=HOST,
    username=USERNAME,
    password=PASSWORD,
)

cam.connect()

print("Connected.")

print("Capturing snapshot...")

image = cam.snapshot.get(
    channel="CH13",
    snapshot_resolution="1280x720",
)

with open("snapshot.jpg", "wb") as f:
    f.write(image)

print("snapshot.jpg saved.")

cam.disconnect()

print("Done.")