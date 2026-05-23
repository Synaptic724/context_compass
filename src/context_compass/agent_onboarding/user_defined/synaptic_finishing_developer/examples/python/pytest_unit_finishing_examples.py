"""Unit-test examples for finishing-role contract work."""

from typing import Optional


class ExampleHandle:
    """Example lifecycle object with explicit cleanup rules.

    Purpose:
      Demonstrate the kind of local lifecycle contract that deserves strong
      unit coverage and explicit docstring language.

    Contract:
      - `read()` is valid only while the handle is live.
      - `cleanup()` is idempotent.
      - Once cleaned, the object rejects future reads instead of silently
        returning fallback data.
    """

    def __init__(self) -> None:
        self._value: Optional[str] = "live"
        self._cleaned: bool = False

    def read(self) -> str:
        """Return the live value or fail if the handle was cleaned."""

        if self._cleaned:
            raise RuntimeError("handle is cleaned")
        return self._value or ""

    def cleanup(self) -> None:
        """Release the owned value and mark the object cleaned."""

        if self._cleaned:
            return
        self._value = None
        self._cleaned = True


def test_read_returns_live_value_before_cleanup() -> None:
    """Unit tests should prove the positive contract first."""

    handle = ExampleHandle()
    assert handle.read() == "live"


def test_read_raises_after_cleanup() -> None:
    """Unit tests should lock down the post-cleanup failure contract."""

    handle = ExampleHandle()
    handle.cleanup()
    try:
        handle.read()
    except RuntimeError as exc:
        assert "cleaned" in str(exc)
    else:
        raise AssertionError("expected RuntimeError after cleanup")


def test_cleanup_is_idempotent() -> None:
    """Cleanup idempotence is a first-class lifecycle claim."""

    handle = ExampleHandle()
    handle.cleanup()
    handle.cleanup()
    assert handle._cleaned is True
