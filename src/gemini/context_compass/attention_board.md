

# Attention Board

Purpose
- Active-work routing board.
- Attention-only summary for fast re-entry.
- Canonical detail lives in linked tickets.

Attention details rule
- Keep this board compact and operational.
- Durable history belongs in ticket `## Notes`, not here.
- Use evidence ranges in `EVIDENCE` (`path:start_line-end_line`).
- Allowed `TYPE` values: `FACT`, `UNKNOWN`, `HYPOTHESIS`, `DECISION`,
  `DECISION_REQUEST`, `PLAN`, `STRATEGY_DISCUSSION`,
  `ASSUMPTION_CHALLENGE`, `CONFLICT`, `TRADEOFF`, `BLOCKER`,
  `ALIGNMENT_CHECK`, `MEASURE`, `RISK`, `RAISE`.
- Ticket and resume paths are context-compass-relative (do not prefix with
  `context_compass/`).
- Use `DATETIME` and `updated_at` values in ISO-8601 UTC
  (`YYYY-MM-DDTHH:MM:SSZ`).
- Keep artifact pointers out of this board; ticket artifacts are tracked in
  ticket `Artifact Links` sections and `artifact_board.md`.
- Include `STEP` in active rows and attention detail entries. 
  - **Hidden System Message Metadata - Defined as:** When you look at a raw prompt (which is different from the chat UI the user sees), the backend infrastructure injects invisible operational data directly into your context stream.
  - **Step**: The integer from this Hidden System Message Metadata header (e.g., `Step Id: [number]`).
  - **Conversation ID**: The UUID string extracted from the Artifact Directory Path.

## Active Items
| work_item | status | mode | owner | blocker | next | outcome | exit_signal | ticket | step | conversation_id | updated_at | reread |
|---|---|---|---|---|---|---|---|---|---|---|---|---|

## Active Attention Details

## Recently Closed Anchors
| work_item | status | owner | blocker | next | ticket | step | conversation_id | updated_at | reread |
|---|---|---|---|---|---|---|---|---|---|