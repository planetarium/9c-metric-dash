from __future__ import annotations
import datetime
import json

class Request:
    def __init__(self, line: str):
        data = json.loads(line)
        self._message = data["Message"].split(".")[-1]
        self._timestamp = datetime.datetime.fromisoformat(data["@t"][:-2])
        self._timeout = data["TimeoutMs"]
        self._duration = data["DurationMs"]
        self._success = "@x" not in data
        return

    @property
    def message(self) -> str:
        return self._message

    @property
    def timestamp(self) -> int:
        return self._timestamp

    @property
    def timeout(self) -> float:
        return self._timeout

    @property
    def duration(self) -> float:
        return self._duration

    @property
    def ratio(self) -> float:
        return self.duration / self.timeout if self.timeout > 0 else -1

    @property
    def success(self) -> bool:
        return self._success
