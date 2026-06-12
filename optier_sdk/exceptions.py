"""
optier_sdk.exceptions
=====================

Custom exception hierarchy for the OPTIER SDK.

SDK users should work with Python exceptions instead of OEM
error codes or raw HTTP responses.
"""

from __future__ import annotations


class OptierSDKError(Exception):
    """
    Base exception for all SDK errors.
    """


# ------------------------------------------------------------------
# Connection / Authentication
# ------------------------------------------------------------------


class ConnectionError(OptierSDKError):
    """
    Unable to communicate with the device.
    """


class AuthenticationError(OptierSDKError):
    """
    Authentication failed.
    """


class VerifyFailedError(AuthenticationError):
    """
    Wrong username or password.
    """


class LoginBlockedError(AuthenticationError):
    """
    Login blocked due to repeated failures.
    """


class PermissionDeniedError(AuthenticationError):
    """
    User has insufficient permission.
    """


class BlacklistedIPError(AuthenticationError):
    """
    Client IP is blacklisted.
    """


class DeviceRebootingError(AuthenticationError):
    """
    Device is rebooting.
    """


class SessionExpiredError(AuthenticationError):
    """
    Session has expired.
    """


class InvalidTokenError(AuthenticationError):
    """
    CSRF token or session token is invalid.
    """


# ------------------------------------------------------------------
# Device Errors
# ------------------------------------------------------------------


class DeviceBusyError(OptierSDKError):
    """
    Device is busy.
    """


class OperationFailedError(OptierSDKError):
    """
    Device operation failed.
    """


class ParameterError(OptierSDKError):
    """
    Invalid parameter supplied.
    """


class UnsupportedError(OptierSDKError):
    """
    Feature not supported by device.
    """


class SaveFailedError(OptierSDKError):
    """
    Failed to save configuration.
    """


# ------------------------------------------------------------------
# Response Errors
# ------------------------------------------------------------------


class InvalidResponseError(OptierSDKError):
    """
    Device returned an unexpected response.
    """


class JsonDecodeError(InvalidResponseError):
    """
    Device returned invalid JSON.
    """