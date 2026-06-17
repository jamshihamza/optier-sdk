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

cam = Camera(
    host=HOST,
    username=USERNAME,
    password=PASSWORD,
)

url = cam.playback_rtsp.url(
    channel=1,
    subtype=0,
    starttime="2026-06-13T00:00:00Z",
    endtime="2026-06-13T01:00:00Z",
    localtime=True,
)

print()

print("=" * 60)
print("Playback RTSP URL")
print("=" * 60)

print(url)