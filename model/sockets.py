from __future__ import annotations
import datetime
import json

class Sockets:
    def __init__(self, prev: Sockets, line: str):
        data = json.loads(line)
        self._timestamp = datetime.datetime.fromisoformat(data["@t"][:-2])
        if prev:
            if "request" in line:
                self._request = data["SocketCount"]
                self._broadcast = prev.broadcast
            elif "broadcast" in line:
                self._request = prev.request
                self._broadcast = data["SocketCount"]
            else:
                raise ValueError("Unknown log type")
        else:
            if "request" in line:
                self._request = data["SocketCount"]
                self._broadcast = 0
            elif "broadcast" in line:
                self._request = 0
                self._broadcast = data["SocketCount"]
            else:
                raise ValueError("Unknown log type")
        return

    @property
    def timestamp(self) -> datetime.datetime:
        return self._timestamp

    @property
    def request(self) -> int:
        return self._request

    @property
    def broadcast(self) -> int:
        return self._broadcast

    @property
    def total(self) -> int:
        return self.request + self.broadcast
