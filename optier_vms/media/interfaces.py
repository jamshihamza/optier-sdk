from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any

from ..domain.media import VideoFrame


class IStreamSource(ABC):
    """
    Abstract stream transport interface.

    Encapsulates network socket, demuxing, and packet/frame acquisition
    without exposing third-party library types to the domain.
    """

    @property
    @abstractmethod
    def endpoint(self) -> str:
        """
        Returns sanitized stream endpoint description (credentials stripped).
        """
        ...

    @abstractmethod
    def open(self) -> bool:
        """
        Establish connection to the stream endpoint.
        """
        ...

    @abstractmethod
    def read_frame(self) -> tuple[bool, Any]:
        """
        Acquire raw frame data / packet from the stream.

        :return: (success: bool, raw_data: Any)
        """
        ...

    @abstractmethod
    def close(self) -> None:
        """
        Disconnect and release all transport socket and buffer resources.
        """
        ...

    @property
    @abstractmethod
    def is_opened(self) -> bool:
        """
        Check if the transport connection is currently active.
        """
        ...


class IVideoDecoder(ABC):
    """
    Abstract video decoder interface.

    Transforms raw demuxed frame/packet data into normalized VMS VideoFrame objects.
    """

    @abstractmethod
    def decode(self, raw_data: Any, frame_number: int = 0) -> VideoFrame | None:
        """
        Decode raw data into a VMS VideoFrame.
        """
        ...

    @abstractmethod
    def reset(self) -> None:
        """
        Flush internal decoder state (e.g. on stream reconnect or seek).
        """
        ...

    @abstractmethod
    def close(self) -> None:
        """
        Release decoder hardware/software context.
        """
        ...


class IFrameSink(ABC):
    """
    Abstract frame consumer interface (e.g. UI Renderer, AI Engine, Video Saver).
    """

    @abstractmethod
    def on_frame(self, frame: VideoFrame) -> None:
        """
        Handle a newly decoded video frame.
        """
        ...
