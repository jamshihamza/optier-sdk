# Production C++20 VMS Architecture Specification

## Executive Overview
This document specifies the final production architecture for the **OPTIER Enterprise Video Management System (VMS)** targeting **C++20**, **Visual Studio 2022 (MSVC v143)**, and **Qt 6.7+** on Windows. The architecture is engineered for multi-device scalability (1 to 256+ cameras), deterministic real-time media decoding, and complete isolation between the HTTP Control Plane and the RTSP/RTP Media Plane.

---

## 1. System Layered Architecture

```mermaid
graph TB
    subgraph UI_Layer [Presentation Layer (Qt 6.7+ / QML)]
        LiveViewWall[Video Wall Grid 1x1..8x8]
        TimelinePlayback[Multi-Channel Timeline Scrubbing]
        AlarmDashboard[Real-time Alarm & Event Monitor]
        SearchPanel[Unified Forensic Search UI]
        ConfigDialogs[Device & Channel Config Trees]
    end

    subgraph Service_Layer [VMS Application Services (C++20 Core)]
        DeviceService[DeviceService: Multi-Device Lifecycle & Inventory]
        StreamService[StreamService: RTSP Session Dispatcher]
        EventService[EventService: Normalized Pub/Sub Event Bus]
        SearchService[SearchService: Multi-Modal Forensic Engine]
        EvidenceService[EvidenceService: Cryptographic Evidence Locker]
        AuthService[AuthService: VMS RBAC & Session Security]
    end

    subgraph Domain_Layer [Domain Models & Entities (Value Types & RAII)]
        DeviceModel[Device / DeviceInfo / ConnectionState]
        ChannelModel[CameraChannel / StreamType / AICapability]
        EventModel[VMSEvent / EventType / EventSeverity]
        EvidenceModel[EvidenceItem / ForensicTag / Checksum]
        UserModel[VMSUser / Role / ChannelPermission]
    end

    subgraph Control_Plane [Control Plane (HTTP / JSON / Digest Auth)]
        OemApiClient[OemApiClient: High-Performance HTTP Transport]
        SessionManager[SessionManager: Digest Auth & Keepalive]
        ConfigManagers[85 Core API Modules: Video, AI, Alarm, System]
    end

    subgraph Media_Plane [Media Plane (RTSP / Demux / Decode / Render)]
        RtspSession[RtspSession: TCP RTSP Client]
        Demuxer[Demuxer: H.264 / H.265 NAL Unit Parser]
        DecoderEngine[DecoderEngine: Software FFmpeg / D3D11VA]
        RingBuffer[BoundedRingBuffer: Zero-Latency Latest Frame Pool]
        VideoRenderer[Qt Quick / Direct3D11 Video Surface]
    end

    UI_Layer --> Service_Layer
    Service_Layer --> Domain_Layer
    Service_Layer --> Control_Plane
    Service_Layer --> Media_Plane
    Control_Plane --> Physical_NVR[Physical NVR / IPC (HTTP :80)]
    Media_Plane --> Physical_Stream[RTSP / RTP Stream (:554 / :80)]
```

---

## 2. Control Plane Design (C++20 Engine)

### Core Classes & Responsibilities
1. **`OemApiClient`**:
   - Asynchronous HTTP/1.1 client utilizing `QNetworkAccessManager` or `WinHTTP` with connection pooling.
   - Handles HTTP Digest Authentication (RFC 2617 / RFC 7616 MD5 `qop="auth"`).
   - Manages CSRF cookie injection (`_CSRF_COOKIE_`) and keeps session alive via non-blocking heartbeat tasks.
2. **`DeviceSession`**:
   - Manages connection lifecycle (`Disconnected` -> `Connecting` -> `Authenticating` -> `Synchronizing` -> `Online` -> `Degraded` -> `Error`).
   - Thread-safe state machine guarded by `std::shared_mutex` (reader/writer lock).
3. **`DeviceManager` / `DeviceService`**:
   - Registry maintaining `std::unordered_map<std::string, std::shared_ptr<Device>>`.
   - **Fault Isolation**: Device connection timeouts (10s) run on separate asynchronous task fibers; failure of Device B never blocks requests to Device A.

---

## 3. C++20 Idioms, RAII & Memory Ownership

| Concept | Python Prototype Approach | Production C++20 Replacement | Architectural Rationale |
| :--- | :--- | :--- | :--- |
| **Domain Entities** | Python `@dataclass` | `struct` / `class` Value Types (`std::string_view`, `std::chrono::system_clock`) | Zero GC overhead, stack allocatability, move semantics (`std::move`). |
| **Thread Synchronization** | `threading.RLock()` / `threading.Condition` | `std::mutex`, `std::shared_mutex`, `std::atomic<T>`, `std::condition_variable` | Sub-microsecond lock contention, true kernel synchronization primitives. |
| **Memory Allocation** | Dynamic Heap / PyObject GC | Custom Memory Pool & `std::pmr::polymorphic_allocator` | Eliminates heap fragmentation when handling 30 FPS video frames across 256 streams. |
| **Media Buffering** | `collections.deque(maxlen=1)` | Lockless Single-Producer Single-Consumer (SPSC) Ring Buffer | True zero-latency atomic pointer exchange between decoder thread and UI render loop. |
| **Error Handling** | Python Exception Hierarchy | `std::expected<T, ErrorCode>` / `std::error_code` | Zero-overhead deterministic error propagation without stack unwinding penalties in hot media loops. |

---

## 4. Subsystem Interfaces & Boundary Contracts

```cpp
namespace optier::vms {

// Control Plane Interface
class IDeviceService {
public:
    virtual ~IDeviceService() = default;
    virtual std::future<bool> connectDevice(const DeviceId& id) = 0;
    virtual void disconnectDevice(const DeviceId& id) = 0;
    virtual std::shared_ptr<Device> getDevice(const DeviceId& id) const = 0;
    virtual std::vector<CameraChannel> listChannels() const = 0;
};

// Media Plane Interface
class IStreamService {
public:
    virtual ~IStreamService() = default;
    virtual std::shared_ptr<StreamSession> startStream(const StreamRequest& request) = 0;
    virtual bool stopStream(const StreamRequest& request) = 0;
    virtual std::shared_ptr<VideoFrame> getLatestFrame(const StreamRequest& request) = 0;
    virtual StreamMetrics getMetrics(const StreamRequest& request) const = 0;
};

// Event Bus Interface
class IEventService {
public:
    virtual ~IEventService() = default;
    virtual void subscribe(EventType type, std::function<void(const VMSEvent&)> handler) = 0;
    virtual void publish(const VMSEvent& event) = 0;
};

} // namespace optier::vms
```
