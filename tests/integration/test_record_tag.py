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
print("Record Tag Range")
print("=" * 60)

pprint.pprint(
    cam.record_tag.range(),
    sort_dicts=False,
)

print()
print("=" * 60)
print("Record Tag Get")
print("=" * 60)

result = cam.record_tag.get(
    start_date=today,
    start_time="00:00:00",
    end_date=today,
    end_time="23:59:59",
    channel=["CH1"],
    Keyword="",
)

pprint.pprint(
    result,
    sort_dicts=False,
)

print()
print("Disconnecting...")

cam.disconnect()

print("Disconnected.")