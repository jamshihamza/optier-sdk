# Production C++20 VMS Threading Architecture

## Executive Overview
This document specifies the thread ownership, task scheduler, inter-thread synchronization primitives, and lock hierarchies for the production **C++20 OPTIER VMS**. The threading model is strictly designed to avoid thread explosion, deadlocks, and UI stutter when managing up to 256 cameras.

---

## 1. Thread Pool Taxonomy & Responsibility Matrix

```mermaid
graph TD
    subgraph UI_Thread_Domain [1. Main GUI Thread (Qt Event Loop)]
        UI_Loop[Qt Event Loop / QML Render Frame / User Input]
    end

    subgraph Control_Domain [2. Control Plane Worker Pool (2-4 Threads)]
        HTTP_Worker[Async HTTP / Digest Auth / Heartbeat / Config Requests]
    end

    subgraph Media_IO_Domain [3. Media Network IO Pool (Asynchronous IOCP / 2 Threads)]
        RTSP_IO[RTSP Handshake / RTP Demuxer / Packet Receive]
    end

    subgraph Decode_Domain [4. Video Decoder Thread Pool (N CPU Cores)]
        DEC_1[Decoder Worker 1]
        DEC_2[Decoder Worker 2]
        DEC_N[Decoder Worker N]
    end

    subgraph Event_Domain [5. Background Event & Analytics Fiber (1 Thread)]
        Event_Loop[Event Normalization / Rule Linkage Engine / DB Write]
    end

    UI_Loop -. Non-blocking Request .-> Control_Domain
    Control_Domain -. Signal Completion .-> UI_Loop
    RTSP_IO --> Decode_Domain
    Decode_Domain -. Lockless SPSC RingBuffer .-> UI_Loop
    Event_Domain -. Qt Queued Connection .-> UI_Loop
```

| Thread Pool | Size / Thread Count | Scheduling Priority | Core Responsibilities |
| :--- | :---: | :---: | :--- |
| **Main UI Thread** | Exactly 1 | `THREAD_PRIORITY_NORMAL` | Qt 6 Event loop, window management, user interactions, Direct3D11 render swaps. **NEVER BLOCKS ON IO.** |
| **Control Plane Pool** | 2 – 4 Threads | `THREAD_PRIORITY_BELOW_NORMAL` | HTTP requests to NVR/IPC, Digest Auth challenges, heartbeat keepalives, PTZ commands. |
| **RTSP Network IO Pool** | 2 Threads (IOCP / `boost::asio`) | `THREAD_PRIORITY_ABOVE_NORMAL` | Asynchronous multiplexed TCP socket reads, RTP demuxing, and NAL unit slicing. |
| **Video Decoder Pool** | `std::clamp(cores - 2, 2, 16)` | `THREAD_PRIORITY_ABOVE_NORMAL` | H.264/H.265 software decompression via FFmpeg `libavcodec` with AVX2 optimizations. |
| **Event & Rule Bus** | Exactly 1 | `THREAD_PRIORITY_NORMAL` | Normalized event routing, linkage actions, local SQLite database logging, evidence packaging. |

---

## 2. Inter-Thread Communication & Synchronization Rules

1. **GUI Thread Non-Blocking Rule**:
   - The Main UI thread must NEVER acquire blocking mutexes or make synchronous network calls.
   - All service requests return `std::future<T>` or dispatch results back to Qt slots via `QMetaObject::invokeMethod(..., Qt::QueuedConnection)`.
2. **Lockless Media Handoff**:
   - Frames move from the Video Decoder Worker to the UI Renderer via `LocklessLatestRingBuffer<VideoFrame, 1>`.
   - Consumer reads use atomic index operations (`std::memory_order_acquire` / `std::memory_order_release`) with zero mutex overhead.
3. **Lock Hierarchy to Prevent Deadlocks**:
   - `DeviceManagerMutex` (Level 1) -> `DeviceSessionMutex` (Level 2) -> `StreamWorkerMutex` (Level 3).
   - Locks must always be acquired in strict descending hierarchy order. Acquiring a Level 1 lock while holding a Level 2 lock is strictly forbidden.

---

## 3. Worker Lifecycle & Deterministic Teardown

```cpp
namespace optier::vms::threading {

class StreamWorkerThread {
public:
    void start() {
        stop_flag_.store(false, std::memory_order_relaxed);
        thread_ = std::jthread([this](std::stop_token st) { run(st); });
    }

    void stop() {
        stop_flag_.store(true, std::memory_order_release);
        if (thread_.joinable()) {
            thread_.request_stop();
            thread_.join();
        }
    }

private:
    void run(std::stop_token st) {
        while (!st.stop_requested() && !stop_flag_.load(std::memory_order_acquire)) {
            // Process demuxed packet and push to lockless ring buffer
        }
    }

    std::atomic<bool> stop_flag_{false};
    std::jthread thread_;
};

} // namespace optier::vms::threading
```
