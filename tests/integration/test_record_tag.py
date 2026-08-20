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
print("Record / Playback Record Tag Range")
print("=" * 60)
try:
    range_res = cam.record_tag.range()
    channels = range_res.get("tag", {}).get("items", {}).get("channel", {}).get("items", [])
    print(f"Record Tag Range Summary:")
    print(f"Supported channels: {len(channels)} channels (first 5: {channels[:5]})")
    print(f"Tag Name constraints: {range_res.get('Tag_name')}")
    print(f"Pre-play options: {range_res.get('Pre-play', {}).get('items')}")
    print(f"Post-play options: {range_res.get('Post-play', {}).get('items')}")
    print(f"Current device date/time: {range_res.get('date')} {range_res.get('time')}")
except OptierSDKError as exc:
    print(f"RecordTag Range error: {exc}")

print()
print("=" * 60)
print("Record / Playback Record Tag Get (CH1 - August 2026)")
print("=" * 60)
try:
    get_res = cam.record_tag.get(
        start_date="08/01/2026",
        end_date="08/20/2026",
        channel=["CH1"],
    )
    print("Record Tag Get Response:")
    pprint.pprint(get_res, sort_dicts=False)
except OptierSDKError as exc:
    print(f"RecordTag Get error: {exc}")

print()
print("=" * 60)
print("Record / Playback Record Tag Get (Multi-Channel CH1..CH8)")
print("=" * 60)
try:
    multi_res = cam.record_tag.get(
        start_date="08/01/2026",
        end_date="08/20/2026",
        channel=[f"CH{i}" for i in range(1, 9)],
    )
    print("Multi-channel Tag Search Summary:")
    print(f"Total tags found: {multi_res.get('all_tag_num')}, Pre-play: {multi_res.get('Pre-play')}, Post-play: {multi_res.get('Post-play')}")
except OptierSDKError as exc:
    print(f"Multi-channel Tag Search error: {exc}")

print()
print("Disconnecting...")

cam.disconnect()

print("Disconnected.")