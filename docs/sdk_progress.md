# OPTIER SDK Progress

| Module | Tested | Status |
|---------|--------|--------|
| Login | ✅ | Complete |
| DeviceInfo | ✅ | Complete |
| ChannelInfo | ✅ | Complete |
| Snapshot | ✅ | Complete |
| DateTime | ✅ | Complete |
| Log | ✅ | Complete |
| SystemInfo | ✅ | Complete |
| NTP | ✅ | Complete |
| General | ✅ | Complete |
| Network State | ✅ | Complete |
| Network Base | ✅ | Range/Get & page_type verified; Set implemented |
| Network ONVIF | ✅ | Range/Get verified on real hardware; Set implemented |
| Network IP Filter | ✅ | Range/Get verified on real hardware; Set implemented |
| Record Information | ✅ | Complete |
| Record Configuration | ✅ | Range/Get verified on real hardware; Set implemented |
| Disk | ✅ | Range/Get verified on real hardware; Set/Control/Format implemented |
| DST | ✅ | Range/Get verified on real hardware, Set implemented but not hardware-tested |
| Auto Reboot | ✅ | Range/Get verified on real hardware, Set implemented but not hardware-tested |
| Stream Encode | ✅ | MainStream, SubStream, MobileStream verified; EventStream unsupported; Set implemented |
| Video Color | ✅ | Range/Get verified on real hardware; Set/Default implemented |
| OSD | ✅ | Range/Get verified on real hardware; Set implemented |
| Image Control | ✅ | Range/Get verified on real hardware; Set/Default implemented |
| Video Cover | ✅ | Range/Get verified on real hardware; Set implemented |
| Motion Alarm | ✅ | Range/Get across page_types verified; Set implemented |
| Exception Alarm | ✅ | Range/Get verified on real hardware; Set implemented |
| Line Crossing Detection | ✅ | Range/Get across page_types verified; Set implemented |
| Perimeter Intrusion Detection | ✅ | Range/Get across page_types verified; Set implemented |
| Occlusion Detection | ✅ | Range/Get across page_types verified; Set implemented |
| DefoggingFan | ❌ | Skipped (device returned "not_found") |

---

### Module Details

#### DST
- Status: Implemented
- Range/Get: Verified on real hardware
- Set: Implemented (not hardware-tested to prevent modifying device configuration)

#### Auto Reboot
- Status: Implemented
- Range/Get: Verified on real hardware
- Set: Implemented (not hardware-tested to prevent modifying device configuration)

#### Stream Encode
- Status: Implemented
- MainStream: Range/Get verified on real hardware
- SubStream: Range/Get verified on real hardware
- MobileStream: Range/Get verified on real hardware
- EventStream: Device returned error_code "not_found"
- Set: Implemented (not hardware-tested to prevent modifying device configuration)

#### Video Color
- Status: Implemented
- Range: Verified on real hardware
- Get: Verified on real hardware
- Set: Implemented (not hardware-tested to prevent modifying device configuration)
- Default: Implemented (not hardware-tested to prevent modifying device configuration)
- IPC/NVR channel structures verified
- No unsupported items on tested hardware

#### OSD
- Status: Implemented
- Range: Verified on real hardware
- Get: Verified on real hardware
- Set: Implemented (not hardware-tested to prevent modifying device configuration)
- IPC/NVR channel structures verified
- Unconfigured NVR channels return "Not configured"
- No unsupported core OSD operations on the tested hardware

#### Image Control
- Status: Implemented
- Range: Verified on real hardware
- Get: Verified on real hardware
- Heterogeneous NVR channel capabilities verified
- Standard optical/image controls verified
- PTZ/motorized optical parameters observed
- TimeSchedule day/night mode observed
- Smart illumination/full-color capability observed
- Defog controls observed
- Offline channel handling verified
- Set: Implemented (not hardware-tested to prevent modifying camera sensor configurations)
- Default: Implemented (not hardware-tested to prevent modifying camera sensor configurations)
- No unsupported core Range/Get operations on the tested hardware

#### Video Cover
- Status: Implemented
- Range: Verified on real hardware
- Get: Verified on real hardware
- NVR channel_max: 256
- support_copy: True
- Privacy zone configuration observed
- Standard channels returned rectangular zone information
- PTZ channel-specific privacy-zone information observed
- Configured privacy zone observed on CH11
- Unconfigured channels returned "Not configured"
- Set: Implemented, not hardware-tested
- No privacy-mask configuration was modified during validation

#### Motion Alarm
- Status: Implemented
- Range: Verified on real hardware
- Get: Verified on real hardware
- page_type=AlarmConfig: Verified
- page_type=ChannelConfig: Verified
- page_type=AllConfig: Verified
- Empty data payload: Device returns param_error; page_type is required
- NVR channel_max: 256
- support_copy: True
- 36 configured channels observed on the tested device
- Motion grid: mbrow=30, mbcol=44
- camera_smd / target_type observed
- Sensitivity differences observed between channels
- Alarm linkage configuration observed
- Set: Implemented, not hardware-tested
- No motion regions, sensitivity, schedules, or alarm linkages were modified

#### Exception Alarm
- Status: Implemented
- Range: Verified on real hardware
- Get: Verified on real hardware
- NVR channel_max: 256
- Discovered and verified 4 hardware exception types: video_loss, disk_error, no_space_on_disk, fan_abnormal
- Exception switches and buzzer/email/message linkage telemetry observed
- Fan abnormal alarm configured with 60s buzzer linkage
- Set: Implemented, not hardware-tested
- No exception alarm configurations or linkages were modified

#### Line Crossing Detection
- Status: Implemented
- Range: Verified on real hardware across page_types
- Get: Verified on real hardware across page_types
- page_type=AlarmConfig: Verified (NVR alarm linkages and support_copy=True)
- page_type=ChannelConfig: Verified (AI detection_type, rule_info with 4 rules, PTZ operation support on CH3)
- page_type=AllConfig / Empty: Device returns param_error (page_type required, AlarmConfig or ChannelConfig)
- NVR channel_max: 256
- AI classification targets supported: Pedestrian, Motor Vehicle, Non-motorized Vehicle
- Rule directions supported: A->B, B->A, A<-->B
- Coordinate limits: x1 [0..704], y1 [0..576], x2 [0..704], y2 [0..576]
- Get returns 'Not configured' across unconfigured channels
- Set: Implemented, not hardware-tested
- No tripwires, AI filters, or alarm linkages were modified

#### Perimeter Intrusion Detection
- Status: Implemented
- Range: Verified on real hardware across page_types
- Get: Verified on real hardware across page_types
- page_type=AlarmConfig: Verified (channel_max=256, support_copy=True)
- page_type=ChannelConfig: Verified (channel_max=256)
- page_type=AllConfig / Empty: Device returns param_error (page_type required, AlarmConfig or ChannelConfig)
- NVR channel_max: 256
- Get returns 'Not configured' across unconfigured channels
- Set: Implemented, not hardware-tested
- No intrusion zones, AI filters, or alarm linkages were modified

#### Occlusion Detection
- Status: Implemented
- Range: Verified on real hardware across page_types
- Get: Verified on real hardware across page_types
- page_type=AlarmConfig: Verified (NVR alarm linkages, voice prompts, and support_copy=True)
- page_type=ChannelConfig: Verified (switch toggle, sensitivity [1..6])
- page_type=AllConfig / Empty: Device returns param_error (page_type required, AlarmConfig or ChannelConfig)
- NVR channel_max: 256
- 7 configured channels observed with active alarm linkages and sensitivity settings (CH1, CH2, CH3, CH4, CH5, CH11, CH31)
- 220 unconfigured channels return 'Not configured'
- Set: Implemented, not hardware-tested
- No occlusion switches, sensitivity, or alarm linkages were modified

#### Network Base
- Status: Implemented
- Range: Verified on real hardware
- Get: Verified on real hardware
- page_type=net_general: Verified
- NVR dual-NIC / Double Address Mode: Verified
- LAN1/LAN2 configuration: Verified
- Set: Implemented (not hardware-tested to prevent modifying device network interfaces)
- No OEM errors during validation

#### Network ONVIF
- Status: Implemented
- Range: Verified on real hardware
- Get: Verified on real hardware
- Supported authentication modes verified: Digest_sha256, Digest, Digest/WSSE, WSSE
- Supported transport protocols verified: HTTP/HTTPS, HTTPS, HTTP
- Active configuration observed: enable=False, authentication=Digest/WSSE, protocol=HTTP/HTTPS, password_empty=True
- Username and password length constraints: [0..63] when disabled, [1..63] when enabled
- Set: Implemented, not hardware-tested
- No ONVIF credentials, authentication mode, or service switches were modified

#### Network IP Filter
- Status: Implemented
- Range: Verified on real hardware
- Get: Verified on real hardware
- Supported filter modes verified: Whitelist, Blacklist
- Supported IP types verified: Ipv4, Ipv6 (max 64 rules, start/end address length max 64 bytes)
- Active configuration observed: enable=False, choose=Whitelist, restricted_type=Whitelist, whitelist=[], blacklist=[]
- Set: Implemented, not hardware-tested
- No IP firewall rules, blacklist/whitelist ranges, or filter switches were modified

#### Storage Disk
- Status: Implemented
- Range: Verified on real hardware
- Get: Verified on real hardware
- Physical HDD telemetry verified (Seagate 4TB ST4000NM0053)
- Overwrite mode verified (Auto)
- Format progress query verified
- Set: Implemented (not hardware-tested to prevent modifying storage configuration)
- Control: Implemented (not hardware-tested to prevent modifying storage configuration)
- Format: Implemented (not hardware-tested to prevent storage data loss)

#### Record Configuration
- Status: Implemented
- Range: Verified on real hardware
- Get: Verified on real hardware
- NVR multi-channel configuration verified
- channel_max: 256
- support_copy: True
- Mainstream / DualStream verified
- prerecord verified
- anr / network-break recording field observed
- copy_ch verified
- Set: Implemented (not hardware-tested to prevent modifying active recording schedules)
- No recording configuration was modified during validation

#### DefoggingFan
- Status: Skipped / Unsupported on tested firmware
- Result: Device returned error_code "not_found"
- Verified: Yes