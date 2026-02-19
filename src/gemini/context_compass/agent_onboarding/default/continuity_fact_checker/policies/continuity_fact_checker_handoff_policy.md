# continuity_fact_checker_handoff_policy

Purpose
- Define safe and deterministic handoff behavior for continuity_fact_checker.

Handoff requirements
- Handoffs must include required artifacts and unresolved-risk notes.
- Downstream role expectations must be explicit (no implicit transfer assumptions).
- If gate criteria are not met, handoff status must be BLOCKED.

Primary handoff targets
- draft_writer or line_copy_editor: receives text-level fix actions.
- proofreader: receives continuity-cleared manuscript and residual waivers.
- researcher: receives unresolved factual unknowns requiring deeper evidence.

Handoff packet checklist
- Deliverable index.
- Gate status summary.
- Open-risk list with owner and proposed next step.
- Decision log entries for any scope changes.
