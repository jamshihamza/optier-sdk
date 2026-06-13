from pathlib import Path
import sys
from datetime import datetime

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

logs = cam.log.search(
    start_date=today,
    start_time="00:00:00",
    end_date=today,
    end_time="23:59:59",
)

print()
print("=" * 60)
print(f"Total Logs : {len(logs)}")
print("=" * 60)

for i, log in enumerate(logs, 1):

    print("-" * 60)

    print(f"#{i}")

    for key, value in log.items():
        print(f"{key:20}: {value}")

print()
print("=" * 60)
print("Log test completed.")
print("=" * 60)

cam.disconnect()