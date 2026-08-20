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
print("Push Subscribe Get")
print("=" * 60)
try:
    get_res = cam.push_subscribe.get()
    print("Push Subscription Event Categories Configured:")
    print(f"Categories: {list(get_res.keys())}")
    print("\nHardware and Exception Alarms:")
    pprint.pprint({
        "HddAlarm": get_res.get("HddAlarm"),
        "FansAbnormalAlarm": get_res.get("FansAbnormalAlarm"),
        "IOAlarm_channels": len(get_res.get("IOAlarm", {}).get("ChnFlags", [])),
        "MotionAlarm_channels": len(get_res.get("MotionAlarm", {}).get("ChnFlags", [])),
        "PIRAlarm_channels": len(get_res.get("PIRAlarm", {}).get("ChnFlags", [])),
        "VideoLoss_channels": len(get_res.get("VideoLoss", {}).get("ChnFlags", [])),
    }, sort_dicts=False)
    print("\nAI Target Subscriptions:")
    pprint.pprint({
        "FaceAlarm_groups": [g.get("Name") for g in get_res.get("FaceAlarm", {}).get("Group", [])],
        "LPRAlarm_groups": [g.get("Name") for g in get_res.get("LPRAlarm", {}).get("Group", [])],
        "Human_channels": len(get_res.get("Human", {}).get("ChnFlags", [])),
        "Vehicle_channels": len(get_res.get("Vehicle", {}).get("ChnFlags", [])),
    }, sort_dicts=False)
except OptierSDKError as exc:
    print(f"PushSubscribe Get error: {exc}")

print()
print("Disconnecting...")

cam.disconnect()

print("Disconnected.")
