# system_aware_docstrings

Purpose
- Force docstring writing to account for the larger system instead of treating
  methods and classes as isolated islands.

Required read surfaces
- `system_docs/src_architecture.md`
- `system_docs/src_components.md`
- `agent_onboarding/default/engineer/skills/src_graph_usage.md`
- `system_docs/src_graph.md`

Use each surface for a different question
- `src_architecture.md`
  - What system layer is this in?
  - What is the top-level purpose?
  - What invariants and failure modes matter globally?
- `src_components.md`
  - What owns this object?
  - What does it create, validate, publish, or bind?
  - What are the method-level call flows?
- `src_graph.md`
  - What does this object own?
  - What does it borrow?
  - What does it create?
  - What edges imply lifecycle responsibility?

System-aware docstring pattern
1) Start from the symbol under edit.
2) Map it to its component and subsystem.
3) Check ownership and borrowing relationships in the graph.
4) Reconcile that with the code and call flow.
5) Write the docstring so it explains the symbol's place in that structure.

What to include when system context matters
- upstream owner
- downstream consumers
- whether it owns lifecycle or only borrows
- shared-state or registry side effects
- validation or publication effects
- why its contract matters beyond the local file

What to avoid
- claiming ownership when the graph shows borrowing
- hiding cleanup responsibility when the component docs make it explicit
- writing local-only descriptions for symbols that coordinate multiple layers
- inventing guarantees that the architecture/docs/code do not support

Unknowns rule
- If the architecture, components, and graph do not line up cleanly with the
  code, do not bluff.
- Investigate further or keep the claim out of the docstring until it is
  evidenced.

References
- `system_docs/src_architecture.md`
- `system_docs/src_components.md`
- `agent_onboarding/default/engineer/skills/src_graph_usage.md`
- `system_docs/src_graph.md`
