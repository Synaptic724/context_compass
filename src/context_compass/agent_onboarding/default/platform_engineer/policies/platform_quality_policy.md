
# platform_quality_policy

Purpose
- Establish the quality bar for platform changes.

Policy
- Prefer small, reviewable, reversible changes.
- Any production-impact change must include:
  - rollback plan,
  - validation plan,
  - monitoring plan.
- Operational claims must be backed by evidence or marked UNKNOWN.

Unknowns Gate
- Apply the canonical policy in
  `agent_onboarding/default/general/skills/unknowns_gate_reference.md`.

References
- `agent_onboarding/default/platform_engineer/policies/operational_safety_policy.md`


