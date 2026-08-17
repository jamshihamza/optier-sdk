from __future__ import annotations

from typing import Any


class IntelligentAnalysisManager:
    """
    Alarm / IVA > Intelligent Analysis (Statistical Counting Reports) APIs.
    """

    def __init__(
        self,
        client,
    ) -> None:

        self._client = client

    def range(
        self,
        page_type: str | None = None,
    ) -> dict[str, Any]:
        """
        Get parameter range for Intelligent Analysis statistical reports.

        :param page_type: Optional page type, e.g. "ChannelConfig", "AlarmConfig".
        """

        data: dict[str, Any] = {}
        if page_type is not None:
            data["page_type"] = page_type

        response = self._client._request(
            "/API/Intelligent/IntelligentAnalysis/Range",
            {
                "version": "1.0",
                "data": data,
            },
        )

        return response.get(
            "data",
            {},
        )

    def get(
        self,
        channels: list[str] | None = None,
        channel_info: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        """
        Get active Intelligent Analysis statistical reports or channel query results.

        :param channels: Optional list of channel identifiers, e.g. ["CH1", "CH2"].
        :param channel_info: Optional query specification per channel (e.g. report_type, cross_type, detection_type, search_date).
        """

        data: dict[str, Any] = {}
        if channels is not None:
            data["channel"] = channels
        if channel_info is not None:
            data["channel_info"] = channel_info

        response = self._client._request(
            "/API/Intelligent/IntelligentAnalysis/Get",
            {
                "version": "1.0",
                "data": data,
            },
        )

        return response.get(
            "data",
            {},
        )

    def set(
        self,
        **kwargs,
    ) -> None:
        """
        Set Intelligent Analysis configuration.
        """

        self._client._request(
            "/API/Intelligent/IntelligentAnalysis/Set",
            {
                "version": "1.0",
                "data": kwargs,
            },
        )
