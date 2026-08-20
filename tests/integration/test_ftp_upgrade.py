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
print("Maintenance FtpUpgrade Range")
print("=" * 60)
try:
    range_res = cam.ftp_upgrade.range()
    print("FTP / Online Upgrade Range Summary:")
    print(f"FTP server address limits: {range_res.get('ftp_addr')}")
    print(f"FTP port range: {range_res.get('ftp_port')}")
    print(f"Username limits: {range_res.get('username')}")
    print(f"Password limits: {range_res.get('user_pwd')}")
    print(f"Online upgrade tips: {range_res.get('online_upgrade_tips', {}).get('items')}")
    print(f"Support online upgrade edit: {range_res.get('support_onlineupgrade_edit')}")
    print(f"FTP path limits: {range_res.get('ftp_path')}")
    print(f"Supported buttons: {range_res.get('ftp_buttons', {}).get('items')}")
except OptierSDKError as exc:
    print(f"FtpUpgrade Range error: {exc}")

print()
print("=" * 60)
print("Maintenance FtpUpgrade Get")
print("=" * 60)
try:
    get_res = cam.ftp_upgrade.get()
    print("FTP / Online Upgrade Current Configuration:")
    pprint.pprint({
        "ftp_addr": get_res.get("ftp_addr"),
        "ftp_port": get_res.get("ftp_port"),
        "username": get_res.get("username"),
        "user_pwd_empty": get_res.get("user_pwd_empty"),
        "ftp_path": get_res.get("ftp_path"),
        "check_for_updates": get_res.get("check_for_updates"),
        "online_upgrade": get_res.get("online_upgrade"),
        "Upgrade_button": get_res.get("Upgrade_button"),
    }, sort_dicts=False)
except OptierSDKError as exc:
    print(f"FtpUpgrade Get error: {exc}")

print()
print("Disconnecting...")

cam.disconnect()

print("Disconnected.")
