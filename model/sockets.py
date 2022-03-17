from __future__ import annotations
import datetime

class Sockets:
    def __init__(self, data: dict):
        self._timestamp = datetime.datetime.fromisoformat(data["@t"][:-2])
        self._count = data["SocketCount"]
        return

    @property
    def timestamp(self) -> datetime.datetime:
        return self._timestamp

    @property
    def count(self) -> int:
        return self._count
