"""
optier_sdk.constants
====================

SDK-wide constants.

Only values that are truly global and stable should be placed here.
"""

from __future__ import annotations

# ----------------------------------------------------------------------
# SDK
# ----------------------------------------------------------------------

SDK_NAME: str = "optier_sdk"
SDK_VERSION: str = "0.1.0"

# ----------------------------------------------------------------------
# API
# ----------------------------------------------------------------------

API_PREFIX: str = "/API"

WEB_LOGIN_URI: str = "/API/Web/Login"
WEB_LOGOUT_URI: str = "/API/Web/Logout"

LOGIN_DEVICE_INFO_URI: str = "/API/Login/DeviceInfo/Get"
LOGIN_CHANNEL_INFO_URI: str = "/API/Login/ChannelInfo/Get"

LOGIN_HEARTBEAT_URI: str = "/API/Login/Heartbeat"

# ----------------------------------------------------------------------
# HTTP
# ----------------------------------------------------------------------

DEFAULT_HTTP_TIMEOUT: int = 10

DEFAULT_CONNECT_TIMEOUT: int = 10

DEFAULT_READ_TIMEOUT: int = 30

DEFAULT_HEARTBEAT_INTERVAL: int = 30

DEFAULT_API_VERSION: str = "1.0"

JSON_CONTENT_TYPE: str = "application/json"

CSRF_HEADER_NAME: str = "X-csrftoken"

# ----------------------------------------------------------------------
# JSON
# ----------------------------------------------------------------------

JSON_KEY_RESULT: str = "result"

JSON_KEY_DATA: str = "data"

JSON_KEY_ERROR_CODE: str = "error_code"

JSON_KEY_REASON: str = "reason"

JSON_RESULT_SUCCESS: str = "success"

# ----------------------------------------------------------------------
# Login
# ----------------------------------------------------------------------

DEFAULT_LOGIN_PAYLOAD = {
    "version": DEFAULT_API_VERSION,
    "data": {},
}

DEFAULT_EMPTY_PAYLOAD = {
    "version": DEFAULT_API_VERSION,
    "data": {},
}

DEFAULT_HEARTBEAT_PAYLOAD = {
    "version": DEFAULT_API_VERSION,
    "data": {
        "keep_alive": True,
    },
}