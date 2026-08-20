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
print("Maintenance IPC FTP Upgrade Range")
print("=" * 60)
try:
    range_res = cam.ftp_ipc_upgrade.range()
    print("IPC FTP Upgrade Range Summary:")
    print(f"Channel max: {range_res.get('channel_max')}")
    print(f"Online upgrade supported: {range_res.get('online_upgrade')}")
    print(f"FTP auto upgrade supported: {range_res.get('ftp_auto_upgrade')}")
    print(f"Check for updates supported: {range_res.get('check_for_updates')}")
    print(f"Supported buttons: {range_res.get('ftp_buttons', {}).get('items')}")
    channels = list(range_res.get("channel_info", {}).get("items", {}).keys())
    print(f"IPC FTP upgrade channel slots: {len(channels)} (channels: {channels})")
except OptierSDKError as exc:
    print(f"FtpIPCUpgrade Range error: {exc}")

print()
print("=" * 60)
print("Maintenance IPC FTP Upgrade Get")
print("=" * 60)
try:
    get_res = cam.ftp_ipc_upgrade.get()
    print("IPC FTP Upgrade Current Configuration:")
    pprint.pprint({
        "online_upgrade": get_res.get("online_upgrade"),
        "ftp_auto_upgrade": get_res.get("ftp_auto_upgrade"),
        "check_for_updates": get_res.get("check_for_updates"),
    }, sort_dicts=False)
    channels = get_res.get("channel_info", {})
    print(f"IPC FTP Upgrade Total Channels: {len(channels)}")
    supported = {k: v for k, v in channels.items() if v.get("reason") != "Not support"}
    print(f"Supported / Online Channels ({len(supported)}):")
    pprint.pprint(supported, sort_dicts=False)
except OptierSDKError as exc:
    print(f"FtpIPCUpgrade Get error: {exc}")

print()
print("Disconnecting...")

cam.disconnect()

print("Disconnected.")
