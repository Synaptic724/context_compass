"""Structural mirrors of the core contracts."""
from typing import Protocol


class IResource(Protocol):
    """Structural mirror of Resource's public surface."""

    def acquire(self) -> None: ...
    def release(self) -> None: ...
    def is_open(self) -> bool: ...
