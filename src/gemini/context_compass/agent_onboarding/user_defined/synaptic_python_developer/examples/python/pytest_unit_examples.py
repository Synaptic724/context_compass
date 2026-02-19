"""Unit-style pytest examples."""


def add(a: int, b: int) -> int:
    return a + b


def test_add_positive_numbers() -> None:
    assert add(2, 3) == 5


def test_add_negative_numbers() -> None:
    assert add(-2, -3) == -5
