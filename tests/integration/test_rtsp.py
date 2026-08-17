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
print("RTSP Range")
print("=" * 60)
try:
    rng = cam.rtsp.range()
    pprint.pprint(rng, sort_dicts=False)
except OptierSDKError as exc:
    print(f"RTSP Range result / error: {exc}")
    print("Note: OEM documentation explicitly specifies: 'note:(DVR/NVR not supported)' for /API/NetworkConfig/Rtsp/Range.")

print()
print("=" * 60)
print("RTSP Get")
print("=" * 60)
try:
    cfg = cam.rtsp.get()
    # Mask any credentials if present
    safe_cfg = {
        k: (
            "******"
            if any(s in k.lower() for s in ("password", "secret", "token")) and v
            else v
        )
        for k, v in cfg.items()
    }
    pprint.pprint(safe_cfg, sort_dicts=False)
except OptierSDKError as exc:
    print(f"RTSP Get result / error: {exc}")
    print("Note: OEM documentation explicitly specifies: 'note:(DVR/NVR not supported)' for /API/NetworkConfig/Rtsp/Get.")

print()
print("Note: RTSP streaming URLs on NVR are provided via Channel RtspUrl (/API/Channel/RtspUrl/Get), managed by cam.rtsp_url.")
print("Note: Set API intentionally not executed against hardware.")
print()
print("Disconnecting...")

cam.disconnect()

print("Disconnected.")
