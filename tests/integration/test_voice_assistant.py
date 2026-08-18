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
            if any(s in k_lower for s in ("username", "email", "password", "token", "key", "secret")) and isinstance(v, str) and v:
                if "@" in v:
                    parts = v.split("@")
                    clean[k] = parts[0][:2] + "****@" + parts[1]
                else:
                    clean[k] = "******"
            else:
                clean[k] = mask_sensitive(v)
        return clean
    elif isinstance(obj, list):
        return [mask_sensitive(elem) for elem in obj]
    return obj


print("=" * 60)
print("Voice Assistant Range")
print("=" * 60)
try:
    rng = cam.voice_assistant.range()
    pprint.pprint(rng, sort_dicts=False)
except OptierSDKError as exc:
    print(f"Voice Assistant Range error: {exc}")

for assistant in ("Amazon", "Google"):
    print()
    print("=" * 60)
    print(f"Voice Assistant Get ({assistant})")
    print("=" * 60)
    try:
        cfg = cam.voice_assistant.get(smart_home_page=assistant)
        pprint.pprint(mask_sensitive(cfg), sort_dicts=False)
    except OptierSDKError as exc:
        print(f"Voice Assistant Get ({assistant}) error: {exc}")

print()
print("Note: Control/Set API intentionally not executed against hardware.")
print()
print("Disconnecting...")

cam.disconnect()

print("Disconnected.")
