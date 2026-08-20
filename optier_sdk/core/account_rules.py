from __future__ import annotations

from typing import Any


class AccountRulesManager:
    """
    Login > Account Rules API.

    Retrieves device user security restrictions and password policies,
    including minimum/maximum lengths, character combination rules,
    special character sets, and forbidden username-password collisions.
    """

    def __init__(
        self,
        client,
    ) -> None:

        self._client = client

    def get(
        self,
        **kwargs,
    ) -> dict[str, Any]:
        """
        Get username and password rule restrictions for user account creation and modification.

        :return: Dict containing rule constraints for username, password, password_activation,
                 password_modify_ipc, and allowed character sets.
        """

        response = self._client._request(
            "/API/AccountRules/Get",
            {
                "version": "1.0",
                "data": {},
            },
        )

        return response.get(
            "data",
            {},
        )
