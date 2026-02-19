"""Attribute aliasing micro benchmark example."""

import timeit


class Sample:
    def __init__(self) -> None:
        self.value = 1


def direct(obj: Sample) -> int:
    total = 0
    for _ in range(1000):
        total += obj.value
    return total


def aliased(obj: Sample) -> int:
    total = 0
    value = obj.value
    for _ in range(1000):
        total += value
    return total


def run() -> tuple[float, float]:
    obj = Sample()
    d = timeit.timeit(lambda: direct(obj), number=2000)
    a = timeit.timeit(lambda: aliased(obj), number=2000)
    return d, a


if __name__ == "__main__":
    direct_t, aliased_t = run()
    print(f"direct={direct_t:.6f}s aliased={aliased_t:.6f}s")
