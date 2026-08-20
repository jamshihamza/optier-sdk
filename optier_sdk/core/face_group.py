from __future__ import annotations

from typing import Any


class FaceGroupManager:
    """
    AI > Recognition > Face Group (FDGroup) API.

    Manages Face Groups and Watchlists (Whitelist, Blocklist, VIP, Staff, Stranger)
    including group policies, similarity thresholds, and channel linkage alarms.
    """

    def __init__(
        self,
        client,
    ) -> None:

        self._client = client

    def get(
        self,
        msg_id: Any | None = None,
        **kwargs,
    ) -> dict[str, Any]:
        """
        Get configured Face groups, channel lists, and parameter limits.

        :param msg_id: Optional message ID tracking identifier.
        :return: Dict containing Group list, channel limits, and SupportAI flag.
        """

        payload = {"MsgId": msg_id}
        payload.update(kwargs)

        response = self._client._request(
            "/API/AI/FDGroup/Get",
            {
                "version": "1.0",
                "data": payload,
            },
        )

        return response.get(
            "data",
            {},
        )

    def get_id(
        self,
        detect_type: int = 0,
        **kwargs,
    ) -> dict[str, Any]:
        """
        Get next available Face/Vehicle group ID.

        :param detect_type: 0 for Face (DLDT_Face), 1 for Vehicle (DLDT_Car).
        :return: Dict containing available group ID.
        """

        payload = {"DetectType": detect_type}
        payload.update(kwargs)

        response = self._client._request(
            "/API/AI/FDGroup/GetId",
            {
                "version": "1.0",
                "data": payload,
            },
        )

        return response.get(
            "data",
            {},
        )

    def add(
        self,
        name: str,
        similarity: int = 70,
        detect_type: int = 0,
        policy_configs: list[dict[str, Any]] | None = None,
        **kwargs,
    ) -> dict[str, Any]:
        """
        Create a new Face group / watchlist.

        :param name: Group name (e.g. 'VIP Customers', 'Blacklist').
        :param similarity: Match similarity threshold (0..100, default 70).
        :param detect_type: 0 for Face, 1 for Car.
        :param policy_configs: Channel alarm output, buzzer, and record linkage policies.
        :return: Device response payload with created group details.
        """

        group_item: dict[str, Any] = {
            "Name": name,
            "Similarity": similarity,
            "DetectType": detect_type,
            "Enabled": 1,
        }
        if policy_configs is not None:
            group_item["PolicyConfigs"] = policy_configs
        group_item.update(kwargs)

        response = self._client._request(
            "/API/AI/FDGroup/Add",
            {
                "version": "1.0",
                "data": {
                    "MsgId": None,
                    "Group": [group_item],
                },
            },
        )

        return response.get(
            "data",
            {},
        )

    def modify(
        self,
        group_id: int,
        name: str | None = None,
        similarity: int | None = None,
        enabled: int | None = None,
        policy_configs: list[dict[str, Any]] | None = None,
        **kwargs,
    ) -> dict[str, Any]:
        """
        Modify existing Face group parameters.

        :param group_id: Unique group ID.
        :param name: Updated group name.
        :param similarity: Updated match similarity threshold (0..100).
        :param enabled: Group enable toggle (1: enabled, 0: disabled).
        :param policy_configs: Updated alarm linkage policies.
        :return: Device response payload.
        """

        group_item: dict[str, Any] = {"Id": group_id}
        if name is not None:
            group_item["Name"] = name
        if similarity is not None:
            group_item["Similarity"] = similarity
        if enabled is not None:
            group_item["Enabled"] = enabled
        if policy_configs is not None:
            group_item["PolicyConfigs"] = policy_configs
        group_item.update(kwargs)

        response = self._client._request(
            "/API/AI/FDGroup/Modify",
            {
                "version": "1.0",
                "data": {
                    "MsgId": None,
                    "Group": [group_item],
                },
            },
        )

        return response.get(
            "data",
            {},
        )

    def remove(
        self,
        group_ids: list[int],
        **kwargs,
    ) -> dict[str, Any]:
        """
        Remove one or more Face groups.

        :param group_ids: List of group IDs to remove.
        :return: Device response payload.
        """

        groups = [{"Id": gid} for gid in group_ids]

        response = self._client._request(
            "/API/AI/FDGroup/Remove",
            {
                "version": "1.0",
                "data": {
                    "MsgId": None,
                    "Group": groups,
                },
            },
        )

        return response.get(
            "data",
            {},
        )

    def change(
        self,
        group_ids: list[int],
        **kwargs,
    ) -> dict[str, Any]:
        """
        Change group priority/order sequence.

        :param group_ids: Ordered list of group IDs.
        :return: Device response payload.
        """

        groups = [{"Id": gid} for gid in group_ids]

        response = self._client._request(
            "/API/AI/FDGroup/Change",
            {
                "version": "1.0",
                "data": {
                    "MsgId": None,
                    "Group": groups,
                },
            },
        )

        return response.get(
            "data",
            {},
        )
