

# ctx_autonomy_policy

Purpose
- Apply CTX Autonomy ranking to engineer ctx work.
- Keep file ctx strong enough to support downstream dir/component/architecture ctx.

Policy
- Use the CTX Autonomy rubric before accepting any file ctx update.
- Target >= 75 for file ctx on production code; do not proceed to dir ctx if below 60.
- Ensure file ctx captures public surface, dependencies, error model, invariants, lifecycle, and testing.
- If code changed, refresh file ctx first, then regenerate dir ctx and resurvey higher layers.

Unknowns Gate
- Apply the canonical policy in
  `agent_onboarding/default/general/skills/unknowns_gate_reference.md`.
- Engineer ctx updates must not promote claims without evidence.
- Engineer file-ctx updates must preserve UNKNOWN status for unresolved behavior
  so dir/component/architecture layers do not inherit inferred claims.
- Before accepting ctx quality >= 75, verify that key responsibilities and
  failure-path claims are traceable to concrete evidence.

Engineer emphasis
- Fidelity: every listed behavior must map to actual code paths.
- Coverage: include non-obvious error paths and side effects.
- Depth: specify invariants, inputs/outputs, and dependency rules.

References
- `agent_onboarding/default/engineer/policies/ctx_autonomy_rubric.md`
- `agent_onboarding/default/engineer/policies/engineer_quality_policy.md`



