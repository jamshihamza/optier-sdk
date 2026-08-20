# OPTIER SDK Progress

| Module | Tested | Status |
|---------|--------|--------|
| Login | ✅ | Complete |
| Recover Password | ✅ | Range and Get verified across security questions and recovery email limits |
| DeviceInfo | ✅ | Complete |
| ChannelInfo | ✅ | Complete |
| Snapshot | ✅ | Complete |
| DateTime | ✅ | Complete |
| Log | ✅ | Complete |
| SystemInfo | ✅ | Complete |
| NTP | ✅ | Complete |
| General | ✅ | Complete |
| Privacy Statement | ✅ | Range and Get verified on real hardware |
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
| Network IPv6 | ⚠️ | Implemented per OEM spec (returns "not_found" on NVR) |
| Network Voice Assistant | ✅ | Range/Get (Amazon & Google) verified on real hardware; Control/Set implemented |
| Network GBT28181 | ⚠️ | Implemented per OEM spec (returns "not_found" on NVR) |
| Network Tuya | ⚠️ | Implemented per OEM spec (returns "not_found" on NVR) |
| Network WLAN Scan | ⚠️ | Implemented per OEM spec (returns "not_found" on NVR) |
| Channel IPChannel | ✅ | Range/Get across 256 channels verified on real hardware; Set/AutoAddIPC implemented |
| Channel Broadcast IPC | ✅ | Range/Search verified on real hardware; Set implemented |
| Channel PTZ | ✅ | Range/Get across 256 channels verified on real hardware; Set implemented |
| Channel Protocol Manage | ✅ | Range/Get verified on real hardware; Set implemented |
| Channel PTZ Tasks / Schedules | ✅ | Range/Get verified on real hardware; Set implemented |
| Channel ROI | ✅ | Range/Get verified on real hardware across 256 channels; Set implemented |
| Channel Analog Channel | ✅ | Range/Get verified on real hardware (Pure IP mode); Set implemented |
| PreviewChannel | ✅ | Complete (Unified manager unifying PTZ, DualTalk, Floodlight2AudioAlarm, and ManualAlarm) |
| PreviewChannel Manual Alarm | ✅ | Get verified across 10 physical and digital alarm outputs; Set implemented |
| PreviewChannel Floodlight & Audio Alarm | ✅ | Get verified across active deterrence channels (horn & white light floodlight); Set implemented |
| PreviewChannel DualTalk | ⚠️ | Implemented per OEM spec (returns "not_found" on NVR) |
| PreviewChannel PTZ | ✅ | Get & Progress verified on CH3 speed dome and standard channels; Control implemented |
| Record Search Month | ✅ | Get verified across channels, dates, and search types |
| Record Search Record | ✅ | Range and Search verified across channels, dates, and time intervals |
| Record Picture Playback | ✅ | Search and Get verified across channels and snapshot tokens |
| Record Tag | ✅ | Range and Get verified across channels and timeline tags; Set implemented |
| Record Playback Page | ✅ | Range verified across all 8 playback modalities and color bitmasks |
| Record Information | ✅ | Complete |
| Record Configuration | ✅ | Range/Get verified on real hardware; Set implemented |
| Disk | ✅ | Range/Get verified on real hardware; Set/Control/Format implemented |
| Storage Cloud | ✅ | Range and Get verified across cloud providers and overwrite retention policies |
| Maintenance Developer Mode | ✅ | Range and Get verified across SSH toggles, debug outputs, and log retention |
| Maintenance FtpUpgrade | ✅ | Range, Get, and Progress verified across FTP/HTTP online upgrade parameters |
| Maintenance IPC Upgrade | ✅ | Range and Get verified across online IP cameras and firmware versions |
| Push Subscribe | ✅ | Get verified across 28 hardware and AI push event bitmask categories |
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

#### Maintenance IPC Upgrade
- Status: Implemented
- Range: Verified on real hardware (URI: POST /API/IPCMaintaint/IPCUpgrade/Range) — channel_max (256), password limits, 9 upgradeable IPC slots (CH1, CH2, CH3, CH4, CH5, CH6, CH11, CH29, CH31)
- Get: Verified on real hardware (URI: POST /API/IPCMaintaint/IPCUpgrade/Get) — Current telemetry returning all 256 channels, with 9 online IP cameras returning IP addresses, firmware versions (V21.45, V31.35, V40.45), and firmware file extension (.sw)
- Token: Implemented per OEM documentation (URI: POST /API/IPCMaintaint/IPCUpgrade/Token), not hardware-tested
- Upgrade: Implemented per OEM documentation (URI: POST /API/IPCMaintaint/IPCUpgrade/Upgrade), not hardware-tested
- Parameters verified: `channel_info`, `channel_max`, `password`, `file_name`, `file_size`, `ipc_channels`, `upgrade_head`, `upgrade_token`, `state`, `ip_address`, `software_version`, `file_type`

#### Login Recover Password
- Status: Implemented
- Range: Verified on real hardware (URI: POST /API/RecoverPassword/Range) — answer_flag (bool), certificate_flag (bool), super_pwd_flag (bool), questions (3 slots, IDs 1..15), enc_answers (3 slots, 1..64 chars), email (1..64 chars)
- Get: Verified on real hardware (URI: POST /API/RecoverPassword/Get) — Current telemetry (questions: [1, 2, 3])
- Set: Implemented per OEM documentation (URI: POST /API/RecoverPassword/Set), not hardware-tested
- Parameters verified: `questions`, `answers`, `email`, `answer_flag`, `email_flag`, `certificate_flag`, `super_pwd_flag`, `enc_answers`

#### Push Subscribe
- Status: Implemented
- Get: Verified on real hardware (URI: POST /API/PushSubscribe/Get) — Current telemetry returning all 28 alarm push subscription categories: HddAlarm, FansAbnormalAlarm, IOAlarm, MotionAlarm, PIRAlarm, PDAlarm, FDAlarm, ADAlarm, CCAlarm, CDAlarm, QDAlarm, RSDAlarm, LPDAlarm, SODAlarm, VTAlarm, SDAlarm, LCDAlarm, PIDAlarm, TempMeasAlarm, FireDetectionAlarm, IntrusionAlarm, RegionEntranceAlarm, RegionExitingAlarm, Human, Vehicle, VideoLoss, FaceAlarm (Allow List, Block List, Stranger), LPRAlarm (Allow List, Block List, Unknown)
- Set: Implemented per OEM documentation (URI: POST /API/PushSubscribe/Set), not hardware-tested
- Parameters verified: `app_support_ai_notification_subscribe`, `HddAlarm`, `FansAbnormalAlarm`, `IOAlarm`, `MotionAlarm`, `PIRAlarm`, `SmartAlarm`, `VideoLoss`, `FaceAlarm`, `LPRAlarm`, `ChnFlags`, `Group`

#### System Privacy Statement
- Status: Implemented
- Range: Verified on real hardware (URI: POST /API/SystemConfig/Statement/Range) — statement_file_name length limits (1..48 chars)
- Get: Verified on real hardware (URI: POST /API/SystemConfig/Statement/Get) — Current telemetry (statement_file_name: 'privacy_statement')
- Parameters verified: `statement_file_name`

#### Maintenance FtpUpgrade
- Status: Implemented
- Range: Verified on real hardware (URI: POST /API/Maintenance/FtpUpgrade/Range) — ftp_addr (0..64 chars), ftp_port (1..65535, default 21), username (0..24 chars), user_pwd (0..24 chars), online_upgrade_tips, support_onlineupgrade_edit (True), ftp_path (0..62 chars), ftp_buttons (['Save', 'Refresh', 'Check', 'Upgrade'])
- Get: Verified on real hardware (URI: POST /API/Maintenance/FtpUpgrade/Get) — Current telemetry (ftp_addr: '', ftp_port: 21, username: '', user_pwd_empty: True, ftp_path: '', check_for_updates: True, online_upgrade: True, Upgrade_button: False)
- Check: Verified on real hardware (URI: POST /API/Maintenance/FtpUpgrade/Check) — Returns firmware check status
- Progress: Verified on real hardware (URI: POST /API/Maintenance/FtpUpgrade/Progress) — Returns upgrade processing status
- Set: Implemented, not hardware-tested
- Upgrade: Implemented per OEM documentation (URI: POST /API/Maintenance/FtpUpgrade/Upgrade), not hardware-tested to prevent triggering firmware flashing
- Parameters verified: `ftp_addr`, `ftp_port`, `username`, `user_pwd`, `user_pwd_empty`, `ftp_path`, `check_for_updates`, `online_upgrade`, `Upgrade_button`, `url_key`, `has_new_firmware`, `upgrade_percent`, `upgrade_state`, `upgrade_result`

#### Maintenance Developer Mode
- Status: Implemented
- Range: Verified on real hardware (URI: POST /API/Maintenance/DeveloperMode/Range) — SSH switch (rw bool), export_disk_switch (Shut Off, Output To Terminal, Output To Disk), export_days (all, 1, 2, 3, 4, 5), default_timeout (1200000ms), enable_export (True), enable_delete (True), support_ipc_log_export (True), support_ipc_log_delete (True), and 256 channel log collection slots
- Get: Verified on real hardware (URI: POST /API/Maintenance/DeveloperMode/Get) — Current telemetry (ssh_switch: False, export_disk_switch: Shut Off, debug_info_level: Error Information, enable_export: True, enable_delete: True, 256 channel log collection states)
- Set: Implemented, not hardware-tested
- Token: Implemented per OEM documentation (URI: POST /API/Maintenance/DeveloperMode/Token)
- Clear: Implemented per OEM documentation (URI: POST /API/Maintenance/DeveloperMode/Clear)
- Parameters verified: `ssh_switch`, `export_disk_switch`, `debug_info_level`, `enable_export`, `enable_delete`, `support_ipc_log_export`, `support_ipc_log_delete`, `export_days`, `channel_info`, `download_type`

#### Storage Cloud
- Status: Implemented
- Range: Verified on real hardware (URI: POST /API/StorageConfig/Cloud/Range) — Cloud types (DROPBOX, Google Drive), status states (Activated, CloudFull, Unactivated, NetworkBlocked, Disabled), overwrite policies (OFF, Auto, 1Day, 3Days, 7Days, 14Days, 30Days, 90Days), video types (RF, AVI, MP4), and 256-channel folder mapping constraints
- Get: Verified on real hardware (URI: POST /API/StorageConfig/Cloud/Get) — Current telemetry (cloud_storage: False, cloud_type: DROPBOX, cloud_status: Unactivated, overwrite: Auto, video_type: MP4, 36 channel folder mappings)
- Set: Implemented, not hardware-tested
- Control: Implemented per OEM documentation (OAuth auth URL generator)
- AccessToken: Implemented per OEM documentation (POST /API/action/accesstoken)
- Parameters verified: `cloud_storage`, `cloud_type`, `cloud_status`, `total_size`, `used_size`, `progress`, `cloud_over_write`, `video_type`, `channel_info`, `accesstoken`

#### Record Playback Page
- Status: Implemented
- Range: Verified on real hardware (URI: POST /API/Playback/PlaybackPage/Range) across all playback modalities: Normal, Smart, Picture, HumanVehicle, PidLcd, LicensePlate, supportFaceAttr, FaceAttendance, and param_limit
- Playback event bitmask telemetry discovered and verified:
  - normal: 1 (0x1)
  - alarm: 2 (0x2)
  - motion: 4 (0x4)
  - IO: 8 (0x8)
  - ai: 128 (0x80)
  - manual: 16384 (0x4000)
  - PIR: 65536 (0x10000)
  - ANR: 134217728 (0x8000000)
- Face Attendance work schedule discovered and verified: working_days ('Mon.'..'Sat.'), on_duty_time ('09:00:00'), off_duty_time ('17:00:00')

#### Record Tag
- Status: Implemented
- Range: Verified on real hardware (URI: POST /API/Playback/Tag/Range) — 256 channels supported, Pre-play/Post-play options (5s, 10s, 30s, 1Min, 2Min, 5Min, 10Min), Tag_name length constraints (1..39 characters)
- Get: Verified on real hardware (URI: POST /API/Playback/Tag/Get) across single and multi-channel search queries
- Set: Implemented per OEM documentation (operations: 0=Set/Add, 1=Delete, 2=Rename), not hardware-tested to prevent modifying device metadata
- Parameters verified: `channel`, `start_date`, `start_time`, `end_date`, `end_time`, `Keyword`, `Tag_name`, `Tag_date`, `Tag_time`, `label_id`, `record_id`, `operate`

#### Record Picture Playback
- Status: Implemented
- Search: Verified on real hardware (URI: POST /API/Playback/Picture/Get) across single and multi-channel configurations
- Get: Implemented per OEM documentation schemas (fetching base64 image data via `pic_info` token)
- Parameters verified: `channel`, `start_date`, `start_time`, `end_date`, `end_time`, `record_type`, `record_type_ex`, `pic_sort`, `pic_info`

#### Record Search Record
- Status: Implemented
- Range: Verified on real hardware (URI: POST /API/Playback/SearchRecord/Range) — Supported channels: 256, stream modes: Mainstream, Substream, size limits, disk_event_id limits
- Search: Verified on real hardware (URI: POST /API/Playback/SearchRecord/Search) — Discovered 47 recorded footage segments on CH1 for 08/20/2026 with exact start/end timestamps, file sizes, record types, record IDs, and lock states
- Parameters verified: `channel`, `start_date`, `start_time`, `end_date`, `end_time`, `record_type`, `record_type_ex`, `stream_mode`, `smart_region`, `enable_smart_search`

#### Record Search Month
- Status: Implemented
- Get: Verified on real hardware (URI: POST /API/Playback/SearchMonth/Get)
- Calendar discovery: Discovered active recorded footage across August 2026 (days 15..20) with active record_type 3
- Parameters verified: `channel` (array of channel names or empty array for all), `start_date` (MM/DD/YYYY), `stream_type` (Mainstream, Substream), `search_type` (Record, Picture, FD, PVD, PidLcd, Repeat, FaceAttendance)
- Response structures verified: `is_has_rec` (31-day boolean integer array), `record_type` (31-day recording type identifier array)

#### PreviewChannel
- Status: Complete
- Unified Manager: `cam.preview_channel` provides unified access to all 4 OEM-documented PreviewChannel operational interfaces:
  - `cam.preview_channel.ptz` (`PreviewPTZManager`)
  - `cam.preview_channel.manual_alarm` (`ManualAlarmManager`)
  - `cam.preview_channel.floodlight_audio_alarm` (`FloodlightAudioAlarmManager`)
  - `cam.preview_channel.dual_talk` (`DualTalkManager`)

#### PreviewChannel PTZ
- Status: Implemented
- Get: Verified on real hardware on CH3 motorized optical speed dome (255 preset point slots, watch mode, line scan area, speed, cruise modes, tour tracks, pattern scans) and standard fixed channels
- Progress: Verified on real hardware (`/API/PreviewChannel/PTZ/Control/Progress` returning `zoom_slider`, `focus_slider`, `isctl: True`)
- Control: Implemented, not hardware-tested
- No PTZ directional movements, zoom/focus alterations, or presets were triggered during verification

#### PreviewChannel DualTalk
- Status: Implemented
- Get: Tested against hardware (URI: POST /API/PreviewChannel/DualTalk/Get) — Device returned error_code "not_found"
- Note: Hardware endpoint tested across channels and payload structures; two-way audio intercom is unsupported or inactive on this NVR firmware.
- Set: Implemented per OEM documentation schemas, but intentionally not hardware-tested.

#### PreviewChannel Floodlight & Audio Alarm
- Status: Implemented
- Get: Verified on real hardware across channels
- Active deterrence hardware discovered and verified:
  - CH6: Siren/Horn deterrence telemetry (`audioAlarm_switch: False`, `audioAlarm_value: 5`, `audioAlarm_value_range: 1..10`, `audioAlarm_value_adjustable: True`)
  - CH29: White-light floodlight deterrence telemetry (`floodlight_switch: False`, `floodlight_mode: 0 [always on]`, `floodlight_strobe_frequency: 1 [middle]`, `floodlight_value_adjustable: True`)
- Parameters verified: `floodlight_switch`, `floodlight_mode` (0: always on, 1: flashing), `floodlight_value` (1..100), `floodlight_strobe_frequency` (0: low, 1: middle, 2: high), `audioAlarm_switch`, `audioAlarm_value` (1..10), `redBlueLight_switch`, `operation_type` (Floodlight, AudioAlarm, RedBlueLight, All)
- Set: Implemented, not hardware-tested
- No sirens, floodlights, or strobe lights were triggered during verification

#### PreviewChannel Manual Alarm
- Status: Implemented
- Get: Verified on real hardware across 10 output ports (4 physical local relay/alarm outputs Local->1..Local->4 and 6 digital IP camera alarm outputs IP_CH1->1, IP_CH3->1, IP_CH5->1, IP_CH6->1, IP_CH11->1, IP_CH31->1)
- Set: Implemented, not hardware-tested
- No siren or physical alarm output relays were tripped during verification

#### Channel Analog Channel
- Status: Implemented
- Range: Verified on real hardware (channel_max=256, page_type="ChannelConfig")
- Get: Verified on real hardware (device operating in pure IP NVR mode with channel_info empty; hybrid DVR/XVR state/switch/channel_name schemas fully supported)
- Set: Implemented, not hardware-tested
- No analog channel switches or bindings were modified

#### Channel ROI
- Status: Implemented
- Range: Verified on real hardware (channel_max=256, channel_info type object)
- Get: Verified on real hardware across 256 channels (8 active ROI-capable channels CH1..CH8 with 8 customizable ROI regions each across Mainstream, Substream, and Mobilestream; 248 unconfigured channels return 'Not configured')
- Parameters verified: roi_switch, roi_level (Lowest, Lower, Low, Medium, Higher, Highest), non_roi_fps (1..29 fps), rect (left, top, width, height [0..704, 0..576])
- Set: Implemented, not hardware-tested
- No ROI compression zones or target bitrates were modified

#### Channel PTZ Tasks / Schedules
- Status: Implemented
- Range: Verified on real hardware (channel_max=256, supported_channels=['CH3'], belt_times_use [0..100], tasks_recovery_times [5..720 min, default 5])
- Get: Verified on real hardware (CH3 speed dome active PTZ task schedule structure verified across 5 cruise modes: Close, Line Scan, Tour, Pattern Scan, Preset with weekly 48-slot half-hour schedules)
- Set: Implemented, not hardware-tested
- No PTZ tour schedules or recovery times were modified

#### Channel Protocol Manage
- Status: Implemented
- Range: Verified on real hardware (16 custom RTSP protocol profile slots supported)
- Get: Verified on real hardware (16 active custom RTSP streaming configurations: protocol_name, custom_stream for Mainstream/Substream, source_path, RTSP port)
- Set: Implemented, not hardware-tested
- No custom RTSP stream mappings were modified

#### Channel PTZ
- Status: Implemented
- Range: Verified on real hardware (channel_max=256, support_copy=True)
- Get: Verified on real hardware across 256 channels
- Telemetry observed: 31 PTZ-configured channels (Pelco-D, baudrate 9600, databit 8, stopbit 1, parity None, address 1, copy_ch digit), CH3 optical speed dome telemetry (focus_mode: Auto, zoom_status: 5s, pan_tilt_status: 5s, preset_status: 5s, min_focus_distance: 3m), 5 fixed cameras (Not support), 220 unconfigured channels (Not configured)
- Set: Implemented, not hardware-tested
- No PTZ addresses, serial protocols, or presets were modified

#### Channel Broadcast IPC
- Status: Implemented
- Range: Verified on real hardware (device_info array max_size=500, supports Private, Onvif, RTSP, and Custom protocols 1..16)
- Search: Verified on real hardware (URI: POST /API/ChannelConfig/RemoteDev/Search) — Discovers local subnet IPCs for automated NVR onboarding
- Set: Implemented, not hardware-tested
- No remote camera network configurations or credentials were modified

#### Channel IPChannel
- Status: Implemented
- Range: Verified on real hardware (channel_max=256, operation_type: AddOrEditChannel, EditIPCParam, SaveCommonParam, PoeToIpChannel)
- Get: Verified on real hardware across 256 channels
- Channel Discovery: 36 active Online IP channels with full hardware telemetry (Private & Onvif protocols, forward ports, MAC addresses, model numbers, software versions, network mode) + 220 NotConfigured channels
- Next bind channel: CH37
- Set: Implemented, not hardware-tested
- AutoAddIPC Set: Implemented, not hardware-tested
- No IP channel mappings or camera credentials were modified

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

#### Network IPv6
- Status: Implemented
- Range: Tested against hardware (URI: POST /API/NetworkConfig/Ipv6/Range) — Device returned error_code "not_found"
- Get: Tested against hardware (URI: POST /API/NetworkConfig/Ipv6/Get) — Device returned error_code "not_found"
- Note: Hardware endpoint tested across case variations (Ipv6, ipv6, IPv6). Like RTSP and IEEE8021x, IPv6 standalone endpoint is IPC-specific or inactive on this NVR firmware.
- Set: Implemented per OEM documentation schemas, but intentionally not hardware-tested.

#### Network Voice Assistant
- Status: Implemented
- Range: Verified on real hardware (URI: POST /API/NetworkConfig/SMARTHOME/Range)
- Get: Verified on real hardware (URI: POST /API/NetworkConfig/SMARTHOME/Get)
- Configuration parameters verified: SmartHomePage (Amazon, Google), operate (Bind, UnBind, Apply), BindEnable (bool), UserName (0..128 chars), ScreenStream (Mainstream, Substream), default_timeout (60000ms)
- Active configuration observed: Google assistant bound with active account and Substream projection
- Control/Set: Implemented, not hardware-tested
- No voice assistant cloud bindings, accounts, or stream mappings were modified

#### Network GBT28181
- Status: Implemented
- Range: Tested against hardware (URI: POST /API/NetworkConfig/T28181/Range) — Device returned error_code "not_found"
- Get: Tested against hardware (URI: POST /API/NetworkConfig/T28181/Get) — Device returned error_code "not_found"
- Note: Hardware endpoint tested across case variations (T28181, t28181, GBT28181, gbt28181). Like RTSP, IEEE8021x, and standalone IPv6, GB/T 28181 protocol endpoint is unsupported or inactive on this NVR firmware.
- Set: Implemented per OEM documentation schemas, but intentionally not hardware-tested.

#### Network Tuya
- Status: Implemented
- Range: Tested against hardware (URI: POST /API/NetworkConfig/Tuya/Range) — Device returned error_code "not_found"
- Get: Tested against hardware (URI: POST /API/NetworkConfig/Tuya/Get) — Device returned error_code "not_found"
- Note: Hardware endpoint tested across case variations (Tuya, tuya). Tuya cloud IoT integration is unsupported or inactive on this NVR firmware.
- Set: Implemented per OEM documentation schemas, but intentionally not hardware-tested.

#### Network WLAN Scan
- Status: Implemented
- Scan: Tested against hardware (URI: POST /API/NetworkConfig/ScanWlan/Scan) — Device returned error_code "not_found"
- Note: Hardware endpoint tested across case variations (ScanWlan, scan_wlan, WLANScan). Wireless client/AP scanning is unsupported or inactive on this wired ethernet NVR.
- Join/Set: Implemented per OEM documentation schemas, but intentionally not hardware-tested.

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