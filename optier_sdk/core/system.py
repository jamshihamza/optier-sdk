from ..models.system_info import SystemInfo

class SystemManager:

    def __init__(self, client):

        self._client = client

    def info(self) -> SystemInfo:

        response = self._client._request(
            "/API/SystemInfo/Base/Get"
        )

        return SystemInfo.from_dict(
            response.get("data", {})
        )