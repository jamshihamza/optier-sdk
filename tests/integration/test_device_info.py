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

        POST /API/Login/DeviceInfo/Get
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

        info = cam.login.device_info()

        print("=" * 60)
        print("Device Information")
        print("=" * 60)

        print(f"Device Type                 : {info.device_type}")
        print(f"Channel Count               : {info.channel_num}")
        print(f"Analog Channel Count        : {info.analog_channel_num}")
        print(f"MAC Address                 : {info.mac_addr}")
        print(f"Preview Count               : {info.preview_num}")

        print()

        print(f"Face Config                 : {info.support_face_config}")
        print(
            f"Human Vehicle Search        : "
            f"{info.support_human_vehicle_search}"
        )

        print(f"Heat Map                    : {info.support_heat_map}")

        print(f"AI Cross Count              : {info.support_ai_cc}")

        print(
            f"Repeat Visitor              : "
            f"{info.support_repeat_visitor}"
        )

        print(
            f"Face Attendance             : "
            f"{info.support_face_attendance}"
        )

        print()

        print("=" * 60)
        print("Raw OEM Values")
        print("=" * 60)

        print("support_ai =", info.get("support_ai"))

        print(
            "support_hls_server =",
            info.get("support_hls_server"),
        )

        print(
            "support_license_plate =",
            info.get("support_license_plate"),
        )

        print()

        print("Test completed successfully.")

    finally:

        print()

        print("Disconnecting...")

        cam.disconnect()

        print("Disconnected.")


if __name__ == "__main__":
    main()