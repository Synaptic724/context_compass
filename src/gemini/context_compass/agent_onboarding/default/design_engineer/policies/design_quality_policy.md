
# design_quality_policy

Purpose
- Establish the quality bar for design artifacts produced by `design_engineer`.

Policy
- Design output must be implementable and testable, not conceptual only.
- For any non-trivial design, include:
  - goal/non-goals,
  - constraints,
  - assumptions + UNKNOWNs,
  - options + tradeoffs,
  - architecture + interfaces,
  - NFR coverage,
  - test/validation plan,
  - rollout/observability plan,
  - ticketization plan.
- Use evidence pointers for current-state claims.
- Do not hide risks: call them out with severity and proposed mitigations.

Unknowns Gate
- Apply the canonical policy in
  `agent_onboarding/default/general/skills/unknowns_gate_reference.md`.

References
- `agent_onboarding/default/design_engineer/skills/system_design_method.md`
- `agent_onboarding/default/design_engineer/skills/architecture_tradeoffs.md`


