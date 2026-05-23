

# Artifact Board

Purpose
- Canonical index of active artifact associations.
- Track artifact lifecycle decisions that support ticket execution.
- Keep `attention_board.md` ticket-only and free of artifact pointers.

Scope rules
- `attention_board.md` routes tickets only; do not add artifact paths there.
- Tickets remain canonical memory; this board is an association index.
- Add rows only when a ticket has one or more active artifact files.
- Every artifact row must include a ticket path and retention decision.
- If runtime is Gemini and step metadata helps resume quality, record the
  continuity anchor under `## Active Artifact Notes` rather than changing the
  routing table shape.

Disposition values
- `delete_on_close`: remove artifact when ticket closes.
- `retain_as_reference`: keep artifact with explicit reason.
- `promote_to_documentation`: convert artifact into durable docs.

## Active Artifact Links
| ticket | artifact_path | artifact_type | status | disposition | next | updated_at | reread |
|---|---|---|---|---|---|---|---|


## Active Artifact Notes
- Optional Gemini continuity note format:
  - `artifact_path`
  - `GEMINI_STEP_COUNTER`
  - `GEMINI_CHECKPOINT`
  - `reason`

## Recently Cleared Artifacts
| ticket | artifact_path | disposition | reason | closed_at |
|---|---|---|---|---|
