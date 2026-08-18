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
print("IPChannel Range")
print("=" * 60)
try:
    rng = cam.ip_channel.range()
    summary = {
        "channel_max": rng.get("channel_max"),
        "operation_type": rng.get("operation_type"),
        "default_password": rng.get("default_password"),
        "batch_modify_password": rng.get("batch_modify_password"),
        "restore_channel_connect": rng.get("restore_channel_connect"),
        "auto_add_ipc": rng.get("auto_add_ipc"),
        "poe_replace_ipc": rng.get("poe_replace_ipc"),
        "IpcListExportBtn": rng.get("IpcListExportBtn"),
    }
    pprint.pprint(summary, sort_dicts=False)
except OptierSDKError as exc:
    print(f"IPChannel Range error: {exc}")

print()
print("=" * 60)
print("IPChannel Get")
print("=" * 60)
try:
    cfg = cam.ip_channel.get()
    channel_info = cfg.get("channel_info", {})
    online_count = sum(1 for ch in channel_info.values() if ch.get("state") == "Online")
    offline_count = sum(1 for ch in channel_info.values() if ch.get("state") == "Offline")
    not_configured_count = sum(1 for ch in channel_info.values() if ch.get("state") == "NotConfigured")

    print(f"Total Channels: {len(channel_info)}")
    print(f"Online Channels: {online_count}")
    print(f"Offline Channels: {offline_count}")
    print(f"Not Configured Channels: {not_configured_count}")
    print(f"Bind Channel: {cfg.get('bind_channel')}")
    print(f"Auto Add IPC Check: {cfg.get('auto_add_ipc_hasCheck')}")
    print()

    print("Sample Configured Channels:")
    configured_samples = {
        k: mask_sensitive(v)
        for k, v in channel_info.items()
        if v.get("state") in ("Online", "Offline")
    }
    for ch_name, ch_data in list(configured_samples.items())[:5]:
        print(f"\n[{ch_name}]")
        pprint.pprint(ch_data, sort_dicts=False)

except OptierSDKError as exc:
    print(f"IPChannel Get error: {exc}")

print()
print("Note: Set API intentionally not executed against hardware.")
print()
print("Disconnecting...")

cam.disconnect()

print("Disconnected.")
