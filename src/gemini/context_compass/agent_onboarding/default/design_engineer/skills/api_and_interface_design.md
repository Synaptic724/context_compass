
# api_and_interface_design

Purpose
- Define interface design discipline for APIs and internal contracts.
- Prevent breaking changes and ambiguous error behavior.

Core rules
- Every interface must define:
  - inputs (types, validation),
  - outputs (types, semantics),
  - error behavior (codes, retries, invariants),
  - versioning/compatibility strategy.
- Prefer explicit, stable, boring contracts over "smart" implicit behavior.
- If idempotency matters, define it explicitly.
- If pagination matters, define it explicitly.
- If timeouts/retries matter, define them explicitly.

Error semantics checklist
- What errors are user-correctable vs system errors?
- What errors are retryable and under what conditions?
- Are errors stable enough to be relied on by callers?
- Do errors leak secrets or sensitive details?

Versioning/compatibility checklist
- Backward compatibility window
- Deprecation mechanism
- Migration strategy
- Rollout plan that supports mixed versions

References
- `agent_onboarding/default/design_engineer/skills/adr_and_decision_hygiene.md`
- `agent_onboarding/default/design_engineer/skills/nonfunctional_requirements.md`
- `agent_onboarding/default/engineer/skills/documentation_standards.md`


