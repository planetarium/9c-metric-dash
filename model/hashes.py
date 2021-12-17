from __future__ import annotations
import json

class FindHashes:
    def __init__(self, line: str):
        data = json.loads(line)
        self._hash_count = data["HashCount"]
        self._chain_id_count = data["ChainIdCount"]
        self._duration = data["DurationMs"]
        return

    @property
    def hash_count(self) -> int:
        return self._hash_count

    @property
    def chain_id_count(self) -> int:
        return self._chain_id_count

    @property
    def duration(self) -> float:
        return self._duration
