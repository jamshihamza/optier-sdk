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
print("DDNS Range")
print("=" * 60)
try:
    rng = cam.ddns.range()
    pprint.pprint(rng, sort_dicts=False)
except OptierSDKError as exc:
    print(f"DDNS Range error: {exc}")

print()
print("=" * 60)
print("DDNS Get")
print("=" * 60)
try:
    cfg = cam.ddns.get()
    # Mask any password or api_key if present
    safe_cfg = {
        k: (
            "******"
            if any(s in k.lower() for s in ("password", "key", "secret"))
            and v
            and not k.endswith("_empty")
            else v
        )
        for k, v in cfg.items()
    }
    pprint.pprint(safe_cfg, sort_dicts=False)
except OptierSDKError as exc:
    print(f"DDNS Get error: {exc}")

print()
print("Note: Set and Test APIs intentionally not executed against hardware.")
print()
print("Disconnecting...")

cam.disconnect()

print("Disconnected.")
