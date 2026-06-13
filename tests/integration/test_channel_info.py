

from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[2]

sys.path.insert(0, str(PROJECT_ROOT))
from optier_sdk import Camera

from tests.fixtures.test_config import (
    HOST,
    USERNAME,
    PASSWORD,
)


def main() -> None:
    """
    Integration test for:

        POST /API/Login/ChannelInfo/Get
    """

    cam = Camera(
        host=HOST,
        username=USERNAME,
        password=PASSWORD,
    )

    try:
        print("=" * 60)
        print("Connecting...")
        print("=" * 60)

        cam.connect()

        print("Connected successfully.\n")

        channels = cam.login.channel_info()

        print("=" * 60)
        print(f"Total Channels : {len(channels)}")
        print("=" * 60)

        for index, ch in enumerate(
            channels,
            start=1,
        ):

            print()

            print("-" * 60)

            print(f"Index              : {index}")

            print(f"Channel            : {ch.channel}")

            print(f"Channel Name       : {ch.channel_name}")

            print(f"Channel Alias      : {ch.channel_alias}")

            print(f"Connect Status     : {ch.connect_status}")

            print(f"Video Loss         : {ch.videoloss}")

            print(f"Alarm In           : {ch.alarm_in_num}")

            print(f"Alarm Out          : {ch.alarm_out_num}")

            print(f"Abilities          :")

            for item in ch.ability:
                print(f"   - {item}")

            print()

            print("Intelligent Ability:")

            for item in ch.intelligent_ability:
                print(f"   - {item}")

            print()

            print("Talk Audio Ability:")

            for item in ch.talk_audio_ability:
                print(f"   - {item}")

            print()

            print(
                f"Wireless IPC Type  : "
                f"{ch.wireless_ipc_type}"
            )

        print()

        print("=" * 60)
        print("ChannelInfo test completed successfully.")
        print("=" * 60)

    finally:

        print()

        print("Disconnecting...")

        cam.disconnect()

        print("Disconnected.")


if __name__ == "__main__":
    main()