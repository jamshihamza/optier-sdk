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
print("Record / Playback Pic Playback Search (CH1 - 08/01/2026 to 08/20/2026)")
print("=" * 60)
try:
    search_res = cam.picture_playback.search(
        start_date="08/01/2026",
        end_date="08/20/2026",
        channel=["CH1"],
    )
    print("Picture Search Response:")
    pprint.pprint(search_res, sort_dicts=False)
    pics = search_res.get("all_pic_info", [])
    if pics:
        first_token = pics[0].get("pic_info")
        print(f"\nFetching snapshot image data for token: {first_token}...")
        pic_data = cam.picture_playback.get(pic_info=first_token)
        print("Snapshot fetch success:")
        pprint.pprint({
            "channel": pic_data.get("channel"),
            "time": pic_data.get("time"),
            "image_base64_length": len(pic_data.get("image", "")),
        }, sort_dicts=False)
except OptierSDKError as exc:
    print(f"PicturePlayback Search error: {exc}")

print()
print("=" * 60)
print("Record / Playback Pic Playback Search (Multi-Channel CH1..CH8)")
print("=" * 60)
try:
    multi_res = cam.picture_playback.search(
        start_date="08/01/2026",
        end_date="08/20/2026",
        channel=[f"CH{i}" for i in range(1, 9)],
    )
    print("Multi-channel Picture Search Summary:")
    print(f"Overload: {multi_res.get('overload')}, Total pictures found: {multi_res.get('all_pic_num')}")
except OptierSDKError as exc:
    print(f"Multi-channel Picture Search error: {exc}")

print()
print("Disconnecting...")

cam.disconnect()

print("Disconnected.")
