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
print("License Plate Groups (PlateGroup) Get")
print("=" * 60)
try:
    res = cam.plate_group.get()
    print(f"Plate Groups SupportAI: {res.get('SupportAI')}")
    print(f"Plate Groups Count: {res.get('Count')}")
    print(f"Plate Groups Available Channels: {len(res.get('channel', []))}")
    print(f"Similarity Limits: {res.get('param_limit', {}).get('similarity')}")
    groups = res.get("Group", [])
    print(f"Configured Watchlist Groups ({len(groups)}):")
    for g in groups:
        print(f"  - ID: {g.get('Id')} | Name: {g.get('Name')} | Similarity: {g.get('Similarity')} | Enabled: {g.get('Enabled')}")
except OptierSDKError as exc:
    print(f"PlateGroup Get error: {exc}")

print()
print("=" * 60)
print("License Plate Groups GetId")
print("=" * 60)
try:
    id_res = cam.plate_group.get_id(detect_type=2)
    print("Next Available Plate Group ID response:")
    pprint.pprint(id_res, sort_dicts=False)
except OptierSDKError as exc:
    print(f"PlateGroup GetId error: {exc}")

print()
print("Disconnecting...")

cam.disconnect()

print("Disconnected.")
