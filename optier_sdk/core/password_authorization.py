from __future__ import annotations

from typing import Any


class PasswordAuthorizationManager:
    """
    Login > Recover Password > Authorization API.

    Manages password recovery authorization verification policies,
    security question answer challenges, email verification codes,
    certificate authentication, and emergency super password verification.
    """

    def __init__(
        self,
        client,
    ) -> None:

        self._client = client

    def range(
        self,
        **kwargs,
    ) -> dict[str, Any]:
        """
        Get supported password recovery authorization modes and question constraints.

        :return: Dict containing supported modes (Answer, Email, Certificate, SuperPwd)
                 and security question slots.
        """

        response = self._client._request(
            "/API/RecoverPassword/Authorization/Range",
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
        **kwargs,
    ) -> dict[str, Any]:
        """
        Get active password recovery authorization verification configuration.

        :return: Dict containing active authorization mode and selected security questions.
        """

        response = self._client._request(
            "/API/RecoverPassword/Authorization/Get",
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
        enc_answers: dict[str, Any] | None = None,
        answer_flag: bool | None = None,
        email_flag: bool | None = None,
        certificate_flag: bool | None = None,
        super_pwd_flag: bool | None = None,
        **kwargs,
    ) -> dict[str, Any]:
        """
        Set password recovery authorization challenge and verification configuration.

        :param questions: List of security question indexes (e.g. [1, 2, 3]).
        :param enc_answers: Encrypted answer structure with peer_key and cipher.
        :param answer_flag: Enable security question answers.
        :param email_flag: Enable email recovery code.
        :param certificate_flag: Enable certificate export recovery.
        :param super_pwd_flag: Enable emergency super password recovery.
        :return: Device response payload.
        """

        payload: dict[str, Any] = {}
        if questions is not None:
            payload["questions"] = questions
        if enc_answers is not None:
            payload["enc_answers"] = enc_answers
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
            "/API/RecoverPassword/Authorization/Set",
            {
                "version": "1.0",
                "data": payload,
            },
        )

        return response.get(
            "data",
            {},
        )
