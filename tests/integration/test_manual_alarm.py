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
print("PreviewChannel Manual Alarm Get")
print("=" * 60)
try:
    cfg = cam.manual_alarm.get()
    local_ports = {k: v for k, v in cfg.items() if k.startswith("Local")}
    ip_ports = {k: v for k, v in cfg.items() if k.startswith("IP_CH")}

    print(f"Total Configured Manual Alarm Output Ports: {len(cfg)}")
    print(f"Physical Local Alarm Outputs: {len(local_ports)}")
    print(f"Digital IP Channel Alarm Outputs: {len(ip_ports)}")

    print("\nPhysical Local Alarm Outputs:")
    pprint.pprint(local_ports, sort_dicts=False)

    print("\nDigital IP Channel Alarm Outputs:")
    pprint.pprint(ip_ports, sort_dicts=False)
except OptierSDKError as exc:
    print(f"PreviewChannel Manual Alarm Get error: {exc}")

print()
print("Note: Set API intentionally not executed against hardware.")
print()
print("Disconnecting...")

cam.disconnect()

print("Disconnected.")
