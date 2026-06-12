# OPTIER SDK Coding Guidelines

Version: 1.0

---

# Philosophy

The OPTIER SDK is intended to be a professional-grade Python SDK.

Every line of code should be:

- Readable
- Maintainable
- Well documented
- Type safe
- Consistent
- Easy to extend

The SDK should hide OEM implementation details from SDK users.

---

# Naming Convention

## Classes

Use PascalCase.

Example:

Camera

CameraConfig

ApiResponse

DeviceInfo

ChannelInfo

---

## Functions

Use snake_case.

Example:

connect()

disconnect()

device_info()

channel_info()

search_face()

search_plate()

---

## Variables

Use snake_case.

Example:

device_name

channel_count

heartbeat_interval

session_token

---

## Constants

Use UPPER_CASE.

Example:

API_PREFIX

API_VERSION

DEFAULT_TIMEOUT

DEFAULT_PORT

---

# Public API Rule

SDK users should never need to know:

- HTTP endpoints
- Cookies
- CSRF tokens
- OEM error codes
- Raw JSON format

The SDK must expose clean Python objects.

Good:

device.channel_count

device.support_face

device.device_name

Bad:

device["channel_num"]

device["support_face"]

---

# Type Hints

Every public function must include type hints.

Example:

def connect() -> None:

def device_info() -> DeviceInfo:

---

# Dataclass Policy

Prefer dataclasses for SDK models.

Use:

@dataclass(slots=True)

unless there is a documented reason not to.

---

# Documentation

Every public class must have:

- Docstring

Every public method must have:

- Docstring

Complex logic should include explanatory comments.

Avoid unnecessary comments.

---

# Exception Policy

Never expose OEM error codes directly.

Convert OEM errors into Python exceptions.

Example:

device_busy

↓

DeviceBusyError

expired

↓

SessionExpiredError

---

# JSON Policy

Raw dictionaries should remain internal.

SDK users should interact with typed objects.

Good:

device.channel_count

Bad:

device["channel_num"]

---

# Request Policy

All HTTP communication must pass through the internal request engine.

Never call:

requests.get()

requests.post()

directly from feature modules.

---

# Future Goals

The same SDK architecture should support:

- IPC
- NVR
- DVR
- Face Recognition
- LPR
- PTZ
- Playback
- AI
- Mobile
- Cloud
- Future VMS

---

# Engineering Rule

If a better architecture is discovered before implementation,
prefer redesign over technical debt.

Readable code is preferred over clever code.

Maintainability is preferred over short code.

Correctness is preferred over convenience.