"""
optier_sdk.error_map
====================

Maps OEM error_code values to Python exceptions.
"""

from __future__ import annotations

from .exceptions import (
    AuthenticationError,
    BlacklistedIPError,
    DeviceBusyError,
    DeviceRebootingError,
    InvalidTokenError,
    LoginBlockedError,
    OperationFailedError,
    ParameterError,
    PermissionDeniedError,
    SaveFailedError,
    SessionExpiredError,
    UnsupportedError,
    VerifyFailedError,
)

# ------------------------------------------------------------------
# OEM error_code -> Python Exception
# ------------------------------------------------------------------

ERROR_MAP = {
    # Generic
    "param_error": ParameterError,
    "no_permission": PermissionDeniedError,
    "no_support": UnsupportedError,
    "device_busy": DeviceBusyError,
    "operation_failed": OperationFailedError,
    "save_failed": SaveFailedError,

    # Authentication
    "verify_failed": VerifyFailedError,
    "login_failed_or_block": LoginBlockedError,
    "black_ip": BlacklistedIPError,
    "device_reboot": DeviceRebootingError,

    # Session
    "expired": SessionExpiredError,
    "no_login": SessionExpiredError,
    "token_invalid": InvalidTokenError,

    # Fallback
    "login_at_other": AuthenticationError,
    "user_locked_login": AuthenticationError,
    "user_expired_login": AuthenticationError,
}


def get_exception_class(error_code: str):
    """
    Return the mapped Python exception class.

    Unknown OEM error codes fall back to OperationFailedError.
    """
    return ERROR_MAP.get(error_code, OperationFailedError)