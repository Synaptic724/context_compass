"""Docstring examples for public APIs."""

from typing import Iterable


def normalize_names(names: Iterable[str]) -> list[str]:
    """Return normalized, non-empty names.

    Contract:
    - trims whitespace
    - lowercases values
    - removes empty results
    """
    out = []
    for name in names:
        value = name.strip().lower()
        if value:
            out.append(value)
    return out
