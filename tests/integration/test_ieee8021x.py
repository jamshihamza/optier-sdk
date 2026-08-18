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
print("IEEE8021x Range")
print("=" * 60)
try:
    rng = cam.ieee8021x.range()
    pprint.pprint(rng, sort_dicts=False)
except OptierSDKError as exc:
    print(f"IEEE8021x Range error: {exc}")

print()
print("=" * 60)
print("IEEE8021x Get")
print("=" * 60)
try:
    cfg = cam.ieee8021x.get()

    def sanitize(obj):
        if isinstance(obj, dict):
            clean = {}
            for k, v in obj.items():
                k_lower = k.lower()
                if any(s in k_lower for s in ("password", "secret", "cipher", "peer_key", "cert", "private_key")) and v and not k.endswith("_empty") and "button" not in k_lower:
                    clean[k] = "******"
                else:
                    clean[k] = sanitize(v)
            return clean
        elif isinstance(obj, list):
            return [sanitize(elem) for elem in obj]
        return obj

    pprint.pprint(sanitize(cfg), sort_dicts=False)
except OptierSDKError as exc:
    print(f"IEEE8021x Get error: {exc}")

print()
print("Note: Set API intentionally not executed against hardware.")
print()
print("Disconnecting...")

cam.disconnect()

print("Disconnected.")
