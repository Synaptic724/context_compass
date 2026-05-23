"""Component-style pytest examples."""

class Counter:
    def __init__(self) -> None:
        self._value = 0

    def inc(self) -> int:
        self._value += 1
        return self._value


def test_counter_component_flow() -> None:
    counter = Counter()
    assert counter.inc() == 1
    assert counter.inc() == 2
