from __future__ import annotations

from typing import Any


class PushSubscribeManager:
    """
    Push > PushSubscribe API.

    Manages mobile/client alarm event push notification subscriptions across
    all hardware alarm triggers (HDD, fan abnormal, IO, motion, PIR, video loss)
    and AI analytics triggers (Face, LPR, Line Crossing, Intrusion, SOD, Sound,
    Human/Vehicle detection) using channel bitmask flags.
    """

    def __init__(
        self,
        client,
    ) -> None:

        self._client = client

    def get(
        self,
        app_support_ai_notification_subscribe: bool = True,
    ) -> dict[str, Any]:
        """
        Retrieve current push subscription settings and channel bitmask flags.

        :param app_support_ai_notification_subscribe: Whether the client app supports AI push notifications.
        :return: Dict containing subscription configurations for HddAlarm, FansAbnormalAlarm,
                 IOAlarm, MotionAlarm, PIRAlarm, SmartAlarm, VideoLoss, FaceAlarm, LPRAlarm,
                 and individual AI detection event categories.
        """

        response = self._client._request(
            "/API/PushSubscribe/Get",
            {
                "version": "1.0",
                "data": {
                    "app_support_ai_notification_subscribe": app_support_ai_notification_subscribe,
                },
            },
        )

        return response.get(
            "data",
            {},
        )

    def set(
        self,
        data: dict[str, Any] | None = None,
        **kwargs,
    ) -> dict[str, Any]:
        """
        Update push notification subscription settings.

        :param data: Complete push subscription configuration dictionary.
        :param kwargs: Key-value updates for specific alarm subscription categories.
        :return: Device response payload.
        """

        if data is not None:
            payload = dict(data)
        else:
            current = self.get()
            payload = dict(current)

        payload.update(kwargs)

        response = self._client._request(
            "/API/PushSubscribe/Set",
            {
                "version": "1.0",
                "data": payload,
            },
        )

        return response.get(
            "data",
            {},
        )
