from __future__ import annotations
import datetime
import json

class BlockAppend:
    def __init__(self, line: str):
        data = json.loads(line)
        self._index = data["BlockIndex"]
        self._hash = data["BlockHash"]
        self._timestamp = datetime.datetime.fromisoformat(data["BlockTimestamp"][:-1])
        self._appended = datetime.datetime.fromisoformat(data["AppendTimestamp"][:-1])
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
        data = json.loads(line)
        self._index = data["BlockIndex"]
        self._pre_eval_hash = data["PreEvaluationHash"]
        self._duration = data["DurationMs"]
        self._tx_count = data["TxCount"]
        return

    @property
    def index(self) -> int:
        return self._index

    @property
    def pre_eval_hash(self) -> str:
        return self._pre_eval_hash

    @property
    def duration(self) -> float:
        return self._duration

    @property
    def tx_count(self) -> int:
        return self._tx_count

class BlockStates:
    def __init__(self, line: str):
        data = json.loads(line)
        self._index = data["BlockIndex"]
        self._hash = data["BlockHash"]
        self._duration = data["DurationMs"]
        self._key_count = data["KeyCount"]
        return

    @property
    def index(self) -> int:
        return self._index

    @property
    def hash(self) -> str:
        return self._hash

    @property
    def duration(self) -> float:
        return self._duration

    @property
    def key_count(self) -> int:
        return self._key_count

class BlockRender:
    def __init__(self, line: str):
        data = json.loads(line)
        self._index = data["BlockIndex"]
        self._hash = data["BlockHash"]
        self._duration = data["DurationMs"]
        self._render_count = data["RenderCount"]
        return

    @property
    def index(self) -> int:
        return self._index

    @property
    def hash(self) -> str:
        return self._hash

    @property
    def duration(self) -> float:
        return self._duration

    @property
    def render_count(self) -> int:
        return self._render_count
