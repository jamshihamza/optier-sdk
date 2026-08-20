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
print("Maintenance Developer Mode Range")
print("=" * 60)
try:
    range_res = cam.developer_mode.range()
    print("Developer Mode Range Summary:")
    print(f"SSH switch supported: {range_res.get('ssh_switch')}")
    print(f"Export disk switch options: {range_res.get('export_disk_switch', {}).get('items')}")
    print(f"Export days options: {range_res.get('export_days', {}).get('items')}")
    print(f"Enable export button: {range_res.get('enable_export')}")
    print(f"Enable delete button: {range_res.get('enable_delete')}")
    print(f"Support IPC log export: {range_res.get('support_ipc_log_export')}")
    print(f"Support IPC log delete: {range_res.get('support_ipc_log_delete')}")
    print(f"Default timeout: {range_res.get('default_timeout')} ms")
    channels = list(range_res.get("channel_info", {}).get("items", {}).keys())
    print(f"Channel log collection slots: {len(channels)} (first 5: {channels[:5]})")
except OptierSDKError as exc:
    print(f"DeveloperMode Range error: {exc}")

print()
print("=" * 60)
print("Maintenance Developer Mode Get")
print("=" * 60)
try:
    get_res = cam.developer_mode.get()
    print("Developer Mode Current Configuration:")
    pprint.pprint({
        "ssh_switch": get_res.get("ssh_switch"),
        "export_disk_switch": get_res.get("export_disk_switch"),
        "debug_info_level": get_res.get("debug_info_level"),
        "enable_export": get_res.get("enable_export"),
        "enable_delete": get_res.get("enable_delete"),
        "support_ipc_log_export": get_res.get("support_ipc_log_export"),
        "support_ipc_log_delete": get_res.get("support_ipc_log_delete"),
        "channel_count": len(get_res.get("channel_info", {})),
    }, sort_dicts=False)
except OptierSDKError as exc:
    print(f"DeveloperMode Get error: {exc}")

print()
print("Disconnecting...")

cam.disconnect()

print("Disconnected.")
