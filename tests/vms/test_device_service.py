from pathlib import Path
import pprint
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(PROJECT_ROOT))

from optier_vms.domain import ConnectionState, DeviceType
from optier_vms.services import DeviceService

from tests.fixtures.test_config import (
    HOST,
    USERNAME,
    PASSWORD,
)

print("=" * 65)
print("OPTIER VMS - Multi-Device Service Live Hardware Test")
print("=" * 65)

service = DeviceService()

# 1. Register Primary Hardware Device
print("1. Registering Primary NVR Device...")
nvr_dev = service.add_device(
    name="Enterprise Main NVR",
    host=HOST,
    username=USERNAME,
    password=PASSWORD,
    device_type=DeviceType.NVR,
    auto_connect=False,
)
print(f"Registered Device: ID={nvr_dev.id} | Name='{nvr_dev.name}' | State={nvr_dev.state}")

# 2. Register Simulated Offline / Unreachable Device for Fault Tolerance Test
print("\n2. Registering Secondary Standalone IPC (Unreachable for Fault Test)...")
offline_dev = service.add_device(
    name="Perimeter IPC (Offline Test)",
    host="192.168.254.254",
    username="admin",
    password="invalid_password",
    device_type=DeviceType.IPC,
    auto_connect=False,
)
print(f"Registered Secondary Device: ID={offline_dev.id} | State={offline_dev.state}")

# 3. Connect Primary Device to Real Hardware
print("\n3. Connecting Primary NVR to Live Hardware...")
connected = service.connect_device(nvr_dev.id)
print(f"Connection Result: {connected} | Final State: {nvr_dev.state}")

print("\n--- Synchronized Hardware Telemetry ---")
print(f"Model: {nvr_dev.info.model}")
print(f"Serial Number: {nvr_dev.info.serial_number}")
print(f"Firmware Version: {nvr_dev.info.firmware_version}")
print(f"Hardware Version: {nvr_dev.info.hardware_version}")
print(f"MAC Address: {nvr_dev.info.mac_address}")
print(f"Hardware Channel Capacity: {nvr_dev.info.channel_capacity}")
print(f"Discovered Logical Channels: {len(nvr_dev.channels)}")
print(f"Online Channels: {nvr_dev.online_channel_count}")

# 4. Verify Channel Retrieval
sample_ch1 = service.get_channel(nvr_dev.id, 1)
if sample_ch1:
    print(f"\nChannel 1 Status: Name='{sample_ch1.name}' | Key={sample_ch1.channel_key} | Status={sample_ch1.current_status}")
    print(f"AI Capabilities: {[cap.value for cap in sample_ch1.ai_capabilities]}")

# 5. Fault Isolation Test on Secondary Offline Device
print("\n5. Testing Fault Isolation with Unreachable Device...")
sec_connected = service.connect_device(offline_dev.id)
print(f"Secondary Connection Result: {sec_connected} | Secondary State: {offline_dev.state}")
print(f"Secondary Error Message: {offline_dev.error_message}")

# Crucial Verification: Primary device MUST remain ONLINE!
print(f"\nVerifying Primary Device State: {nvr_dev.state} (MUST BE ONLINE)")
assert nvr_dev.state == ConnectionState.ONLINE, "Primary device was affected by secondary failure!"

# 6. Heartbeat Health Check
print("\n6. Running Heartbeat Health Check on Primary Device...")
healthy = service.health_check(nvr_dev.id)
print(f"Health Check Passed: {healthy} | State: {nvr_dev.state}")

# 7. List All Managed Channels across the VMS
all_channels = service.list_all_channels()
print(f"\n7. Total Managed Channels Across Enterprise VMS: {len(all_channels)}")

# 8. Graceful Disconnect
print("\n8. Gracefully Disconnecting Devices...")
service.disconnect_device(nvr_dev.id)
print(f"Primary Device State after Disconnect: {nvr_dev.state}")

print("\n" + "=" * 65)
print("VMS Multi-Device Service Verification COMPLETE!")
print("=" * 65)
