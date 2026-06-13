from pathlib import Path
from datetime import datetime
import pprint
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

print("=" * 60)
print("Connecting...")
print("=" * 60)

cam.connect()

today = datetime.now().strftime("%m/%d/%Y")

print()
print("=" * 60)
print("Search Record Range")
print("=" * 60)

pprint.pprint(
    cam.search_record.range(),
    sort_dicts=False,
)

print()
print("=" * 60)
print("Search Today's CH1 Records")
print("=" * 60)

result = cam.search_record.search(
    channel=["CH1"],
    start_date=today,
    start_time="00:00:00",
    end_date=today,
    end_time="23:59:59",
    record_type=0xFFFFFFFF,
)

pprint.pprint(
    result,
    sort_dicts=False,
)

print()
print("Disconnecting...")

cam.disconnect()

print("Disconnected.")