"""Anti-pattern snippets used in policy docs.

These examples are intentionally bad patterns.
"""

class BadCleanupExample:
    def __init__(self):
        self._resource = object()

    def cleanup(self):
        # Anti-pattern: relies on hasattr/getattr for owned state.
        if hasattr(self, "_resource"):
            _ = getattr(self, "_resource")
        # Anti-pattern: missing explicit null assignment.


def bad_exists_check(obj):
    # Anti-pattern: tests internal existence instead of behavior.
    return hasattr(obj, "_internal_state")
