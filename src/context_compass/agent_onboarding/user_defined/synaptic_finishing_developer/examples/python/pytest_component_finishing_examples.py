"""Component-test examples for finishing-role boundary work."""

from typing import Optional


class ExampleDescriptorStore:
    """Own a tiny published-record store.

    Purpose:
      Model the kind of owned publication surface that is often too real for a
      pure unit test but too small for a full integration test.
    """

    def __init__(self) -> None:
        self._records: dict[str, str] = {}

    def publish(self, key: str, payload: str) -> None:
        self._records[key] = payload

    def get(self, key: str) -> Optional[str]:
        return self._records.get(key)


class ExampleViewer:
    """Borrow the descriptor store and expose one read helper.

    Contract:
      - Reads the latest published payload from the borrowed store.
      - Raises when the requested record is absent.
      - Does not own store lifecycle.
    """

    def __init__(self, store: ExampleDescriptorStore) -> None:
        self._store = store

    def describe(self, key: str) -> str:
        payload = self._store.get(key)
        if payload is None:
            raise KeyError(key)
        return f"visible:{payload}"


def test_viewer_reads_the_latest_published_record() -> None:
    """Component tests should prove the real boundary, not mock it away."""

    store = ExampleDescriptorStore()
    viewer = ExampleViewer(store)
    store.publish("alpha", "payload-v1")
    assert viewer.describe("alpha") == "visible:payload-v1"
    store.publish("alpha", "payload-v2")
    assert viewer.describe("alpha") == "visible:payload-v2"
