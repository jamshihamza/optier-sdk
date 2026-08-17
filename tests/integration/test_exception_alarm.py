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
print("Exception Alarm Range")
print("=" * 60)

try:
    rng = cam.exception_alarm.range()
    pprint.pprint({k: v for k, v in rng.items() if k != "exception_info"}, sort_dicts=False)
    exc_items = rng.get("exception_info", {}).get("items", {})
    print(f"Discovered Exception Types in Range ({len(exc_items)}): {list(exc_items.keys())}")
    for exc_name, exc_schema in exc_items.items():
        print(f"  {exc_name}: {list(exc_schema.get('items', {}).keys())}")
except OptierSDKError as exc:
    print(f"Exception Alarm Range error: {exc}")

print()

print("=" * 60)
print("Exception Alarm Get")
print("=" * 60)

try:
    cfg = cam.exception_alarm.get()
    exc_info = cfg.get("exception_info", {})
    print(f"Configured Exception Types in Get ({len(exc_info)}): {list(exc_info.keys())}")
    for exc_name, exc_val in exc_info.items():
        print(f"\n--- {exc_name} ---")
        summary = {
            k: v for k, v in exc_val.items()
            if k not in ["voice_prompts_time", "voice_prompts_index"]
        }
        pprint.pprint(summary, sort_dicts=False)
except OptierSDKError as exc:
    print(f"Exception Alarm Get error: {exc}")

print()
print("Note: Set API intentionally not executed against hardware.")
print()
print("Disconnecting...")

cam.disconnect()

print("Disconnected.")
