from __future__ import annotations
import datetime

class BlockAppend:
    def __init__(self, line: str):
        words = line[:-1].split(" ")
        self._index = int(words[3][1:])
        self._hash = words[4]
        self._timestamp = datetime.datetime.fromisoformat(words[-4][:-1])
        self._appended = datetime.datetime.fromisoformat(words[-1][:-1])
        return

    @property
    def index(self) -> int:
        return self._index

    @property
    def hash(self) -> str:
        return self._hash

    @property
    def timestamp(self) -> datetime:
        return self._timestamp

    @property
    def appended(self) -> datetime:
        return self._appended

class BlockEvaluation:
    def __init__(self, line: str):
        words = line[:-1].split(" ")
        self._index = int(words[-5][1:])
        self._hash = words[-4]
        self._evaluation = int(words[-1][:-2])
        return

    @property
    def index(self) -> int:
        return self._index

    @property
    def hash(self) -> str:
        return self._hash

    @property
    def evaluation(self) -> int:
        return self._evaluation

class BlockStates:
    def __init__(self, line: str):
        words = line[:-1].split(" ")
        self._index = int(words[-4][1:])
        self._hash = words[-3]
        self._states = int(words[-1][:-2])
        return

    @property
    def index(self) -> int:
        return self._index

    @property
    def hash(self) -> str:
        return self._hash

    @property
    def states(self) -> int:
        return self._states
