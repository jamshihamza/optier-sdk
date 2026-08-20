from __future__ import annotations

import logging
import os
import re
from typing import Any

import cv2

from .interfaces import IStreamSource

logger = logging.getLogger("optier_vms.media.rtsp_source")


def sanitize_rtsp_url(url: str) -> str:
    """
    Remove user and password credentials from an RTSP URL for safe logging.
    e.g. 'rtsp://admin:pass123@192.168.1.100:80/live' -> 'rtsp://***:***@192.168.1.100:80/live'
    """
    return re.sub(r"rtsp://[^:]+:[^@]+@", "rtsp://***:***@", url)


class RtspStreamSource(IStreamSource):
    """
    Concrete RTSP Stream Transport using OpenCV with embedded FFmpeg backend.

    Configured for reliable low-latency TCP streaming and safe credential masking.
    """

    def __init__(
        self,
        rtsp_url: str,
        transport: str = "tcp",
        buffer_size_kb: int = 1024,
    ) -> None:
        self._raw_url = rtsp_url
        self._sanitized_endpoint = sanitize_rtsp_url(rtsp_url)
        self._transport = transport
        self._buffer_size_kb = buffer_size_kb
        self._cap: cv2.VideoCapture | None = None

    @property
    def endpoint(self) -> str:
        return self._sanitized_endpoint

    @property
    def is_opened(self) -> bool:
        return self._cap is not None and self._cap.isOpened()

    def open(self) -> bool:
        """
        Open the RTSP network stream over TCP.
        """
        self.close()

        # Configure environment options for OpenCV FFmpeg capture
        # Enforces TCP transport to eliminate UDP packet loss and sets buffer size
        ffmpeg_opts = f"rtsp_transport;{self._transport}|buffer_size;{self._buffer_size_kb * 1024}"
        os.environ["OPENCV_FFMPEG_CAPTURE_OPTIONS"] = ffmpeg_opts

        try:
            logger.debug("Connecting RTSP source: %s", self._sanitized_endpoint)
            self._cap = cv2.VideoCapture(self._raw_url, cv2.CAP_FFMPEG)
            if not self._cap.isOpened():
                logger.warning("Failed to open RTSP stream: %s", self._sanitized_endpoint)
                self.close()
                return False

            # Set OpenCV internal buffer size to 1 to reduce frame buffering latency
            self._cap.set(cv2.CAP_PROP_BUFFERSIZE, 1)
            logger.debug("Successfully connected to RTSP stream: %s", self._sanitized_endpoint)
            return True

        except Exception as exc:
            logger.error("Exception opening RTSP stream %s: %s", self._sanitized_endpoint, exc)
            self.close()
            return False

    def read_frame(self) -> tuple[bool, Any]:
        """
        Read next raw video frame from the active stream.
        """
        if not self.is_opened or self._cap is None:
            return False, None

        try:
            ret, frame = self._cap.read()
            return ret, frame
        except Exception as exc:
            logger.error("Error reading frame from %s: %s", self._sanitized_endpoint, exc)
            return False, None

    def close(self) -> None:
        """
        Release VideoCapture and reset state.
        """
        if self._cap is not None:
            try:
                self._cap.release()
            except Exception as exc:
                logger.debug("Error closing VideoCapture: %s", exc)
            self._cap = None
