from __future__ import annotations

from typing import Any


class SystemUserManager:
    """
    System > Multi-User Account Management API.

    Manages NVR multi-user accounts, user creation, password updates,
    account enable/disable toggles, login limits, and user permissions
    across all local and remote channels (CH1..CH256).
    """

    def __init__(
        self,
        client,
    ) -> None:

        self._client = client

    def range(
        self,
        user_info: dict[str, Any] | None = None,
        **kwargs,
    ) -> dict[str, Any]:
        """
        Get parameter range and capacity limits for user account management.

        :param user_info: Optional filter dict.
        :return: Dict containing user_info capability definitions and limits.
        """

        payload: dict[str, Any] = {}
        if user_info is not None:
            payload["user_info"] = user_info
        payload.update(kwargs)

        response = self._client._request(
            "/API/SystemConfig/User/Range",
            {
                "version": "1.0",
                "data": payload,
            },
        )

        return response.get(
            "data",
            {},
        )

    def get(
        self,
        user_info: dict[str, Any] | None = None,
        **kwargs,
    ) -> dict[str, Any]:
        """
        Get configured user accounts, usernames, enable flags, and channel permissions.

        :param user_info: Optional filter dict.
        :return: Dict mapping user slots (e.g. 'ADMIN', 'USER1') to account profiles and permissions.
        """

        payload: dict[str, Any] = {}
        if user_info is not None:
            payload["user_info"] = user_info
        payload.update(kwargs)

        response = self._client._request(
            "/API/SystemConfig/User/Get",
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
        user_info: dict[str, Any],
        **kwargs,
    ) -> dict[str, Any]:
        """
        Update user account credentials, enable status, or permissions.

        :param user_info: Dict mapping user slots (e.g. 'USER1') to updated account settings.
        :return: Device response payload.
        """

        payload: dict[str, Any] = {
            "user_info": user_info,
        }
        payload.update(kwargs)

        response = self._client._request(
            "/API/SystemConfig/User/Set",
            {
                "version": "1.0",
                "data": payload,
            },
        )

        return response.get(
            "data",
            {},
        )
