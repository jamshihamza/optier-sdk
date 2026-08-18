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
| Network Email | ✅ | Range/Get verified on real hardware; Set/Test implemented |
| Network FTP | ✅ | Range/Get verified on real hardware; Set/Test implemented |
| Network DDNS | ✅ | Range/Get verified on real hardware; Set/Test implemented |
| Network HTTPS | ✅ | Range/Get verified on real hardware; Set implemented |
| Network RTSP | ⚠️ | Implemented per OEM spec (IPC-specific; NVR returns "not_found") |
| Network SNMP | ✅ | Range/Get verified on real hardware; Set implemented |
| Network IEEE8021x | ⚠️ | Implemented per OEM spec (returns "not_found" on NVR) |
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
| Face Detection | ✅ | Range/Get across page_types verified; Set implemented |
| Pedestrian Detection | ✅ | Range/Get across page_types verified; Set implemented |
| Cross Counting | ✅ | Range/Get across page_types verified; Set implemented |
| Stationary Object Detection | ✅ | Range/Get across page_types verified; Set implemented |
| Sound Detection | ✅ | Range/Get across page_types verified; Set implemented |
| IO Alarm | ✅ | Range/Get & alarm_in filter verified; Set implemented |
| Disarming | ✅ | Range/Get verified on real hardware; Set implemented |
| PTZ Linkage | ✅ | Range/Get & channel filter verified; Set implemented |
| Intelligent Analysis | ✅ | Range/Get, page_type & search query verified; Set implemented |
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

#### Face Detection
- Status: Implemented
- Range: Verified on real hardware across page_types
- Get: Verified on real hardware across page_types
- page_type=AlarmConfig: Verified (agreed_to_agreement=True, statement_file_name='agreement_face', NVR alarm linkages, support_copy=True)
- page_type=ChannelConfig: Verified (channel_max=256)
- page_type=AllConfig / Empty: Device returns param_error (page_type required, AlarmConfig or ChannelConfig)
- NVR channel_max: 256
- 7 configured channels observed with active alarm linkages (CH1, CH2, CH3, CH4, CH5, CH11, CH31)
- 249 unconfigured channels return 'Not configured'
- Set: Implemented, not hardware-tested
- No face detection agreements, switches, or alarm linkages were modified

#### Pedestrian Detection
- Status: Implemented
- Range: Verified on real hardware across page_types
- Get: Verified on real hardware across page_types
- page_type=AlarmConfig: Verified (channel_max=256, support_copy=True)
- page_type=ChannelConfig: Verified (channel_max=256)
- page_type=AllConfig / Empty: Device returns param_error (page_type required, AlarmConfig or ChannelConfig)
- NVR channel_max: 256
- Get returns 'Not configured' across unconfigured channels
- Set: Implemented, not hardware-tested
- No pedestrian humanoid detection rules, AI filters, or alarm linkages were modified

#### Cross Counting
- Status: Implemented
- Range: Verified on real hardware across page_types
- Get: Verified on real hardware across page_types
- page_type=AlarmConfig: Verified (channel_max=256, support_copy=True)
- page_type=ChannelConfig: Verified (channel_max=256)
- page_type=AllConfig / Empty: Device returns param_error (page_type required, AlarmConfig or ChannelConfig)
- NVR channel_max: 256
- Get returns 'Not configured' across unconfigured channels
- Set: Implemented, not hardware-tested
- No cross counting statistic rules, thresholds, or alarm linkages were modified

#### Stationary Object Detection
- Status: Implemented
- Range: Verified on real hardware across page_types
- Get: Verified on real hardware across page_types
- page_type=AlarmConfig: Verified (channel_max=256, support_copy=True, NVR alarm linkages)
- page_type=ChannelConfig: Verified (channel_max=256, sensitivity range [1..4], iva_lines, 4 rules per channel with 8-point polygon coordinate support [x1..x8, y1..y8], PTZ operation support on CH3)
- page_type=AllConfig / Empty: Device returns param_error (page_type required, AlarmConfig or ChannelConfig)
- NVR channel_max: 256
- 7 configured channels observed with active alarm linkages and rule configurations (CH1, CH2, CH3, CH4, CH5, CH11, CH31)
- 249 unconfigured channels return 'Not configured'
- Set: Implemented, not hardware-tested
- No stationary object rules, polygons, sensitivity, or alarm linkages were modified

#### Sound Detection
- Status: Implemented
- Range: Verified on real hardware across page_types
- Get: Verified on real hardware across page_types
- page_type=AlarmConfig: Verified (channel_max=256, support_copy=True, NVR alarm linkages)
- page_type=ChannelConfig: Verified (channel_max=256, rise_switch, rise_sensitivity [1..100], decline_switch, decline_sensitivity [1..100], sound_intensity [1..100], time_schedule)
- page_type=AllConfig / Empty: Device returns param_error (page_type required, AlarmConfig or ChannelConfig)
- NVR channel_max: 256
- 7 configured channels observed with active sound detection configurations and alarm linkages (CH1, CH3, CH4, CH5, CH6, CH11, CH31)
- 249 unconfigured channels return 'Not configured'
- Set: Implemented, not hardware-tested
- No sound detection thresholds, switches, schedules, or alarm linkages were modified

#### IO Alarm
- Status: Implemented
- Range: Verified on real hardware (channel_max=256, support_copy=True)
- Get: Verified on real hardware
- 22 active alarm input ports discovered and verified: 16 physical local alarm inputs (Local<-1..Local<-16) + 6 digital IPC alarm inputs (IP_CH1<-1, IP_CH3<-1, IP_CH5<-1, IP_CH6<-1, IP_CH11<-1, IP_CH31<-1)
- Telemetry observed: alarm_type (NormallyOpen, NormallyClose, Off), buzzer, latch_time, post_recording, alarm_out, channel recording linkage arrays, email, FTP, cloud push
- Targeted alarm_in filtering verified
- Set: Implemented, not hardware-tested
- No physical or digital IO alarm configurations or linkages were modified

#### Disarming
- Status: Implemented
- Range: Verified on real hardware (support_copy=True)
- Get: Verified on real hardware
- Global one-key disarm configuration verified: disarming=False
- Disarm action linkage suppression verified: buzzer, alarm_out, show_message, send_email, full_screen, voice_prompts, event_push_platform, mobile_push
- 256 disarming channels and 7-day weekly half-hour disarming schedules verified
- Set: Implemented, not hardware-tested
- No disarming switches, linkage actions, or schedules were modified

#### PTZ Linkage
- Status: Implemented
- Range: Verified on real hardware (channel_max=256, support_copy=True, ptz_info max_size=256)
- Get: Verified on real hardware
- 36 configured channels verified with full alarm trigger linkage mapping: motion, pir, io, linkage_sod, linkage_cc, linkage_sound, linkage_vt, linkage_fd, linkage_ad, linkage_cd, linkage_qd, linkage_lpd, linkage_rsd, linkage_lpr, linkage_fr, linkage_ai_pid, linkage_ai_lcd, linkage_ai_pdvd, linkage_ai_firedetet, linkage_ai_tempmeas, linkage_intrusion, linkage_region_entrance, linkage_region_exiting
- 4 PTZ linkage preset points per channel (ptz_chn, linkage_ptz_point_index [0..255], ptz_switch)
- Targeted channel filtering verified
- Set: Implemented, not hardware-tested
- No PTZ preset linkage mappings or triggers were modified

#### Intelligent Analysis
- Status: Implemented
- Range: Verified on real hardware (channel_max=256, page_type="ChannelConfig")
- Get: Verified on real hardware
- Statistical counting report parameters documented and supported: report_type (Daily report [24h], Weekly report [7d], Monthly report [31d], Annual report [12m]), cross_type (Number of in, Number of out), detection_type (Motion, Person, Vehicle, Non-motorized Vehicle), ai_cross_count, search_date
- Unconfigured channels return 'Not configured' (statistical counting inactive)
- Targeted channel filtering and search query payload structures verified
- Set: Implemented, not hardware-tested
- No statistical analytics configurations were modified

#### Network Email
- Status: Implemented
- Range: Verified on real hardware
- Get: Verified on real hardware
- Configuration parameters verified: email_enable, encryption (Disable, SSL, TLS, Auto), smtp_port (1..65535, default 25), smtp_server, username, password, password_empty, sender, recvemail (recvemail_1..3), interval_time (1, 3, 5, 10 min), test_version (2.0)
- Set: Implemented, not hardware-tested
- Test: Implemented, not hardware-tested
- No SMTP credentials or email delivery configurations were modified

#### Network FTP
- Status: Implemented
- Range: Verified on real hardware (ftp_test=True)
- Get: Verified on real hardware
- Configuration parameters verified: ftp_enable, server_ip, port (1..65535, default 21), username, password, password_empty, picture_quality (Highest, Higher, Medium, Low, Lower, Lowest), video_stream_type (Mainstream, Substream), max_package_interval (10, 20, 30, 45, 60 min), directory_name (max 95 chars)
- Set: Implemented, not hardware-tested
- Test: Implemented, not hardware-tested
- No FTP credentials or upload configurations were modified

#### Network DDNS
- Status: Implemented
- Range: Verified on real hardware
- Get: Verified on real hardware
- Configuration parameters verified: ddns_enable, server (DYNDNS, NO_IP, CHANGEIP, DNSEXIT), domain (max 35 chars), username, password (max 32 chars), api_key (max 32 chars), password_empty, api_key_empty, test_befault_save, api_key_url (https://dnsexit.com), server_content & ddns_v1 provider profiles
- Set: Implemented, not hardware-tested
- Test: Implemented, not hardware-tested
- No DDNS service credentials, host mappings, or resolution switches were modified

#### Network HTTPS
- Status: Implemented
- Range: Verified on real hardware (URI: POST /API/NetworkConfig/https/Range)
- Get: Verified on real hardware (URI: POST /API/NetworkConfig/https/Get)
- Configuration parameters verified: https_enable (True), file_type (Default, Custom), file_exist (0, 1), ca_file (0..10240 bytes), key_file (0..10240 bytes), root_ca_file (0..10240 bytes), operate (Install, Uninstall, Switch)
- Set: Implemented, not hardware-tested
- No SSL certificates, private keys, or TLS modes were modified

#### Network RTSP
- Status: Implemented
- Range: Tested against hardware (URI: POST /API/NetworkConfig/Rtsp/Range) — Device returned error_code "not_found"
- Get: Tested against hardware (URI: POST /API/NetworkConfig/Rtsp/Get) — Device returned error_code "not_found"
- OEM Documented Note: "note:(DVR/NVR not supported)" explicitly confirmed on hardware
- NVR Channel RTSP URLs: Provided via Channel RtspUrl API (/API/Channel/RtspUrl/Get) and managed by RtspUrlManager (cam.rtsp_url)
- Set: Implemented, not hardware-tested

#### Network SNMP
- Status: Implemented
- Range: Verified on real hardware
- Get: Verified on real hardware
- Configuration parameters verified: snmp_enable (True), snmp_versions (V1, V2, V1,V2, V3; active: V1), snmp_port (1..65535, active 161), read_community (Pub-Group), write_community (Pte-Group), trap_ipaddr (127.0.0.1), trap_port (162), authentication (readonly_user, readwrite_user with MD5/SHA authentication and CBC-DES encryption)
- Set: Implemented, not hardware-tested
- No SNMP credentials, community names, or trap targets were modified

#### Network IEEE8021x
- Status: Implemented
- Range: Tested against hardware (URI: POST /API/NetworkConfig/IEEE8021x/Range) — Device returned error_code "not_found"
- Get: Tested against hardware (URI: POST /API/NetworkConfig/IEEE8021x/Get) — Device returned error_code "not_found"
- Note: Hardware endpoint explicitly tested on an NVR. Like RTSP, IEEE8021x is often IPC-specific on these OEM devices.
- Set: Implemented per OEM documentation schemas, but intentionally not hardware-tested.

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