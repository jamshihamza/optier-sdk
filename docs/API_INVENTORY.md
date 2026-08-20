# Complete OEM API Inventory & Protocol Specification

## Executive Overview
This document represents the exhaustive, authoritative inventory of the OEM HTTP/JSON protocol discovered across both official documentation trees:
- `C:\Users\ACCOUNTS\Desktop\API Protocol-English-2024-1-29\book_en` (676 HTML specification files)
- `C:\Users\ACCOUNTS\Desktop\OPT_SDK\API notes` (170 specification files)

---

## 1. Protocol Architecture & Common Conventions

### Transport & Authentication
- **Transport**: HTTP/1.1 over TCP (Standard Port `80` or `443` HTTPS).
- **Authentication**: HTTP Digest Authentication (RFC 2617 / RFC 7616) using MD5 (`qop="auth"`).
- **Session Handshake**: `POST /API/Web/Login` initiates web session and returns authentication cookies and CSRF tokens (`_CSRF_COOKIE_`).
- **Heartbeat Keepalive**: `POST /API/Login/Heartbeat` sent every 15–30s to keep session alive.
- **Request Envelope**:
```json
{
    "version": "1.0",
    "data": { ... }
}
```
- **Response Envelope**:
```json
{
    "result": "success" | "failed",
    "error_code": "operate_success" | "param_error" | "no_permission" | "not_found",
    "reason": "...",
    "data": { ... }
}
```

---

## 2. Exhaustive API Domain Matrix

### Domain 1: Authentication, Session & User RBAC

| Endpoint URI | Method | Action Types | Target | Scope / Channel Limits | Base64 / Binary | Side Effects / Safety | Hardware Status |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `POST /API/Web/Login` | POST | Login | NVR/IPC | System Global | No | Session Creation | ✅ Verified |
| `POST /API/Web/Logout` | POST | Logout | NVR/IPC | System Global | No | Session Teardown | ✅ Verified |
| `POST /API/Login/Heartbeat` | POST | Heartbeat | NVR/IPC | System Global | No | None (Read-only) | ✅ Verified |
| `POST /API/Login/DeviceInfo/Get` | POST | Get | NVR/IPC | System Global | No | None (Read-only) | ✅ Verified |
| `POST /API/Login/ChannelInfo/Get` | POST | Get | NVR/IPC | 1..256 Channels | No | None (Read-only) | ✅ Verified |
| `POST /API/Login/DevicePage/Get` | POST | Get | NVR/IPC | System Global | No | None (Read-only) | ✅ Verified |
| `POST /API/AccountRules/Get` | POST | Get | NVR/IPC | System Global | No | None (Read-only) | ✅ Verified |
| `POST /API/SystemConfig/User/{Range,Get,Set}` | POST | Range, Get, Set | NVR/IPC | 512 User Slots | No | User CRUD (Write) | ✅ Verified |
| `POST /API/RecoverPassword/{Range,Get,Set}` | POST | Range, Get, Set | NVR/IPC | System Global | No | Email / Security Qs | ✅ Verified |
| `POST /API/RecoverPassword/Authorization/{Range,Get,Set}`| POST | Range, Get, Set | NVR/IPC | System Global | No | Challenge Qs | ✅ Verified |
| `POST /API/RecoverPassword/Certificate/Export` | POST | Export | NVR/IPC | System Global | Base64 | Certificate Dump | Documented |
| `POST /API/FirstLogin/Password/Set` | POST | Set | NVR/IPC | System Global | No | Initial Password | Documented |
| `POST /API/Maintenance/TransKey/Get` | POST | Get | NVR/IPC | System Global | Base64 | Key Exchange | ✅ Verified |

---

### Domain 2: Device Management, System & Maintenance

| Endpoint URI | Method | Action Types | Target | Scope / Limits | Base64 / Binary | Side Effects / Safety | Hardware Status |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `POST /API/SystemInfo/Base/Get` | POST | Get | NVR/IPC | System Global | No | None (Read-only) | ✅ Verified |
| `POST /API/SystemInfo/Channel/Get` | POST | Get | NVR/IPC | 1..256 Channels | No | None (Read-only) | ✅ Verified |
| `POST /API/SystemConfig/General/{Range,Get,Set}` | POST | Range, Get, Set | NVR/IPC | System Global | No | Config Write | ✅ Verified |
| `POST /API/SystemConfig/DateTime/{Range,Get,Set}` | POST | Range, Get, Set | NVR/IPC | System Global | No | Time Sync Write | ✅ Verified |
| `POST /API/SystemConfig/NTP/{Range,Get,Set}` | POST | Range, Get, Set | NVR/IPC | System Global | No | NTP Server Write | ✅ Verified |
| `POST /API/SystemConfig/DST/{Range,Get,Set}` | POST | Range, Get, Set | NVR/IPC | System Global | No | Daylight Savings | ✅ Verified |
| `POST /API/SystemConfig/Output/{Range,Get,Set}` | POST | Range, Get, Set | NVR/IPC | HDMI/VGA Out | No | Resolution Change | ✅ Verified |
| `POST /API/SystemConfig/Statement/{Range,Get}` | POST | Range, Get | NVR/IPC | System Global | No | None (Read-only) | ✅ Verified |
| `POST /API/System/Log/Search` | POST | Search | NVR/IPC | Paginated (100) | No | None (Read-only) | ✅ Verified |
| `POST /API/System/Log/Export` | POST | Export | NVR/IPC | System Global | Binary/CSV | None (Read-only) | Documented |
| `POST /API/System/Log/Clear` | POST | Clear | NVR/IPC | System Global | No | **DESTRUCTIVE** | Documented |
| `POST /API/Maintenance/Reboot` | POST | Reboot | NVR/IPC | System Global | No | **DESTRUCTIVE** | Documented |
| `POST /API/Maintenance/Reset` | POST | Reset | NVR/IPC | System Global | No | **DESTRUCTIVE** | Documented |
| `POST /API/Maintenance/AutoReboot/{Range,Get,Set}` | POST | Range, Get, Set | NVR/IPC | System Global | No | Schedule Write | ✅ Verified |
| `POST /API/Maintenance/DeveloperMode/{Get,Set}` | POST | Get, Set | NVR/IPC | System Global | No | Telnet / SSH Enable | ✅ Verified |
| `POST /API/Maintenance/SystemUpgrade/{Upgrade,VersionCheck}` | POST | Upgrade, Check | NVR/IPC | Firmware Bin | Binary Upload | **DESTRUCTIVE** | Documented |
| `POST /API/Maintenance/FtpUpgrade/{Range,Get,Set,Start,Stop}` | POST | Range, Get, Set | NVR/IPC | FTP Firmware | No | Remote Upgrade | ✅ Verified |
| `POST /API/Maintenance/IPCUpgrade/{Range,Get,Set,Start}` | POST | Range, Get, Set | NVR/IPC | 1..256 IPCs | Binary Multi | Multi-IPC Upgrade | ✅ Verified |
| `POST /API/Maintenance/FtpIPCUpgrade/{Range,Get,Set,Start}` | POST | Range, Get, Set | NVR/IPC | 1..256 IPCs | No | Remote IPC Upgrade| ✅ Verified |
| `POST /API/Maintenance/IPCParam/{Export,Import}` | POST | Export, Import | NVR/IPC | 1..256 IPCs | Base64/Tar | Batch Config | ✅ Verified |
| `POST /API/Maintenance/IPCReboot/Reboot` | POST | Reboot | NVR/IPC | 1..256 IPCs | No | Remote IPC Reboot | ✅ Verified |
| `POST /API/Maintenance/IPCReset/Reset` | POST | Reset | NVR/IPC | 1..256 IPCs | No | Remote IPC Reset | ✅ Verified |

---

### Domain 3: Video Stream, RTSP & Picture Encoding

| Endpoint URI | Method | Action Types | Target | Scope / Limits | Base64 / Binary | Side Effects / Safety | Hardware Status |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `POST /API/Network/RtspUrl/Get` | POST | Get | NVR/IPC | 1..256 Channels | No | None (Read-only) | ✅ Verified |
| `POST /API/PreviewChannel/PlaybackRtspUrl/Get` | POST | Get | NVR/IPC | 1..256 Channels | No | None (Read-only) | ✅ Verified |
| `POST /API/Video/Encode/{Range,Get,Set}` | POST | Range, Get, Set | NVR/IPC | 1..256 Channels | No | Codec/Res Write | ✅ Verified |
| `POST /API/Video/Color/{Range,Get,Set}` | POST | Range, Get, Set | NVR/IPC | 1..256 Channels | No | Bright/Contrast | ✅ Verified |
| `POST /API/Video/ImageControl/{Range,Get,Set,Default}` | POST | Range, Get, Set | NVR/IPC | 1..256 Channels | No | WDR, 3DNR, Mirror | ✅ Verified |
| `POST /API/Video/OSD/{Range,Get,Set}` | POST | Range, Get, Set | NVR/IPC | 1..256 Channels | No | On-Screen Display | ✅ Verified |
| `POST /API/Video/VideoCover/{Range,Get,Set}` | POST | Range, Get, Set | NVR/IPC | 1..256 Channels | No | Privacy Mask Grid | ✅ Verified |
| `POST /API/Video/ROI/{Range,Get,Set}` | POST | Range, Get, Set | NVR/IPC | 1..256 Channels | No | Region of Interest | ✅ Verified |
| `POST /API/Snapshot/Snapshot` | POST | Snapshot | NVR/IPC | 1..256 Channels | Base64 JPEG | Single Snapshot | ✅ Verified |

---

### Domain 4: Recording, Storage & Playback Search

| Endpoint URI | Method | Action Types | Target | Scope / Limits | Base64 / Binary | Side Effects / Safety | Hardware Status |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `POST /API/Record/SearchMonth` | POST | SearchMonth | NVR/IPC | 1..256 Channels | No | Calendar Grid | ✅ Verified |
| `POST /API/Record/SearchRecord` | POST | SearchRecord | NVR/IPC | 1..256 Channels | No | Timeline Slices | ✅ Verified |
| `POST /API/Record/PicturePlayback/Search` | POST | Search | NVR/IPC | 1..256 Channels | No | Paginated Images | ✅ Verified |
| `POST /API/Record/PicturePlayback/GetByIndex` | POST | GetByIndex | NVR/IPC | Paginated (20) | Base64 JPEG | Image Download | ✅ Verified |
| `POST /API/Record/RecordTag/{Range,Get,Add,Modify,Remove}`| POST | Range, Get, CRUD| NVR/IPC | 1..256 Channels | No | Bookmark Tags | ✅ Verified |
| `POST /API/Record/PlaybackPage/Get` | POST | Get | NVR/IPC | 1..256 Channels | No | None (Read-only) | ✅ Verified |
| `POST /API/Record/RecordInfo/Get` | POST | Get | NVR/IPC | 1..256 Channels | No | Active Rec Status | ✅ Verified |
| `POST /API/Record/RecordConfig/{Range,Get,Set}` | POST | Range, Get, Set | NVR/IPC | 1..256 Channels | No | Schedule Matrix | ✅ Verified |
| `POST /API/Storage/Disk/{Range,Get,Set}` | POST | Range, Get, Set | NVR/IPC | Physical HDDs | No | HDD Overwrite/Rec | ✅ Verified |
| `POST /API/Storage/Cloud/{Range,Get,Set}` | POST | Range, Get, Set | NVR/IPC | Dropbox/GDrive | No | Cloud Storage | ✅ Verified |
| `POST /API/Storage/FTP/{Range,Get,Set,Test}` | POST | Range, Get, Test| NVR/IPC | Remote FTP | No | FTP Storage Rec | ✅ Verified |

---

### Domain 5: Alarm & Event Linkage

| Endpoint URI | Method | Action Types | Target | Scope / Limits | Base64 / Binary | Side Effects / Safety | Hardware Status |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `POST /API/AlarmConfig/Motion/{Range,Get,Set}` | POST | Range, Get, Set | NVR/IPC | 1..256 Channels | No | Motion Grid Write | ✅ Verified |
| `POST /API/AlarmConfig/PIR/{Range,Get,Set}` | POST | Range, Get, Set | NVR/IPC | 1..256 Channels | No | PIR Sensitivity | ✅ Verified |
| `POST /API/AlarmConfig/IO/{Range,Get,Set}` | POST | Range, Get, Set | NVR/IPC | 1..32 Sensor IO | No | Relay NO/NC | ✅ Verified |
| `POST /API/AlarmConfig/Combination/{Range,Get,Set}` | POST | Range, Get, Set | NVR/IPC | 1..256 Channels | No | Multi-Trigger Map | ✅ Verified |
| `POST /API/AlarmConfig/Schedule/{Range,Get,Set}` | POST | Range, Get, Set | NVR/IPC | 1..256 Channels | No | Arming Timeblocks | ✅ Verified |
| `POST /API/AlarmConfig/Exception/{Range,Get,Set}` | POST | Range, Get, Set | NVR/IPC | Disk/Net Loss | No | Exception Routing | ✅ Verified |
| `POST /API/AlarmConfig/Disarming/{Range,Get,Set}` | POST | Range, Get, Set | NVR/IPC | 1..256 Channels | No | Emergency Disarm | ✅ Verified |
| `POST /API/PreviewChannel/ManualAlarm/{Get,Set}` | POST | Get, Set | NVR/IPC | 1..256 Channels | No | Panic Siren/Light | ✅ Verified |
| `POST /API/PreviewChannel/Floodlight2AudioAlarm/{Get,Set}`| POST | Get, Set | NVR/IPC | 1..256 Channels | No | Light/Voice Mode | ✅ Verified |
| `POST /API/PushSubscribe/{Get,Set}` | POST | Get, Set | NVR/IPC | 28 Push Types | No | App Push Sub | ✅ Verified |

---

### Domain 6: AI Analytics, Face Recognition & LPR

| Endpoint URI | Method | Action Types | Target | Scope / Limits | Base64 / Binary | Side Effects / Safety | Hardware Status |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `POST /API/AI/FDGroup/{Get,GetId,Add,Modify,Remove,Change}`| POST | Group CRUD | NVR/IPC | 16 Face Groups | No | Watchlist DB | ✅ Verified |
| `POST /API/AI/Faces/{Add,Modify,Remove,GetImagesFeature}`| POST | Person CRUD | NVR/IPC | 10k Face Library| Base64 Eigen/JPG | Enrolment Write | ✅ Verified |
| `POST /API/AI/AddedFaces/{Search,GetByIndex,GetById,GetId}`| POST | Search, Query | NVR/IPC | 10k Face Library| Base64 Eigen/JPG | None (Read-only) | ✅ Verified |
| `POST /API/AI/SnapedFaces/{Search,StopSearch,GetByIndex,GetById}`| POST | Forensics | NVR/IPC | 100k Snapshots | Base64 Crop/Scene| Forensic Search | ✅ Verified |
| `POST /API/AI/VhdLogCount/Get` | POST | Get | NVR/IPC | 1..256 Channels | No | Event Log Totals | ✅ Verified |
| `POST /API/AI/processAlarm/Get` | POST | Get | NVR/IPC | 1..256 Channels | Base64 Thumbnail| Realtime Alarms | ✅ Verified |
| `POST /API/AI/FDAttendance/{Range,Get,Set}` | POST | Range, Get, Set | NVR/IPC | Day/Week/Month | No | Staff Shift Rules | ✅ Verified |
| `POST /API/AI/PlateGroup/{Get,GetId,Add,Modify,Remove}` | POST | Group CRUD | NVR/IPC | 16 Plate Groups | No | Allow/Block Lists | ✅ Verified |
| `POST /API/AI/Plates/{Add,Modify,Remove,Change}` | POST | Vehicle CRUD | NVR/IPC | 10k Plate Library| No | Vehicle Enrolment| ✅ Verified |
| `POST /API/AI/AddedPlates/{GetCount,GetId,GetById}` | POST | Count, Query | NVR/IPC | 10k Plate Library| No | None (Read-only) | ✅ Verified |
| `POST /API/AI/SnapedObjects/{SearchPlate,StopSearch,GetByIndex,GetById}`| POST | Forensics | NVR/IPC | 200k Snapshots | Base64 Plate/Car | Fuzzy LPR Search | ✅ Verified |
| `POST /API/AI/Setup/LPD/{Range,Get,Set}` | POST | Range, Get, Set | NVR/IPC | 1..256 Channels | No | Detection Config | ✅ Verified |
| `POST /API/AI/Setup/AISchedule/{Range,Get,Set}` | POST | Range, Get, Set | NVR/IPC | 1..256 Channels | No | AI Runtime Blocks | ✅ Verified |
| `POST /API/AI/Setup/Line/{Range,Get,Set}` | POST | Range, Get, Set | NVR/IPC | 1..256 Channels | No | Tripwire Vectors | ✅ Verified |
| `POST /API/AI/Setup/PID/{Range,Get,Set}` | POST | Range, Get, Set | NVR/IPC | 1..256 Channels | No | Perimeter Zones | ✅ Verified |
| `POST /API/AI/Setup/SOD/{Range,Get,Set}` | POST | Range, Get, Set | NVR/IPC | 1..256 Channels | No | Left/Lost Objects | ✅ Verified |
| `POST /API/AI/Setup/PD/{Range,Get,Set}` | POST | Range, Get, Set | NVR/IPC | 1..256 Channels | No | Human Detection | ✅ Verified |
| `POST /API/AI/Setup/CC/{Range,Get,Set}` | POST | Range, Get, Set | NVR/IPC | 1..256 Channels | No | People Counting | ✅ Verified |
| `POST /API/AI/Setup/Sound_Detection/{Range,Get,Set}` | POST | Range, Get, Set | NVR/IPC | 1..256 Channels | No | Audio Anomalies | ✅ Verified |
| `POST /API/AI/Setup/Occlusion_Detection/{Range,Get,Set}` | POST | Range, Get, Set | NVR/IPC | 1..256 Channels | No | Lens Blind Mask | ✅ Verified |
| `POST /API/AI/Setup/Intelligent_Analysis/{Range,Get,Set}` | POST | Range, Get, Set | NVR/IPC | 1..256 Channels | No | Crowd / Density | ✅ Verified |

---

### Domain 7: PTZ Control & Scheduled Tasks

| Endpoint URI | Method | Action Types | Target | Scope / Limits | Base64 / Binary | Side Effects / Safety | Hardware Status |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `POST /API/PreviewChannel/PTZ/Control` | POST | Control | NVR/IPC | Pan/Tilt/Zoom | No | Physical Motion | ✅ Verified |
| `POST /API/PreviewChannel/PTZ/Control/Progress` | POST | Progress | NVR/IPC | Pan/Tilt/Zoom | No | None (Read-only) | ✅ Verified |
| `POST /API/PreviewChannel/PTZ/Get` | POST | Get | NVR/IPC | Presets/Tours | No | None (Read-only) | ✅ Verified |
| `POST /API/Channel/PTZ/{Range,Get,Set}` | POST | Range, Get, Set | NVR/IPC | 1..256 Channels | No | Serial Baud/Proto| ✅ Verified |
| `POST /API/Schedules/PtzTasks/{Range,Get,Set}` | POST | Range, Get, Set | NVR/IPC | 1..256 Channels | No | Scheduled Patrol | ✅ Verified |
| `POST /API/AlarmConfig/PTZLinkage/{Range,Get,Set}` | POST | Range, Get, Set | NVR/IPC | 1..256 Channels | No | Trigger Preset Tour| ✅ Verified |
