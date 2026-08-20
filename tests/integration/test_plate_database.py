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
print("Plate Database Schema Verification")
print("=" * 60)
print(f"PlateDatabaseManager bound to client: {cam.plate_database is not None}")
print(f"Methods: {['add', 'modify', 'remove', 'change_group']}")

print()
print("Disconnecting...")

cam.disconnect()

print("Disconnected.")
