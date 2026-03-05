# code_description_patch_contracts

Purpose
- Define the conditional authoring contract for
  `system_docs/patches/active/<patch_id>/code_description_patch_<component>.md`.
- Capture implementation-relevant control-flow intent when component patches
  are not sufficient by themselves.

When required
- Complex control-flow or state-machine changes.
- New or changed policy gate pipelines.
- Multi-branch error/rollback semantics.
- Concurrency, ordering, or idempotency-sensitive behavior.

When not required
- Simple interface or data-shape changes already fully covered by
  `component_patch_<component>.md`.
- Low-risk behavior changes with no non-trivial control-flow deltas.

Required section contract
1) Trigger justification (why this file is required)
2) Control-flow description (pseudocode level, not production code)
3) Edge/error behavior and rollback semantics
4) Invariants and idempotency expectations
5) Explicit non-goals
6) Validation focus points

Authoring rules
- Keep this file implementation-guiding, not implementation-copying.
- Avoid line-level code prescriptions unless required by invariant safety.
- Keep language deterministic so engineer mapping can be unambiguous.

Quality gate
- Trigger reason is explicit and evidence-backed.
- Control-flow and error semantics are concrete and testable.
- Non-goals prevent unintended scope expansion.
- Validation focus points map to ticketed verification steps.

Handoff requirements
- Link this artifact when trigger criteria are met.
- Engineer lane is blocked if required code-description patches are missing.

References
- `agent_onboarding/default/design_engineer/skills/patch_framework_design.md`
- `agent_onboarding/default/design_engineer/skills/component_patch_contracts.md`
- `agent_onboarding/default/engineer/skills/patch_framework_gating.md`
