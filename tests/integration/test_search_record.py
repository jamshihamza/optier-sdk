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
print("Record / Playback SearchRecord Range")
print("=" * 60)
try:
    range_data = cam.search_record.range()
    channels = range_data.get("channel", {}).get("items", [])
    stream_modes = range_data.get("stream_mode", {}).get("items", [])
    summary_range = {
        "total_supported_channels": len(channels),
        "supported_stream_modes": stream_modes,
        "record_type_limits": range_data.get("record_type", {}),
        "size_limits": range_data.get("size", {}),
        "disk_event_id_limits": range_data.get("disk_event_id", {}),
    }
    pprint.pprint(summary_range, sort_dicts=False)
except OptierSDKError as exc:
    print(f"SearchRecord Range error: {exc}")

print()
print("=" * 60)
print("Record / Playback SearchRecord Search (CH1 - 08/20/2026)")
print("=" * 60)
try:
    records = cam.search_record.search(
        start_date="08/20/2026",
        end_date="08/20/2026",
        channel=["CH1"],
        stream_mode="Mainstream",
    )
    print(f"Total channel record groups returned: {len(records)}")
    if records and records[0]:
        print(f"Total segments found in CH1: {len(records[0])}")
        print("\nFirst 3 segments:")
        for idx, seg in enumerate(records[0][:3]):
            print(f"Segment #{idx + 1}: {seg.get('start_time')} -> {seg.get('end_time')} | Size: {seg.get('size')} B | Type: {seg.get('new_record_type')} (ID: {seg.get('record_id')})")
    else:
        print("No segments found for specified date.")
except OptierSDKError as exc:
    print(f"SearchRecord Search error: {exc}")

print()
print("Disconnecting...")

cam.disconnect()

print("Disconnected.")