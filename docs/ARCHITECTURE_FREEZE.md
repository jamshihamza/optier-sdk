# Production C++20 VMS Architecture Freeze Specification

## Status: FROZEN & AUTHORITATIVE

## 1. Final Project & Module Structure

```
optier-vms/
├── CMakeLists.txt                      # Root CMake Project (MSVC C++20 / Qt 6.7+)
├── src/
│   ├── app/                            # Application Entrypoint & Startup
│   │   ├── main.cpp
│   │   ├── app_context.hpp/.cpp
│   │   └── config_manager.hpp/.cpp
│   ├── domain/                         # Value Types & Pure Domain Entities
│   │   ├── types.hpp                   # Identifiers, Enums, Timestamps
│   │   ├── device.hpp/.cpp
│   │   ├── channel.hpp/.cpp
│   │   ├── media.hpp/.cpp
│   │   ├── event.hpp/.cpp
│   │   ├── evidence.hpp/.cpp
│   │   └── user.hpp/.cpp
│   ├── control/                        # Control Plane (HTTP / Digest Auth / SDK Core)
│   │   ├── http_client.hpp/.cpp
│   │   ├── digest_auth.hpp/.cpp
│   │   ├── device_session.hpp/.cpp
│   │   └── managers/                   # 85 Ported Protocol Managers (P0/P1 First)
│   │       ├── system_manager.hpp/.cpp
│   │       ├── video_manager.hpp/.cpp
│   │       ├── record_manager.hpp/.cpp
│   │       ├── ptz_manager.hpp/.cpp
│   │       ├── alarm_manager.hpp/.cpp
│   │       ├── ai_face_manager.hpp/.cpp
│   │       ├── ai_plate_manager.hpp/.cpp
│   │       └── user_manager.hpp/.cpp
│   ├── media/                          # Media Plane (RTSP / Demux / Decode / Buffering)
│   │   ├── interfaces.hpp
│   │   ├── ring_buffer.hpp             # Lockless SPSC Latest-Frame Buffer
│   │   ├── rtsp_source.hpp/.cpp        # Asynchronous TCP RTSP Ingest
│   │   ├── software_decoder.hpp/.cpp   # libavcodec AVX2 Software Decoder
│   │   ├── hardware_decoder.hpp/.cpp   # D3D11VA / DXVA2 Hardware Decoder
│   │   ├── frame_pool.hpp              # Pre-allocated Memory Frame Pool
│   │   └── stream_worker.hpp/.cpp
│   ├── services/                       # High-Level VMS Orchestration Services
│   │   ├── device_service.hpp/.cpp     # Multi-Device Lifecycle & Inventory
│   │   ├── stream_service.hpp/.cpp     # Concurrent Stream Routing & Health
│   │   ├── event_service.hpp/.cpp      # Normalized Pub/Sub Event Bus
│   │   ├── search_service.hpp/.cpp     # Forensic Timeline & AI Query Engine
│   │   ├── evidence_service.hpp/.cpp   # SHA-256 Sealed Evidence Locker
│   │   └── auth_service.hpp/.cpp       # VMS RBAC & Session Security
│   └── ui/                             # Qt 6 / QML Presentation Layer
│       ├── main_window.hpp/.cpp
│       ├── video_grid_widget.hpp/.cpp
│       ├── timeline_widget.hpp/.cpp
│       ├── alarm_panel_widget.hpp/.cpp
│       └── renderers/
│           ├── d3d11_video_surface.hpp/.cpp
│           └── software_video_surface.hpp/.cpp
├── tests/                              # GoogleTest & Benchmark Test Suite
│   ├── unit/
│   │   ├── test_domain_types.cpp
│   │   ├── test_ring_buffer.cpp
│   │   ├── test_digest_auth.cpp
│   │   └── test_event_bus.cpp
│   ├── integration/
│   │   ├── test_hardware_control.cpp   # Live Hardware NVR HTTP Tests
│   │   └── test_hardware_rtsp.cpp      # Live Hardware RTSP Streaming Tests
│   └── benchmarks/
│       ├── bench_decoder.cpp
│       └── bench_ring_buffer.cpp
└── third_party/                        # VCPKG / Submodule Dependencies
    ├── ffmpeg/                         # libavcodec, libavformat, libavutil, libswscale
    └── nlohmann_json/                  # Modern JSON for C++20
```

---

## 2. Architectural Rules & Invariants

1. **Strict Plane Separation**:
   - The Control Plane (HTTP API) and Media Plane (RTSP Video) must NEVER share threads or data pathways.
   - Video frames are NEVER transported over HTTP API calls.
2. **Memory & Thread Safety**:
   - Zero raw pointer ownership (`new`/`delete` forbidden; use `std::unique_ptr` and `std::shared_ptr`).
   - Lockless SPSC Ring Buffers between decoder threads and render loops.
   - Main GUI Thread NEVER blocks on network IO or mutex locks.
3. **Hardware Decoding Fallback**:
   - Software CPU decoding via FFmpeg `libavcodec` is the mandatory baseline.
   - Systems without NVIDIA/Intel GPUs must operate at 100% functionality without crashes.
4. **Credential Sanitization**:
   - Passwords and raw authentication hashes must NEVER be written to log files or standard output.

---

## 3. Testing Strategy
- **Unit Tests (GoogleTest)**: Domain serialization, ring buffer concurrency, Digest auth calculations, event filters.
- **Hardware Integration Tests**: Validating live NVR connection, channel discovery, PTZ control, and RTSP stream decoding.
- **Automated Stress Benchmarks**: Continuous 24-hour stability tests under 16, 32, and 64 concurrent streams measuring memory leak resistance and CPU stability.
