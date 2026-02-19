"""Protocol and ABC examples."""

from abc import ABC, abstractmethod
from typing import Protocol


class Cache(Protocol):
    def get(self, key: str) -> str | None:
        ...


class Writer(ABC):
    @abstractmethod
    def write(self, payload: str) -> None:
        raise NotImplementedError
