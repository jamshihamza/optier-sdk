from __future__ import annotations

from typing import Any

from .dual_talk import DualTalkManager
from .floodlight_audio_alarm import FloodlightAudioAlarmManager
from .manual_alarm import ManualAlarmManager
from .preview_ptz import PreviewPTZManager


class PreviewChannelManager:
    """
    PreviewChannel (Unified Live Preview Operational Control: PTZ, DualTalk, Floodlight & Audio Alarm, Manual Alarm) APIs.
    """

    def __init__(
        self,
        client,
    ) -> None:

        self._client = client
        self.manual_alarm = ManualAlarmManager(client)
        self.floodlight_audio_alarm = FloodlightAudioAlarmManager(client)
        self.dual_talk = DualTalkManager(client)
        self.ptz = PreviewPTZManager(client)
