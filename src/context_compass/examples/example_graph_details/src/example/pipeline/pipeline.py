"""Pipeline execution scope."""
from threading import RLock
from example.core.resource import Resource
from example.pipeline.stage import Stage
from example.storage.store import Store


class Pipeline(Resource):
    """Execution scope that owns its stages and borrows a store."""

    def __init__(self, store: Store) -> None:
        self._lock = RLock()
        self._stages: list[Stage] = [Stage("load"), Stage("validate")]
        self._store = store

    def acquire(self) -> None: ...
    def release(self) -> None: ...
    def add_stage(self, stage: Stage) -> None: ...
    def run(self, payload: bytes) -> bytes: ...
    def stage_names(self) -> list[str]: ...
