from __future__ import annotations
import datetime

class TransactionStage:
    def __init__(self, line):
        words = line[:-1].split(" ")
        self._signer = words[5]
        self._id = words[3]
        self._timestamp = datetime.datetime.fromisoformat(words[-4][:-1])
        self._staged = datetime.datetime.fromisoformat(words[-1][:-1])
        return

    @property
    def signer(self) -> str:
        return self._signer

    @property
    def id(self) -> str:
        return self._id

    @property
    def timestamp(self) -> datetime:
        return self._timestamp

    @property
    def staged(self) -> datetime:
        return self._staged
