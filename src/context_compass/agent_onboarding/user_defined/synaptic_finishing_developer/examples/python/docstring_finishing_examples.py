"""Examples of deep public-library docstrings for finishing work.

These examples are intentionally richer than the compact synaptic Python
examples. They model the finishing role's expectation that a docstring should
explain system role, ownership, cleanup, and the visible contract the tests
must defend.
"""

from threading import RLock
from typing import Callable, Optional


class ExamplePublicationCache:
    """Own a small publication cache with explicit lifecycle and locking rules.

    Purpose:
      Store recently published payloads under stable keys so callers can reuse
      the latest published shape without rebuilding it.

    System Role:
      This object stands in for the class of runtime surfaces that sit between
      a producer and a later read path. It owns one local cache, guards that
      cache with an internal re-entrant lock, and exposes a cleanup boundary so
      callers do not keep reading stale state after teardown.

    Contract:
      - `publish(...)` replaces the payload for one key and records the latest
        visible value.
      - `get(...)` returns the current payload for one key or ``None`` when no
        payload is present.
      - `cleanup()` is idempotent.
      - After cleanup, public methods that require a live cache raise
        ``RuntimeError`` instead of silently recreating state.

    Threading / Concurrency:
      - The instance owns one `RLock`.
      - All cache mutation and reads occur under that lock so callers never see
        a half-updated payload map.

    Lifecycle / Cleanup:
      - This object owns `_payloads`, `_lock`, and `_on_publish`.
      - Cleanup clears owned payload state, then releases owned references.
      - The callback reference is treated as borrowed behavior supplied by the
        caller; the cache owns only the reference, not the callback's broader
        lifecycle.
    """

    def __init__(self, on_publish: Optional[Callable[[str, str], None]] = None) -> None:
        """Initialize the cache with an optional publish callback.

        Args:
          on_publish: Optional callback invoked after one payload is stored.

        Contract:
          - The cache starts live and empty.
          - The callback is optional and may be ``None``.
        """

        self._payloads: dict[str, str] = {}
        self._lock: RLock = RLock()
        self._on_publish: Optional[Callable[[str, str], None]] = on_publish
        self._cleaned: bool = False

    def publish(self, key: str, payload: str) -> None:
        """Store one payload and expose it as the latest value for ``key``.

        Args:
          key: Stable lookup key for the payload.
          payload: Visible payload value to publish.

        Raises:
          RuntimeError: If the cache was already cleaned.
          ValueError: If ``key`` is empty.

        Side Effects:
          - Mutates the owned payload map.
          - Invokes the optional callback after the new payload is visible.
        """

        if not key:
            raise ValueError("key must be non-empty")
        with self._lock:
            self._check_cleaned()
            self._payloads[key] = payload
            callback = self._on_publish
        if callback is not None:
            callback(key, payload)

    def get(self, key: str) -> Optional[str]:
        """Return the latest payload for ``key``.

        Args:
          key: Stable lookup key for the payload.

        Returns:
          The latest payload for the key, or ``None`` if no payload exists.

        Raises:
          RuntimeError: If the cache was already cleaned.
        """

        with self._lock:
            self._check_cleaned()
            return self._payloads.get(key)

    def cleanup(self) -> None:
        """Release owned cache state.

        Contract:
          - Cleanup is idempotent.
          - After cleanup, the cache no longer serves reads or writes.
          - Owned payload state is cleared before owned references are dropped.
        """

        with self._lock:
            if self._cleaned:
                return
            self._payloads.clear()
            self._on_publish = None
            self._cleaned = True

    def _check_cleaned(self) -> None:
        """Raise when a caller uses the cache after cleanup."""

        if self._cleaned:
            raise RuntimeError("ExamplePublicationCache is cleaned")
