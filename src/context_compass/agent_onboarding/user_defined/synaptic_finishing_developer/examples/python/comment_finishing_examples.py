"""Examples of high-signal comments for finishing work."""

from threading import RLock


class ExampleDrainGate:
    """Small example showing where comments add contract value.

    Purpose:
      Demonstrate comments that explain admission and drain semantics rather
      than narrating trivial code.

    Contract:
      - `begin()` increments the in-flight count only while the gate is open.
      - `finish()` rejects underflow instead of silently correcting it.
      - `close()` blocks future entrants without mutating current in-flight
        work.
    """

    def __init__(self) -> None:
        self._lock: RLock = RLock()
        self._tickets: int = 0
        self._closed: bool = False

    def begin(self) -> None:
        """Register one in-flight ticket.

        Raises:
          RuntimeError: If the gate is already closed.
        """

        with self._lock:
            # Reject new entrants after close so later drain checks see a stable
            # in-flight ticket count instead of a moving target.
            if self._closed:
                raise RuntimeError("gate is closed")
            self._tickets += 1

    def finish(self) -> None:
        """Release one in-flight ticket.

        Raises:
          RuntimeError: If no ticket is active.
        """

        with self._lock:
            # Keep the underflow check explicit. A silent floor-to-zero update
            # would hide misuse from callers and make drain behavior ambiguous.
            if self._tickets <= 0:
                raise RuntimeError("no active ticket")
            self._tickets -= 1

    def close(self) -> None:
        """Prevent future tickets from entering the gate.

        Contract:
          Closing the gate does not itself drain active work. It only changes
          admission state.
        """

        with self._lock:
            # Close only flips admission state. It does not mutate the current
            # in-flight count, because callers still need to drain outstanding
            # work explicitly.
            self._closed = True
