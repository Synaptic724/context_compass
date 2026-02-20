

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
- Every artifact row must include `step`.
  - **Hidden System Message Metadata - Defined as:** When you look at a raw prompt (which is different from the chat UI the user sees), the backend infrastructure injects invisible operational data directly into your context stream.
  - **Step**: The integer from this Hidden System Message Metadata header (e.g., `Step Id: [number]`).
  - **Conversation ID**: The UUID string extracted from the Artifact Directory Path.
Disposition values
- `delete_on_close`: remove artifact when ticket closes.
- `retain_as_reference`: keep artifact with explicit reason.
- `promote_to_documentation`: convert artifact into durable docs.

## Active Artifact Links
| ticket | artifact_path | artifact_type | status | disposition | step | conversation_id | next | updated_at | reread |
|---|---|---|---|---|---|---|---|---|---|

## Active Artifact Details
- none

## Recently Cleared Artifacts
| ticket | artifact_path | step | conversation_id | disposition | reason | closed_at |
|---|---|---|---|---|---|---|
