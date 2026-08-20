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
from .core.auto_reboot import AutoRebootManager
from .core.log import LogManager
from .core.system_info import SystemInfoManager
from .core.ntp import NTPManager
from .core.general import GeneralManager
from .core.network_state import NetworkStateManager
from .core.network_base import NetworkBaseManager
from .core.onvif import OnvifManager
from .core.ip_filter import IPFilterManager
from .core.email import EmailManager
from .core.ftp import FTPManager
from .core.ddns import DDNSManager
from .core.https import HTTPSManager
from .core.rtsp import RTSPManager
from .core.snmp import SNMPManager
from .core.ieee8021x import IEEE8021xManager
from .core.ipv6 import IPv6Manager
from .core.voice_assistant import VoiceAssistantManager
from .core.gbt28181 import GBT28181Manager
from .core.tuya import TuyaManager
from .core.wlan_scan import WLANScanManager
from .core.ip_channel import IPChannelManager
from .core.remote_dev import RemoteDevManager
from .core.ptz import PTZManager
from .core.protocol_manage import ProtocolManageManager
from .core.ptz_tasks import PTZTasksManager
from .core.roi import ROIManager
from .core.analog_channel import AnalogChannelManager
from .core.manual_alarm import ManualAlarmManager
from .core.floodlight_audio_alarm import FloodlightAudioAlarmManager
from .core.dual_talk import DualTalkManager
from .core.preview_ptz import PreviewPTZManager
from .core.preview_channel import PreviewChannelManager
from .core.search_month import SearchMonthManager
from .core.search_record import SearchRecordManager
from .core.picture_playback import PicturePlaybackManager
from .core.record_tag import RecordTagManager
from .core.playback_page import PlaybackPageManager
from .core.record_info import RecordInfoManager
from .core.record_config import RecordConfigManager
from .core.disk import DiskManager
from .core.storage_cloud import StorageCloudManager
from .core.channel_info import SystemChannelInfoManager
from .core.output import OutputManager
from .core.dst import DSTManager
from .core.encode import EncodeManager
from .core.video_color import VideoColorManager
from .core.osd import OSDManager
from .core.image_control import ImageControlManager
from .core.video_cover import VideoCoverManager
from .core.motion_alarm import MotionAlarmManager
from .core.exception_alarm import ExceptionAlarmManager
from .core.line_crossing_alarm import LineCrossingAlarmManager
from .core.perimeter_intrusion_alarm import PerimeterIntrusionAlarmManager
from .core.occlusion_alarm import OcclusionAlarmManager
from .core.face_detection import FaceDetectionManager
from .core.pedestrian_detection import PedestrianDetectionManager
from .core.cross_counting import CrossCountingManager
from .core.stationary_object_detection import StationaryObjectDetectionManager
from .core.sound_detection import SoundDetectionManager
from .core.io_alarm import IOAlarmManager
from .core.disarming import DisarmingManager
from .core.ptz_linkage import PTZLinkageManager
from .core.intelligent_analysis import IntelligentAnalysisManager
from .core.rtsp_url import RtspUrlManager
from .core.search_record import SearchRecordManager
from .core.record_tag import RecordTagManager
from .core.playback_rtsp import PlaybackRtspManager


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
        self.auto_reboot = AutoRebootManager(self)

        self.log = LogManager(self)
        self.system_info = SystemInfoManager(self)
        self.ntp = NTPManager(self)
        self.general=GeneralManager(self)
        self.network_state = NetworkStateManager(self)
        self.network_base = NetworkBaseManager(self)
        self.onvif = OnvifManager(self)
        self.ip_filter = IPFilterManager(self)
        self.email = EmailManager(self)
        self.ftp = FTPManager(self)
        self.ddns = DDNSManager(self)
        self.https = HTTPSManager(self)
        self.rtsp = RTSPManager(self)
        self.snmp = SNMPManager(self)
        self.ieee8021x = IEEE8021xManager(self)
        self.ipv6 = IPv6Manager(self)
        self.voice_assistant = VoiceAssistantManager(self)
        self.gbt28181 = GBT28181Manager(self)
        self.tuya = TuyaManager(self)
        self.wlan_scan = WLANScanManager(self)
        self.ip_channel = IPChannelManager(self)
        self.remote_dev = RemoteDevManager(self)
        self.ptz = PTZManager(self)
        self.protocol_manage = ProtocolManageManager(self)
        self.ptz_tasks = PTZTasksManager(self)
        self.roi = ROIManager(self)
        self.analog_channel = AnalogChannelManager(self)
        self.manual_alarm = ManualAlarmManager(self)
        self.floodlight_audio_alarm = FloodlightAudioAlarmManager(self)
        self.dual_talk = DualTalkManager(self)
        self.preview_ptz = PreviewPTZManager(self)
        self.preview_channel = PreviewChannelManager(self)
        self.search_month = SearchMonthManager(self)
        self.search_record = SearchRecordManager(self)
        self.picture_playback = PicturePlaybackManager(self)
        self.record_tag = RecordTagManager(self)
        self.playback_page = PlaybackPageManager(self)
        self.record_info = RecordInfoManager(self)
        self.record_config = RecordConfigManager(self)
        self.disk = DiskManager(self)
        self.storage_cloud = StorageCloudManager(self)
        self.channel_info = SystemChannelInfoManager(self)
        self.output = OutputManager(self)
        self.dst = DSTManager(self)
        self.encode = EncodeManager(self)
        self.video_color = VideoColorManager(self)
        self.osd = OSDManager(self)
        self.image_control = ImageControlManager(self)
        self.video_cover = VideoCoverManager(self)
        self.motion_alarm = MotionAlarmManager(self)
        self.exception_alarm = ExceptionAlarmManager(self)
        self.line_crossing_alarm = LineCrossingAlarmManager(self)
        self.perimeter_intrusion_alarm = PerimeterIntrusionAlarmManager(self)
        self.occlusion_alarm = OcclusionAlarmManager(self)
        self.face_detection = FaceDetectionManager(self)
        self.pedestrian_detection = PedestrianDetectionManager(self)
        self.cross_counting = CrossCountingManager(self)
        self.stationary_object_detection = StationaryObjectDetectionManager(self)
        self.sound_detection = SoundDetectionManager(self)
        self.io_alarm = IOAlarmManager(self)
        self.disarming = DisarmingManager(self)
        self.ptz_linkage = PTZLinkageManager(self)
        self.intelligent_analysis = IntelligentAnalysisManager(self)
        self.rtsp_url = RtspUrlManager(self)
        self.search_record = SearchRecordManager(self)
        self.record_tag = RecordTagManager(self)
        self.playback_rtsp = PlaybackRtspManager(self)

        
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
                print(body)
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