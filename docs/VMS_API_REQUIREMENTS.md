# Enterprise VMS API Requirements & Priority Classification

## Executive Summary
This document defines the functional requirement priorities for the C++20 OPTIER VMS, categorizing the complete OEM API surface into 4 distinct implementation tiers:
- **P0 (Critical Core)**: Mandatory for minimum viable VMS operation (Live View, Playback, Recording, PTZ, Authentication, Basic Alarms).
- **P1 (Major VMS Functionality)**: Advanced capabilities required for enterprise deployments (AI Analytics, Face Watchlists, LPR/ANPR, Forensics, RBAC).
- **P2 (Operational & Ancillary)**: Administrative features for large-scale operations (Cloud/FTP backups, Attendance, Audio modes, Multi-IPC upgrades).
- **P3 (Engineering & Diagnostics)**: Low-level manufacturing, field recovery, and developer troubleshooting tools.

---

## 1. Priority P0 — Critical Core VMS Foundation

| Functional Domain | OEM API Endpoints | VMS Engine Responsibility |
| :--- | :--- | :--- |
| **Authentication & Session** | `POST /API/Web/Login`<br>`POST /API/Web/Logout`<br>`POST /API/Login/Heartbeat` | Digest session negotiation, keepalives, and automatic reconnection. |
| **Device & Channel Inventory**| `POST /API/Login/DeviceInfo/Get`<br>`POST /API/Login/ChannelInfo/Get`<br>`POST /API/Channel/IP Channels/Get`<br>`POST /API/Channel/RemoteDev/Get` | Multi-channel discovery (1..256 channels), physical IP camera mapping, and online status polling. |
| **Media Plane Streaming** | `POST /API/Network/RtspUrl/Get`<br>`RTSP TCP / RTP Transport` | Live view mainstream and substream endpoint resolution and RTSP stream consumption. |
| **Recording & Archive** | `POST /API/Record/SearchMonth`<br>`POST /API/Record/SearchRecord`<br>`POST /API/PreviewChannel/PlaybackRtspUrl/Get`<br>`POST /API/Record/RecordConfig/{Range,Get,Set}` | Calendar month bitmask search, second-accurate timeline slice retrieval, and playback RTSP streaming. |
| **Storage Infrastructure** | `POST /API/Storage/Disk/{Range,Get,Set}` | HDD health monitoring, RAID status, capacity calculations, and overwrite policies. |
| **Video Encoding & Picture** | `POST /API/Video/Encode/{Range,Get,Set}`<br>`POST /API/Snapshot/Snapshot` | Remote codec configuration (H.264/H.265, Bitrate, FPS) and real-time snapshot capture. |
| **PTZ Control** | `POST /API/PreviewChannel/PTZ/Control`<br>`POST /API/PreviewChannel/PTZ/Get` | Real-time pan/tilt/zoom execution, speed adjustment, and preset jump operations. |
| **Basic Event Detection** | `POST /API/AlarmConfig/Motion/{Range,Get,Set}`<br>`POST /API/AlarmConfig/IO/{Range,Get,Set}`<br>`POST /API/AlarmConfig/Combination/{Range,Get,Set}`<br>`POST /API/PushSubscribe/{Get,Set}` | Video motion grid, physical sensor triggers, multi-sensor joint router, and push notification intake. |
| **System Diagnostics & Clock**| `POST /API/SystemInfo/Base/Get`<br>`POST /API/SystemConfig/DateTime/{Range,Get,Set}` | Hardware telemetry and millisecond-accurate NTP/RTC time synchronization. |
| **User Access Control** | `POST /API/SystemConfig/User/{Range,Get,Set}`<br>`POST /API/Login/DevicePage/Get` | 512-slot user accounts, channel live/playback/PTZ permissions, and dynamic UI menu structures. |

---

## 2. Priority P1 — Major Enterprise VMS Capabilities

| Functional Domain | OEM API Endpoints | VMS Engine Responsibility |
| :--- | :--- | :--- |
| **Face Recognition & Watchlists** | `POST /API/AI/FDGroup/{Get,GetId,Add,Modify,Remove,Change}`<br>`POST /API/AI/Faces/{Add,Modify,Remove,GetImagesFeature}`<br>`POST /API/AI/AddedFaces/{Search,GetByIndex,GetById,GetId}`<br>`POST /API/AI/SnapedFaces/{Search,StopSearch,GetByIndex,GetById}` | Face library enrollment, eigenvalue extraction, VIP/Blocklist matching, and 100k+ forensic face searches. |
| **LPR / ANPR Vehicle Tracking** | `POST /API/AI/PlateGroup/{Get,GetId,Add,Modify,Remove}`<br>`POST /API/AI/Plates/{Add,Modify,Remove,Change}`<br>`POST /API/AI/AddedPlates/{GetCount,GetId,GetById}`<br>`POST /API/AI/SnapedObjects/{SearchPlate,StopSearch,GetByIndex,GetById}`<br>`POST /API/AI/Setup/LPD/{Range,Get,Set}` | Vehicle allow/block lists, plate number enrollment, and fuzzy plate search across 200k+ forensic snapshots. |
| **Video Analytics (Perimeter)**| `POST /API/AI/Setup/Line/{Range,Get,Set}`<br>`POST /API/AI/Setup/PID/{Range,Get,Set}`<br>`POST /API/AI/Setup/PD/{Range,Get,Set}`<br>`POST /API/AI/Setup/CC/{Range,Get,Set}`<br>`POST /API/AI/Setup/SOD/{Range,Get,Set}`<br>`POST /API/AI/Setup/Sound_Detection/{Range,Get,Set}`<br>`POST /API/AI/Setup/Occlusion_Detection/{Range,Get,Set}`<br>`POST /API/AI/Setup/AISchedule/{Range,Get,Set}` | Tripwire vectors, perimeter quadrilateral zones, human body detection, people counting, and audio spike detection. |
| **Alarm Linkage & Deterrence** | `POST /API/AlarmConfig/PIR/{Range,Get,Set}`<br>`POST /API/AlarmConfig/Schedule/{Range,Get,Set}`<br>`POST /API/AlarmConfig/Exception/{Range,Get,Set}`<br>`POST /API/AlarmConfig/Disarming/{Range,Get,Set}`<br>`POST /API/PreviewChannel/ManualAlarm/{Get,Set}`<br>`POST /API/PreviewChannel/Floodlight2AudioAlarm/{Get,Set}` | Arming schedules, operator panic sirens, flashing floodlights, and system exception alerts. |
| **Image Optimization & OSD** | `POST /API/Video/Color/{Range,Get,Set}`<br>`POST /API/Video/ImageControl/{Range,Get,Set,Default}`<br>`POST /API/Video/OSD/{Range,Get,Set}`<br>`POST /API/Video/VideoCover/{Range,Get,Set}` | WDR, 3D noise reduction, privacy masking, and on-screen channel titles. |
| **Forensic Evidence Search** | `POST /API/Record/PicturePlayback/{Search,GetByIndex}`<br>`POST /API/Record/RecordTag/{Range,Get,Add,Modify,Remove}`<br>`POST /API/System/Log/Search` | Tagging video bookmarks, thumbnail browsing, and system audit log queries. |
| **Security & Policy** | `POST /API/AccountRules/Get` | Password complexity policy enforcement. |

---

## 3. Priority P2 — Operational & Ancillary Management

| Functional Domain | OEM API Endpoints | VMS Engine Responsibility |
| :--- | :--- | :--- |
| **Staff Attendance Tracking** | `POST /API/AI/FDAttendance/{Range,Get,Set}` | Shift schedules (Day/Week/Month) and attendance email reporting. |
| **Offsite & Cloud Backups** | `POST /API/Storage/Cloud/{Range,Get,Set}`<br>`POST /API/Storage/FTP/{Range,Get,Set,Test}` | Offsite backup dispatch to Dropbox/Google Drive/FTP. |
| **Multi-IPC Remote Firmware** | `POST /API/Maintenance/IPCUpgrade/{Range,Get,Set,Start}`<br>`POST /API/Maintenance/FtpIPCUpgrade/{Range,Get,Set,Start}`<br>`POST /API/Maintenance/IPCParam/{Export,Import}`<br>`POST /API/Maintenance/IPCReboot/Reboot` | Batch firmware upgrading and configuration import/export for attached IP cameras. |
| **Password Recovery Workflows**| `POST /API/RecoverPassword/{Range,Get,Set}`<br>`POST /API/RecoverPassword/Authorization/{Range,Get,Set}`<br>`POST /API/RecoverPassword/Certificate/Export` | Security questions and certificate-based admin password reset. |
| **Scheduled Maintenance** | `POST /API/Maintenance/AutoReboot/{Range,Get,Set}`<br>`POST /API/SystemConfig/Output/{Range,Get,Set}` | Scheduled weekly reboots and local HDMI/VGA display resolution adjustments. |

---

## 4. Priority P3 — Engineering, Diagnostics & Factory Reset

| Functional Domain | OEM API Endpoints | VMS Engine Responsibility |
| :--- | :--- | :--- |
| **System Firmware Flashing** | `POST /API/Maintenance/SystemUpgrade/{Upgrade,VersionCheck}` | NVR system firmware upload and binary flashing. |
| **Developer & Factory Tools** | `POST /API/Maintenance/DeveloperMode/{Get,Set}`<br>`POST /API/Maintenance/Reset`<br>`POST /API/Maintenance/IPCReset/Reset`<br>`POST /API/System/Log/Clear` | Engineering Telnet/SSH access and factory default resets. |
