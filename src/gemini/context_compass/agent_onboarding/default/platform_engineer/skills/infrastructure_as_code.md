
# infrastructure_as_code

Purpose
- Establish IaC discipline: reproducibility, auditability, drift control.

Core rules
- Treat IaC as code:
  - reviewable diffs,
  - tests/lints where possible,
  - small changesets.
- Never change infra manually without recording:
  - why it was needed,
  - what drift was introduced,
  - how to reconcile back to IaC.

Drift control
- Prefer automated drift detection.
- Any detected drift must become a ticket with remediation plan.

References
- `agent_onboarding/default/platform_engineer/policies/platform_quality_policy.md`


