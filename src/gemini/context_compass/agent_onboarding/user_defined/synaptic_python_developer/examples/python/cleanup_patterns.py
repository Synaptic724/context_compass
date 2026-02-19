"""Cleanup patterns referenced by the synaptic overlay."""

class ManagedResource:
    def __init__(self):
        self._open = True

    def close(self):
        self._open = False


class GoodCleanupExample:
    def __init__(self):
        self._resource = ManagedResource()
        self._cleaned = False

    def cleanup(self):
        """Release owned resources in deterministic order."""
        if self._cleaned:
            return
        self._resource.close()
        self._resource = None
        self._cleaned = True
