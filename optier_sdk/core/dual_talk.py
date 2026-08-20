from __future__ import annotations

from typing import Any


class DualTalkManager:
    """
    PreviewChannel > DualTalk (Two-Way Audio Intercom Information & Control) APIs.
    """

    def __init__(
        self,
        client,
    ) -> None:

        self._client = client

    def get(
        self,
        channel: str = "CH1",
        command_flag: bool = False,
        **kwargs,
    ) -> dict[str, Any]:
        """
        Get two-way audio intercom status for a channel.
        """

        payload = {
            "channel": channel,
            "command_flag": command_flag,
        }
        payload.update(kwargs)

        response = self._client._request(
            "/API/PreviewChannel/DualTalk/Get",
            {
                "version": "1.0",
                "data": payload,
            },
        )

        return response.get(
            "data",
            {},
        )

    def set(
        self,
        channel: str = "CH1",
        action: int = 1,
        **kwargs,
    ) -> None:
        """
        Control two-way audio intercom for a channel (action: 1=open, 0=close).
        """

        payload = {
            "channel": channel,
            "action": action,
        }
        payload.update(kwargs)

        self._client._request(
            "/API/PreviewChannel/DualTalk/Set",
            {
                "version": "1.0",
                "data": payload,
            },
        )
