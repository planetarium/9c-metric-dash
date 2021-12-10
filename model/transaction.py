from __future__ import annotations
import datetime

class Transaction:
    def __init__(self, line):
        words = line[:-1].split(" ")
        self._signer = words[5]
        self._id = words[3]
        self._created = datetime.datetime.fromisoformat(words[-4][:-1])
        self._staged = datetime.datetime.fromisoformat(words[-1][:-1])
        return

    @property
    def signer(self) -> str:
        return self._signer

    @property
    def id(self) -> str:
        return self._id

    @property
    def created(self) -> datetime:
        return self._created

    @property
    def staged(self) -> datetime:
        return self._staged
