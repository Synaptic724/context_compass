# line_copy_editor_handoff_policy

Purpose
- Define safe and deterministic handoff behavior for line_copy_editor.

Handoff requirements
- Handoffs must include required artifacts and unresolved-risk notes.
- Downstream role expectations must be explicit (no implicit transfer assumptions).
- If gate criteria are not met, handoff status must be BLOCKED.

Primary handoff targets
- continuity_fact_checker: receives polished manuscript plus consistency logs.
- proofreader: receives near-final text after continuity clearance.
- draft_writer: receives targeted issues requiring content-level rewrite.

Handoff packet checklist
- Deliverable index.
- Gate status summary.
- Open-risk list with owner and proposed next step.
- Decision log entries for any scope changes.
