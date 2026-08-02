# story_novel_artist_handoff_policy

Purpose
- Define safe and deterministic handoff behavior for story_novel_artist.

Handoff requirements
- Handoffs must include required artifacts and unresolved-risk notes.
- Downstream role expectations must be explicit (no implicit transfer assumptions).
- If gate criteria are not met, handoff status must be BLOCKED.

Primary handoff targets
- draft_writer: receives visual constraints for descriptive consistency.
- continuity_fact_checker: receives visual canon map for contradiction checks.
- Image-generation workflows: receive deterministic brief pack.

Handoff packet checklist
- Deliverable index.
- Gate status summary.
- Open-risk list with owner and proposed next step.
- Decision log entries for any scope changes.
