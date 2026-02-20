# Example: artifact workflow (repo-based)

Scenario
- A docs release-readiness pass requires a retained rationale artifact.

Flow
1. Create artifact
- `examples/example_completed/2026-02-19_context_compass_release_overview_artifact.md`

2. Link artifact in ticket chain
- Epic, story, and task all include the same artifact path.

3. Capture rationale
- Add `DECISION`, `EVIDENCE`, `NEXT`, `STEP` (integer step id), and `CHECKPOINT` (snapshot id) note fields in linked tickets.

4. Apply disposition
- Keep as `retain_as_reference` unless a later docs policy changes it, and keep
  `artifact_board.md` rows aligned with `step` and `checkpoint` (using the Hidden System Message Metadata).

Expected outcome
- Any reader can reconstruct why the artifact exists and how it supports ticket closure.
