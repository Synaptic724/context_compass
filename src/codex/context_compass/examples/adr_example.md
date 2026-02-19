# Example: ADR - Cleanup Ordering Contract

Status
- Accepted

Context
- Shutdown failures were hard to debug because logger teardown happened too early.

Decision
- Keep logger cleanup as the final teardown step.

Consequences
- Better post-failure observability during cleanup.
- Requires regression tests that assert teardown ordering.

Implementation links
- ticket: `tickets/tasks/2026-02-19_spellbook_cleanup_ordering.md`
- validation: targeted integration logging test