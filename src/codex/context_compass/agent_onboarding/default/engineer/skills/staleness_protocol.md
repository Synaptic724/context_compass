

# staleness_protocol

Purpose
- Define required actions for stale documentation or ticket context.

Required flow
- Resolve stale or missing documentation/tickets before feature work.

States and required actions
- missing: create the missing doc or ticket immediately.
- stale: refresh the doc to match current code or intent.
- needs_review: confirm architecture and update notes if needed.
- fresh: no action.
- blocked: record a blocker in the relevant ticket.

Noise control
- Update docs only when state or semantic content changes.
- Avoid churn or rewording without new information.

Enforcement rule
- Do not handwave around stale docs; update canonical `system_docs/` files
  (`src_architecture.md`, `src_components.md`, `tests_architecture.md`,
  `tests_components.md`) when boundaries or invariants change.

Example transitions
- missing -> fresh after doc creation.
- stale -> fresh after refresh.
- fresh -> needs_review after a significant refactor.

References
- `system_docs/src_architecture.md`
- `system_docs/src_components.md`
- `system_docs/tests_architecture.md`
- `system_docs/tests_components.md`



