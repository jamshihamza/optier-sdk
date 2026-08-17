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

for pt in [None, "ChannelConfig"]:
    label = f"page_type={pt!r}"
    print("=" * 60)
    print(f"Intelligent Analysis Range ({label})")
    print("=" * 60)
    try:
        rng = cam.intelligent_analysis.range(page_type=pt)
        metadata = {k: v for k, v in rng.items() if k != "channel_info"}
        pprint.pprint(metadata, sort_dicts=False)
        ch_info = rng.get("channel_info", {})
        if isinstance(ch_info, dict):
            items = ch_info.get("items", {})
            print(f"Total Range channels: {len(items)}")
    except OptierSDKError as exc:
        print(f"Intelligent Analysis Range ({label}) error: {exc}")
    print()

for ch_filter in [None, ["CH1", "CH3"]]:
    label = f"channels={ch_filter!r}"
    print("=" * 60)
    print(f"Intelligent Analysis Get ({label})")
    print("=" * 60)
    try:
        cfg = cam.intelligent_analysis.get(channels=ch_filter)
        ch_info = cfg.get("channel_info", {})
        print(f"Total returned channels: {len(ch_info)}")
        configured_channels = {
            k: v for k, v in ch_info.items()
            if isinstance(v, dict) and "reason" not in v
        }
        unconfigured_channels = [
            k for k, v in ch_info.items()
            if isinstance(v, dict) and v.get("reason") == "Not configured"
        ]
        print(f"Configured statistical reporting channels ({len(configured_channels)}): {list(configured_channels.keys())}")
        print(f"Unconfigured channels count: {len(unconfigured_channels)}")
    except OptierSDKError as exc:
        print(f"Intelligent Analysis Get ({label}) error: {exc}")
    print()

print("=" * 60)
print("Intelligent Analysis Get (Search Query)")
print("=" * 60)
try:
    search_query = {
        "CH1": {
            "report_type": "Daily report",
            "cross_type": "Number of in",
            "detection_type": "Person",
            "search_date": "2026-08-17",
        }
    }
    cfg = cam.intelligent_analysis.get(channel_info=search_query)
    ch_info = cfg.get("channel_info", {})
    print(f"Search query returned channels: {len(ch_info)}")
    print(f"CH1 response: {ch_info.get('CH1')}")
except OptierSDKError as exc:
    print(f"Intelligent Analysis Search Query error: {exc}")

print()
print("Note: Set API intentionally not executed against hardware.")
print()
print("Disconnecting...")

cam.disconnect()

print("Disconnected.")
