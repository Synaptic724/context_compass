"""Base resource contract."""
from abc import ABC, abstractmethod


class Resource(ABC):
    """Anything with an acquire/release lifecycle."""

    @abstractmethod
    def acquire(self) -> None: ...

    @abstractmethod
    def release(self) -> None: ...

    def is_open(self) -> bool:
        return False
