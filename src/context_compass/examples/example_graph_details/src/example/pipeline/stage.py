"""A single unit of work in a pipeline."""


class Stage:
    """One transformation step."""

    def __init__(self, name: str) -> None:
        self.name = name

    def run(self, payload: bytes) -> bytes: ...
    def describe(self) -> str: ...
