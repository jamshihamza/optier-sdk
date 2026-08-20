from __future__ import annotations

from typing import Any


class PlateGroupManager:
    """
    AI > Recognition > PlateGroup (License Plate Groups & Watchlists) API.

    Manages License Plate Watchlist groups (Allow List / Whitelist, Block List / Blacklist,
    Unknown / Visitor) including matching similarity thresholds and alarm output linkages.
    """

    def __init__(
        self,
        client,
    ) -> None:

        self._client = client

    def get(
        self,
        groups_id: list[int] | None = None,
        simple_info: int = 1,
        default_val: int = 0,
        **kwargs,
    ) -> dict[str, Any]:
        """
        Get configured License Plate Watchlist groups.

        :param groups_id: Optional list of group IDs to filter. Empty list returns all groups.
        :param simple_info: 1 for simple summary (Name, Id, DetectType, Policy, Enabled), 0 for full config.
        :param default_val: 0 for actual runtime params, 1 for default alarm params.
        :return: Dict containing Group list, channel limits, and SupportAI flag.
        """

        payload: dict[str, Any] = {
            "MsgId": "",
            "DefaultVal": default_val,
            "SimpleInfo": simple_info,
            "GroupsId": groups_id if groups_id is not None else [],
        }
        payload.update(kwargs)

        response = self._client._request(
            "/API/AI/PlateGroup/Get",
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
        detect_type: int = 2,
        **kwargs,
    ) -> dict[str, Any]:
        """
        Get next available License Plate group ID.

        :param detect_type: Fixed as 2 (DLDT_Plate).
        :return: Dict containing available group ID.
        """

        payload = {"DetectType": detect_type}
        payload.update(kwargs)

        response = self._client._request(
            "/API/AI/PlateGroup/GetId",
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
        similarity: int = 1,
        detect_type: int = 2,
        policy_configs: list[dict[str, Any]] | None = None,
        **kwargs,
    ) -> dict[str, Any]:
        """
        Add a new license plate group.

        :param name: Group name (e.g. 'Authorized Employees', 'Denied Access').
        :param similarity: Match similarity tolerance.
        :param detect_type: Fixed as 2 for Plate group.
        :param policy_configs: Alarm output and recording linkage policies.
        :return: Device response payload.
        """

        group_item: dict[str, Any] = {
            "Name": name,
            "Similarity": similarity,
            "DetectType": detect_type,
            "Enabled": 1,
            "EnableAlarm": 1,
        }
        if policy_configs is not None:
            group_item["PolicyConfigs"] = policy_configs
        group_item.update(kwargs)

        response = self._client._request(
            "/API/AI/PlateGroup/Add",
            {
                "version": "1.0",
                "data": {
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
        enable_alarm: int | None = None,
        policy_configs: list[dict[str, Any]] | None = None,
        **kwargs,
    ) -> dict[str, Any]:
        """
        Modify existing license plate group configuration.

        :param group_id: Unique group ID.
        :param name: Updated group name.
        :param similarity: Updated similarity threshold.
        :param enabled: Group enable toggle.
        :param enable_alarm: Alarm linkage toggle.
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
        if enable_alarm is not None:
            group_item["EnableAlarm"] = enable_alarm
        if policy_configs is not None:
            group_item["PolicyConfigs"] = policy_configs
        group_item.update(kwargs)

        response = self._client._request(
            "/API/AI/PlateGroup/Modify",
            {
                "version": "1.0",
                "data": {
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
        Remove license plate groups.

        :param group_ids: List of group IDs to remove.
        :return: Device response payload.
        """

        groups = [{"Id": gid} for gid in group_ids]

        response = self._client._request(
            "/API/AI/PlateGroup/Remove",
            {
                "version": "1.0",
                "data": {
                    "Group": groups,
                },
            },
        )

        return response.get(
            "data",
            {},
        )
