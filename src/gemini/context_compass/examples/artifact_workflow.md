# Example: artifact workflow

Scenario
- A design update requires a long-form artifact before implementation.

Flow
1. Create artifact file
- `artifacts/2026-02-19_cleanup_ordering_design.md`

2. Link artifact in ticket
- Add `## Artifacts` section in active ticket.

3. Register artifact on board
- Add row to `artifact_board.md` with ticket id and disposition.

4. Capture decision note
- Ticket note includes:
  - `DECISION`: selected option
  - `RATIONALE`: key tradeoff
  - `EVIDENCE`: files reviewed

5. Close or retain artifact on ticket close
- Apply disposition:
  - `delete_on_close`, `retain_as_reference`, or `promote_to_documentation`.

Expected outcome
- Any reader can reconstruct why the artifact exists and where it is consumed.