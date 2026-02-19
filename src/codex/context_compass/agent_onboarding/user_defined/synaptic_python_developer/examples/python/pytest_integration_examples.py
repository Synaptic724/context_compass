"""Integration-style pytest examples."""

class Store:
    def __init__(self) -> None:
        self._items: dict[str, str] = {}

    def put(self, key: str, value: str) -> None:
        self._items[key] = value

    def get(self, key: str) -> str | None:
        return self._items.get(key)


def test_store_round_trip() -> None:
    store = Store()
    store.put("k", "v")
    assert store.get("k") == "v"
