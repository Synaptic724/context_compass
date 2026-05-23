
# regression_and_release_quality

Purpose
- Define how to reason about regression risk and release readiness.

Regression posture
- Identify change surface:
  - what code paths are affected,
  - what integrations are touched,
  - what data migrations happen.
- Ensure coverage across:
  - happy path,
  - error path,
  - edge cases,
  - rollback/backout scenarios when relevant.

Release readiness checklist
- Test suite status (what ran, what didn't)
- Open defects and severity
- Known risks and mitigations
- Rollout and monitoring plan (if behavior changes)

References
- `agent_onboarding/default/qa_engineer/policies/quality_gate_policy.md`
- `agent_onboarding/default/platform_engineer/skills/deployment_and_environments.md`


