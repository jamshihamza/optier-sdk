"""
optier_sdk.client

Core Camera client implementation.
"""

from __future__ import annotations

import logging
import threading
from copy import deepcopy
from typing import Any

import requests
from requests.auth import HTTPDigestAuth

from .core.login import LoginManager
from .core.system import SystemManager
from .core.snapshot import SnapshotManager
from .core.datetime import DateTimeManager
from .core.defogging_fan import DefoggingFanManager
from .core.log import LogManager
from .core.system_info import SystemInfoManager





from .constants import (
    CSRF_HEADER_NAME,
    DEFAULT_EMPTY_PAYLOAD,
    DEFAULT_HEARTBEAT_INTERVAL,
    DEFAULT_HEARTBEAT_PAYLOAD,
    DEFAULT_HTTP_TIMEOUT,
    DEFAULT_LOGIN_PAYLOAD,
    JSON_CONTENT_TYPE,
    JSON_KEY_ERROR_CODE,
    JSON_KEY_REASON,
    JSON_KEY_RESULT,
    JSON_RESULT_SUCCESS,
    LOGIN_HEARTBEAT_URI,
    WEB_LOGIN_URI,
    WEB_LOGOUT_URI,
)

from .error_map import get_exception_class

from .exceptions import (
    AuthenticationError,
    ConnectionError,
    InvalidResponseError,
)


class Camera:
    """
    Main OPTIER SDK camera object.
    """

    def __init__(
        self,
        host: str,
        username: str,
        password: str,
        *,
        port: int = 80,
        https: bool = False,
        timeout: int = DEFAULT_HTTP_TIMEOUT,
        oem_type: int | None = None,
        logger: logging.Logger | None = None,
    ) -> None:

        self.host = host
        self.port = port

        self.username = username
        self.password = password

        self.timeout = timeout
        self.oem_type = oem_type

        self._logger = logger

        self.scheme = "https" if https else "http"

        self.base_url = (
            f"{self.scheme}://{self.host}:{self.port}"
        )

        #
        # HTTP session
        #

        self._session: requests.Session | None = None

        #
        # CSRF token
        #

        self._csrf_token: str | None = None

        #
        # Connection state
        #

        self._connected = False

        #
        # Thread synchronization
        #

        self._lock = threading.RLock()

        #
        # Heartbeat
        #

        self._heartbeat_interval = (
            DEFAULT_HEARTBEAT_INTERVAL
        )

        self._heartbeat_thread: (
            threading.Thread | None
        ) = None

        self._heartbeat_stop_event = (
            threading.Event()
        )

        #
        # API Managers
        #

        self.login = LoginManager(self)

        self.system = SystemManager(self)

        self.snapshot = SnapshotManager(self)

        self.datetime = DateTimeManager(self)

        self.defogging_fan = DefoggingFanManager(self)

        self.log = LogManager(self)

        self.system_info = SystemInfoManager(self)

        
    # ---------------------------------------------------------
    # Properties
    # ---------------------------------------------------------

    @property
    def connected(self) -> bool:
        """
        Current connection state.
        """
        return self._connected

    # ---------------------------------------------------------
    # Context manager
    # ---------------------------------------------------------

    def __enter__(self) -> "Camera":

        self.connect()

        return self

    def __exit__(
        self,
        exc_type,
        exc,
        tb,
    ) -> None:

        self.disconnect()

    # ---------------------------------------------------------
    # Public API
    # ---------------------------------------------------------

    def connect(self) -> None:
        """
        Connect to the device.
        """

        with self._lock:

            if self._connected:
                return

            self._session = requests.Session()

            self._login()

            self._connected = True

            self._start_heartbeat()

    def disconnect(self) -> None:
        """
        Logout and release all resources.
        """

        with self._lock:

            if not self._connected:
                return

            self._stop_heartbeat()

            try:
                self._logout()

            finally:

                if self._session is not None:
                    self._session.close()

                self._session = None

                self._csrf_token = None

                self._connected = False

    close = disconnect

    # ---------------------------------------------------------
    # Login
    # ---------------------------------------------------------

    def _login(self) -> None:
        """
        Perform Digest authentication.
        """

        if self._session is None:
            raise ConnectionError(
                "HTTP session not initialized."
            )

        payload = deepcopy(DEFAULT_LOGIN_PAYLOAD)

        if self.oem_type is not None:
            payload["data"]["oem_type"] = self.oem_type

        try:

            response = self._session.post(
                self.base_url + WEB_LOGIN_URI,
                json=payload,
                auth=HTTPDigestAuth(
                    self.username,
                    self.password,
                ),
                timeout=self.timeout,
            )

        except requests.RequestException as exc:

            raise ConnectionError(
                str(exc)
            ) from exc

        try:
            body = response.json()

        except Exception:
            body = None

        if body is not None:

            if (
                body.get(JSON_KEY_RESULT)
                != JSON_RESULT_SUCCESS
            ):

                error_code = body.get(
                    JSON_KEY_ERROR_CODE
                )

                reason = body.get(
                    JSON_KEY_REASON,
                    "Login failed.",
                )

                exception_type = (
                    get_exception_class(
                        error_code
                    )
                )

                print("\n========== OEM RESPONSE ==========")
                print(response_json)
                print("==================================\n")

                raise exception_type(reason)    

        self._csrf_token = response.headers.get(
            CSRF_HEADER_NAME
        )

        if not self._csrf_token:

            raise AuthenticationError(
                "Login succeeded but "
                "X-csrftoken is missing."
            )

        self._session.headers.update(
            {
                CSRF_HEADER_NAME: self._csrf_token,
                "Content-Type": JSON_CONTENT_TYPE,
            }
        )

    # ---------------------------------------------------------
    # Logout
    # ---------------------------------------------------------

    def _logout(self) -> None:
        """
        Logout from the device.
        """

        if self._session is None:
            return

        try:

            self._session.post(
                self.base_url + WEB_LOGOUT_URI,
                json=DEFAULT_EMPTY_PAYLOAD,
                timeout=self.timeout,
            )

        except Exception as exc:

            if self._logger is not None:

                self._logger.warning(
                    "Logout failed: %s",
                    exc,
                )

    # ---------------------------------------------------------
    # Error handling
    # ---------------------------------------------------------

    def _is_session_error(
        self,
        response_json: dict[str, Any],
    ) -> bool:

        error_code = response_json.get(
            JSON_KEY_ERROR_CODE
        )

        return error_code in (
            "expired",
            "no_login",
            "token_invalid",
        )

    def _raise_for_error(
        self,
        response_json: dict[str, Any],
    ) -> None:
        """
        Raise mapped Python exception.
        """

        if (
            response_json.get(JSON_KEY_RESULT)
            == JSON_RESULT_SUCCESS
        ):
            return

        error_code = response_json.get(
            JSON_KEY_ERROR_CODE
        )

        reason = response_json.get(
            JSON_KEY_REASON,
            "Unknown device error.",
        )

        exception_type = get_exception_class(
            error_code
        )

        print()
        print("=" * 60)
        print("OEM RESPONSE")
        print("=" * 60)
        print(response_json)
        print("=" * 60)
        print()

        raise exception_type(reason)
    # ---------------------------------------------------------
    # Core request
    # ---------------------------------------------------------

    def _request(
        self,
        api: str,
        payload: dict[str, Any] | None = None,
        *,
        timeout: int | None = None,
    ) -> dict[str, Any]:
        """
        Centralized request function.
        """

        with self._lock:

            if self._session is None:

                raise ConnectionError(
                    "Camera is not connected."
                )

            if payload is None:

                payload = deepcopy(
                    DEFAULT_EMPTY_PAYLOAD
                )

            try:

                response = self._session.post(
                    self.base_url + api,
                    json=payload,
                    timeout=timeout or self.timeout,
                )

            except requests.RequestException as exc:

                raise ConnectionError(
                    str(exc)
                ) from exc

            try:

                response_json = response.json()

            except Exception as exc:

                raise InvalidResponseError(
                    "Device returned invalid JSON."
                ) from exc

            #
            # Automatic session recovery
            #

            if self._is_session_error(
                response_json
            ):

                self._login()

                response = self._session.post(
                    self.base_url + api,
                    json=payload,
                    timeout=timeout or self.timeout,
                )

                response_json = response.json()

            self._raise_for_error(
                response_json
            )

            return response_json


    # ---------------------------------------------------------
    # Heartbeat
    # ---------------------------------------------------------

    def _heartbeat_loop(self) -> None:
        """
        Background heartbeat worker.

        Runs until the stop event is signalled.
        """

        while not self._heartbeat_stop_event.wait(
            self._heartbeat_interval
        ):

            try:

                self._request(
                    LOGIN_HEARTBEAT_URI,
                    deepcopy(
                        DEFAULT_HEARTBEAT_PAYLOAD
                    ),
                )

            except Exception as exc:

                if self._logger is not None:

                    self._logger.warning(
                        "Heartbeat failed: %s",
                        exc,
                    )

    def _start_heartbeat(self) -> None:
        """
        Start the background heartbeat thread.
        """

        if (
            self._heartbeat_thread is not None
            and self._heartbeat_thread.is_alive()
        ):
            return

        self._heartbeat_stop_event.clear()

        self._heartbeat_thread = threading.Thread(
            target=self._heartbeat_loop,
            name="OptierHeartbeat",
            daemon=True,
        )

        self._heartbeat_thread.start()

    def _stop_heartbeat(self) -> None:
        """
        Stop the background heartbeat thread.
        """

        self._heartbeat_stop_event.set()

        if self._heartbeat_thread is None:
            return

        self._heartbeat_thread.join(
            timeout=2.0
        )

        self._heartbeat_thread = None