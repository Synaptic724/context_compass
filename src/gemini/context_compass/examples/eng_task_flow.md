# Example: engineer task flow

Scenario
- Active ticket: `tickets/tasks/2026-02-19_spellbook_cleanup_ordering.md`
- Goal: keep logger cleanup as the final step in Spellbook teardown.

Entry gate
- `attention_board.md` points to the active ticket.
- Scope is limited to teardown ordering and related tests.

Ticket microcycle
1. Investigate
- Read current cleanup code and failing test history.

2. Document
- Add ticket note:
  - `FACT`: logger cleanup runs before child resources in current code.
  - `UNKNOWN`: whether any callers rely on current ordering.

3. Plan
- Update cleanup ordering.
- Add regression test for ordering contract.

4. Implement
- Edit teardown method to release children first, logger last.

5. Validate
- Run targeted test command.
- Record exact result (`pass` or `Not run`).

Exit gate
- Ticket notes include evidence paths and next single step.
- Acceptance criteria state ordering contract explicitly.