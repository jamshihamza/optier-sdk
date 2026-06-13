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

info = cam.system_info.get()

print("=" * 60)
print("System Information")
print("=" * 60)

print(f"Device ID          : {info.device_id}")
print(f"Device Name        : {info.device_name}")
print(f"Device Type        : {info.device_type}")
print(f"Hardware Version   : {info.hardware_version}")
print(f"Software Version   : {info.software_version}")
print(f"Build Time         : {info.build_time}")
print(f"IE Client Version  : {info.ie_client_version}")

print()
print("=" * 60)
print("Raw OEM Values")
print("=" * 60)

for key, value in info.raw.items():
    print(f"{key:25}: {value}")

print()
print("Disconnecting...")
cam.disconnect()

print("Disconnected.")