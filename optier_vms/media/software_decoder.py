from __future__ import annotations

from datetime import datetime, timezone
import logging
from typing import Any

from ..domain.media import PixelFormat, VideoFrame
from .interfaces import IVideoDecoder

logger = logging.getLogger("optier_vms.media.software_decoder")


class SoftwareVideoDecoder(IVideoDecoder):
    """
    Software CPU Video Decoder.

    Converts raw demuxed image buffers into normalized VMS VideoFrame instances.
    """

    def __init__(self, target_format: PixelFormat = PixelFormat.BGR24) -> None:
        self._target_format = target_format
        self._frame_count = 0

    def decode(self, raw_data: Any, frame_number: int = 0) -> VideoFrame | None:
        """
        Transform raw image data into a VMS VideoFrame.
        """
        if raw_data is None:
            return None

        # When raw_data is a numpy ndarray (e.g. from OpenCV VideoCapture)
        if hasattr(raw_data, "shape"):
            shape = raw_data.shape
            if len(shape) < 2:
                return None
            height, width = shape[0], shape[1]
            self._frame_count += 1
            idx = frame_number if frame_number > 0 else self._frame_count

            return VideoFrame(
                width=width,
                height=height,
                pixel_format=self._target_format,
                timestamp=datetime.now(timezone.utc),
                frame_number=idx,
                data=raw_data,
            )

        return None

    def reset(self) -> None:
        """
        Reset internal frame counters on reconnect or flush.
        """
        self._frame_count = 0

    def close(self) -> None:
        """
        Release decoder context.
        """
        self.reset()
