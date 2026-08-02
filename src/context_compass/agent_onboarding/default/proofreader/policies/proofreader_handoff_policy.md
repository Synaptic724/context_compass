# proofreader_handoff_policy

Purpose
- Define safe and deterministic handoff behavior for proofreader.

Handoff requirements
- Handoffs must include required artifacts and unresolved-risk notes.
- Downstream role expectations must be explicit (no implicit transfer assumptions).
- If gate criteria are not met, handoff status must be BLOCKED.

Primary handoff targets
- Publishing/release workflows: receive final manuscript and proof logs.
- line_copy_editor: receives issues that exceed proofreader scope.
- continuity_fact_checker: receives any late-discovered canon blockers.

Handoff packet checklist
- Deliverable index.
- Gate status summary.
- Open-risk list with owner and proposed next step.
- Decision log entries for any scope changes.
