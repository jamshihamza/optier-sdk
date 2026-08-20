from __future__ import annotations

from typing import Any


class RecoverPasswordManager:
    """
    Login > RecoverPassword API.

    Controls password recovery configuration, security questions and answers,
    recovery email registration, certificate retrieval flags, and super password
    support across the device.
    """

    def __init__(
        self,
        client,
    ) -> None:

        self._client = client

    def range(
        self,
    ) -> dict[str, Any]:
        """
        Get capability parameters and range limits for Password Recovery configuration.

        :return: Dict containing answer_flag, certificate_flag, super_pwd_flag,
                 available questions (1..15), enc_answers length limits, and email constraints.
        """

        response = self._client._request(
            "/API/RecoverPassword/Range",
            {
                "version": "1.0",
                "data": {},
            },
        )

        return response.get(
            "data",
            {},
        )

    def get(
        self,
    ) -> dict[str, Any]:
        """
        Retrieve current active password recovery configuration.

        :return: Dict containing configured security questions array.
        """

        response = self._client._request(
            "/API/RecoverPassword/Get",
            {
                "version": "1.0",
                "data": {},
            },
        )

        return response.get(
            "data",
            {},
        )

    def set(
        self,
        questions: list[int] | None = None,
        answers: list[str] | None = None,
        email: str | None = None,
        answer_flag: bool | None = None,
        email_flag: bool | None = None,
        certificate_flag: bool | None = None,
        super_pwd_flag: bool | None = None,
        **kwargs,
    ) -> dict[str, Any]:
        """
        Update Password Recovery configuration.

        :param questions: Array of 3 question IDs (chosen from 1..15).
        :param answers: Array of 3 answer strings.
        :param email: Notification/recovery email address.
        :param answer_flag: Enable question and answer retrieval.
        :param email_flag: Enable email recovery.
        :param certificate_flag: Enable certificate recovery.
        :param super_pwd_flag: Enable super password recovery.
        :return: Device response payload.
        """

        payload: dict[str, Any] = {}

        if questions is not None:
            payload["questions"] = questions
        if answers is not None:
            payload["answers"] = answers
        if email is not None:
            payload["email"] = email
        if answer_flag is not None:
            payload["answer_flag"] = answer_flag
        if email_flag is not None:
            payload["email_flag"] = email_flag
        if certificate_flag is not None:
            payload["certificate_flag"] = certificate_flag
        if super_pwd_flag is not None:
            payload["super_pwd_flag"] = super_pwd_flag

        payload.update(kwargs)

        response = self._client._request(
            "/API/RecoverPassword/Set",
            {
                "version": "1.0",
                "data": payload,
            },
        )

        return response.get(
            "data",
            {},
        )
