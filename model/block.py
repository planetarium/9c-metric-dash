from __future__ import annotations
import datetime

class Block:
    def __init__(self, line: str):
        words = line[:-1].split(" ")
        self._index = int(words[3][1:])
        self._hash = words[4]
        self._created = datetime.datetime.fromisoformat(words[-4][:-1])
        self._appended = datetime.datetime.fromisoformat(words[-1][:-1])
        return

    @property
    def index(self) -> int:
        return self._index

    @property
    def hash(self) -> str:
        return self._hash

    @property
    def created(self) -> datetime:
        return self._created

    @property
    def appended(self) -> datetime:
        return self._appended
