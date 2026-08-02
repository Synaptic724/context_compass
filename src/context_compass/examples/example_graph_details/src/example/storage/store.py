"""Record storage."""
from threading import RLock
from example.core.resource import Resource


class Store(Resource):
    """Holds records for the duration of a run."""

    def __init__(self) -> None:
        self._lock = RLock()
        self._records: dict[str, bytes] = {}

    def acquire(self) -> None: ...
    def release(self) -> None: ...
    def put(self, key: str, value: bytes) -> None: ...
    def get(self, key: str) -> bytes: ...
    def keys(self) -> list[str]: ...


Storage = Store
