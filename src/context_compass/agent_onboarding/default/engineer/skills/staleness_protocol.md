

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
- Do not handwave around stale docs. When boundaries, invariants, or documented
  source wiring change, bring the canonical `system_docs/` files current.
- **AUTHORED documents you edit directly:** `src_architecture.md`,
  `src_components.md`, `tests_architecture.md`, `tests_components.md`. Regenerate
  each one's `*_index.md` in the same pass.
- **GENERATED documents you must NOT edit:** `src_graph.md` and
  `src_graph_index.md`. Edit the per-file descriptors and reassemble; a hand-edit
  is overwritten by the next run and, in the meantime, breaks the index hash so
  every slice is refused. See
  `agent_onboarding/default/engineer/skills/src_graph_generation.md`.
- The distinction is not cosmetic. "Update `src_graph.md`" is an instruction that
  cannot be carried out correctly, and an agent that follows it literally
  corrupts the staleness proof the whole slicing protocol depends on.

Example transitions
- missing -> fresh after doc creation.
- stale -> fresh after refresh.
- fresh -> needs_review after a significant refactor.

References
- `system_docs/src_architecture.md`
- `system_docs/src_components.md`
- `system_docs/src_graph.md`
- `system_docs/tests_architecture.md`
- `system_docs/tests_components.md`


