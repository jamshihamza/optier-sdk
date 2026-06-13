from __future__ import annotations

import base64


class SnapshotManager:
    """
    Snapshot APIs.
    """

    def __init__(self, client) -> None:

        self._client = client

    def get(
        self,
        channel: str = "CH1",
        snapshot_resolution: str = "1280x720",
        reset_session_timeout: bool = False,
    ) -> bytes:
        """
        Capture a snapshot.

        Returns:
            JPEG bytes.
        """

        response = self._client._request(
            "/API/Snapshot/Get",
            {
                "version": "1.0",
                "data": {
                    "channel": channel,
                    "snapshot_resolution": snapshot_resolution,
                    "reset_session_timeout": reset_session_timeout,
                },
            },
        )

        data = response.get("data", {})

        #
        # OEM documentation contains a typo:
        # ima_data / img_data
        #

        img_data = (
            data.get("img_data")
            or data.get("ima_data")
            or ""
        )

        if not img_data:
            raise ValueError(
                "Snapshot image data is empty."
            )

        return base64.b64decode(img_data)

    def range(self) -> dict:

        return self._client._request(
            "/API/Snapshot/Range",
            {
                "version": "1.0",
                "data": {
                    "reset_session_timeout": False,
                },
            },
        )
    
    def save(
        self,
        filename: str,
        channel: str = "CH1",
        snapshot_resolution: str = "1280x720",
        reset_session_timeout: bool = False,
    ) -> None:
        
        """
        Capture a snapshot and save it to a file.
        """

        image = self.get(
            channel=channel,
            snapshot_resolution=snapshot_resolution,
            reset_session_timeout=reset_session_timeout,
        )

        with open(filename, "wb") as f:
            f.write(image)