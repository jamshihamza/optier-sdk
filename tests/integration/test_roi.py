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


def mask_sensitive(obj):
    if isinstance(obj, dict):
        clean = {}
        for k, v in obj.items():
            k_lower = k.lower()
            if any(s in k_lower for s in ("password", "secret", "token", "cipher", "peer_key", "key")) and v and not k.endswith("_empty"):
                clean[k] = "******"
            else:
                clean[k] = mask_sensitive(v)
        return clean
    elif isinstance(obj, list):
        return [mask_sensitive(elem) for elem in obj]
    return obj


print("=" * 60)
print("Channel ROI Range")
print("=" * 60)
try:
    rng = cam.roi.range()
    summary = {
        "channel_max": rng.get("channel_max"),
        "channel_info_type": rng.get("channel_info", {}).get("type"),
    }
    pprint.pprint(summary, sort_dicts=False)
except OptierSDKError as exc:
    print(f"Channel ROI Range error: {exc}")

print()
print("=" * 60)
print("Channel ROI Get")
print("=" * 60)
try:
    cfg = cam.roi.get()
    channel_info = cfg.get("channel_info", {})
    configured_channels = [ch for ch, data in channel_info.items() if not (isinstance(data, dict) and data.get("reason") == "Not configured")]
    unconfigured_channels = [ch for ch, data in channel_info.items() if isinstance(data, dict) and data.get("reason") == "Not configured"]

    print(f"Total Channels: {len(channel_info)}")
    print(f"ROI-Capable Channels: {len(configured_channels)}")
    print(f"Not Configured Channels: {len(unconfigured_channels)}")

    if "CH1" in channel_info:
        ch1 = channel_info["CH1"]
        print("\n[CH1 ROI Configuration Sample]")
        sample = {
            "main_stream_regions": len(ch1.get("main_stream_info", {})),
            "sub_stream_regions": len(ch1.get("sub_stream_info", {})),
            "mobile_stream_regions": len(ch1.get("mobile_stream_info", {})),
            "main_stream_region_1": ch1.get("main_stream_info", {}).get("region_id_1"),
        }
        pprint.pprint(sample, sort_dicts=False)
except OptierSDKError as exc:
    print(f"Channel ROI Get error: {exc}")

print()
print("Note: Set API intentionally not executed against hardware.")
print()
print("Disconnecting...")

cam.disconnect()

print("Disconnected.")
