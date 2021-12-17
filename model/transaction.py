from __future__ import annotations
import datetime
import json

class TransactionStage:
    def __init__(self, line):
        data = json.loads(line)
        self._signer = data["Signer"]
        self._id = data["TxId"]
        self._timestamp = datetime.datetime.fromisoformat(data["TxTimestamp"][:-1])
        self._staged = datetime.datetime.fromisoformat(data["StagedTimestamp"][:-1])
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
