
# Design Engineer Career

Purpose
- Design-engineer-specific onboarding deltas on top of the shared `general` baseline and the `engineer` implementation baseline.
- Optimized for software/system design, architecture planning, and high-quality handoff to implementation.

Scope rule
- Keep only design-engineer-specific policy/behavior here.
- Shared rules remain in:
  - `agent_onboarding/default/general/` (process, ticketing, gates, certification)
  - `agent_onboarding/default/engineer/` (implementation and engineering quality discipline)
- Design Engineer extends `engineer` and must remain a delta layer:
  no path overlap with `agent_onboarding/default/engineer/SKILLS.MD`.

Design Engineer inventory
- `agent_onboarding/default/design_engineer/SKILLS.MD`: design-engineer-specific read sequence.
- `skills/architecture_contexts.md`: architecture/components source-of-truth policy.
- `skills/src_architecture_instructions.md`: creation/maintenance mechanics for
  `system_docs/src_architecture.md`.
- `skills/src_components_instructions.md`: creation/maintenance mechanics for
  `system_docs/src_components.md`.
- `skills/tests_architecture_instructions.md`: creation/maintenance mechanics
  for `system_docs/tests_architecture.md`.
- `skills/tests_components_instructions.md`: creation/maintenance mechanics for
  `system_docs/tests_components.md`.
- `skills/design_engineer_execution.md`: design execution discipline and artifact expectations.
- `skills/requirements_to_architecture.md`: convert goals to requirements, constraints, and acceptance criteria.
- `skills/system_design_method.md`: system design structure (components, data flows, failure modes).
- `skills/decomposition_and_boundaries.md`: decomposition, boundaries, and coupling control.
- `skills/api_and_interface_design.md`: interface/API design discipline (contracts, versioning, errors).
- `skills/data_modeling.md`: schema and data modeling discipline.
- `skills/architecture_tradeoffs.md`: tradeoff analysis and option evaluation.
- `skills/adr_and_decision_hygiene.md`: ADR format, decision recording, and decision hygiene.
- `skills/nonfunctional_requirements.md`: NFR design (performance, reliability, security, operability).
- `skills/design_review_protocol.md`: review/checkpoint protocol and handoff to tickets.
- `policies/design_quality_policy.md`: design artifact quality bar.
- `policies/decision_record_policy.md`: ADR and decision-record gating.
- `policies/design_review_policy.md`: review gate rules before implementation.
- `behavioral_guidelines/design_engineer_workflow.md`: design task execution flow.
- `behavioral_guidelines/design_validation_and_handoff.md`: validation and implementation handoff flow.
- `examples/design_task_flow.md`: example design task flow.
- `examples/adr_example.md`: ADR example template.

Overlap rules
- If a skill is already defined in `engineer` or `general`, reference it instead of duplicating.
- Implementation tasks still follow engineer execution discipline:
  - `agent_onboarding/default/engineer/skills/engineer_execution.md`
  - `agent_onboarding/default/engineer/behavioral_guidelines/task_execution_and_validation.md`

Unknowns Gate
- Apply the canonical policy in
  `agent_onboarding/default/general/skills/unknowns_gate_reference.md`.

