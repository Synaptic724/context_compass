

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
- Include `STEP` and `CHECKPOINT` in active rows and attention detail entries.

## Active Items
| work_item | status | mode | owner | blocker | next | outcome | exit_signal | ticket | step | checkpoint | updated_at | reread |
|---|---|---|---|---|---|---|---|---|---|---|---|---|

## Active Attention Details
- DATETIME: YYYY-MM-DDTHH:MM:SSZ
  TYPE:
    FACT | UNKNOWN | HYPOTHESIS | DECISION | DECISION_REQUEST | PLAN |
    STRATEGY_DISCUSSION | ASSUMPTION_CHALLENGE | CONFLICT | TRADEOFF |
    BLOCKER | ALIGNMENT_CHECK | MEASURE | RISK | RAISE
  CLAIM: <short finding>
  EVIDENCE:
  - <path:start_line-end_line>
  IMPACT: <why this matters>
  NEXT: <one concrete next action>
  STEP: <STEP-ID>
  CHECKPOINT: <CHECKPOINT-ID | none>
  REREAD: REQUIRED | HELPFUL

## Recently Closed Anchors
| work_item | status | owner | blocker | next | ticket | step | checkpoint | updated_at | reread |
|---|---|---|---|---|---|---|---|---|---|
