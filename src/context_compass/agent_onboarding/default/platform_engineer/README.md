
# Platform Engineer Career

Purpose
- Platform-engineer-specific onboarding deltas on top of the shared `general` baseline and the `engineer` implementation baseline.
- Optimized for CI/CD, deployment, environments, observability, and operational safety.

Scope rule
- Keep only platform-engineer-specific policy/behavior here.
- Shared rules remain in:
  - `agent_onboarding/default/general/` (process, ticketing, gates, certification)
  - `agent_onboarding/default/engineer/` (implementation discipline and architecture docs mechanics)
- Platform Engineer extends `engineer` and must remain a delta layer:
  no path overlap with `agent_onboarding/default/engineer/SKILLS.MD`.

Platform Engineer inventory
- `agent_onboarding/default/platform_engineer/SKILLS.MD`: platform-engineer-specific read sequence.
- `skills/platform_engineer_execution.md`: platform execution discipline and artifact expectations.
- `skills/ci_cd_and_release.md`: pipeline design and release mechanics.
- `skills/deployment_and_environments.md`: deployment strategies, environment discipline, and rollback plans.
- `skills/infrastructure_as_code.md`: IaC discipline, drift control, and reproducibility.
- `skills/observability_and_monitoring.md`: logs/metrics/traces, SLOs, dashboards, alerting.
- `skills/incident_response_and_runbooks.md`: incident flow, runbooks, and postmortems.
- `skills/performance_capacity_cost.md`: capacity, performance, and cost guardrails.
- `skills/platform_security_basics.md`: production security posture (references security docs).
- `policies/platform_quality_policy.md`: quality and evidence bar for platform changes.
- `policies/production_change_management_policy.md`: safe-change gating for production.
- `policies/operational_safety_policy.md`: "do no harm" operational guardrails.
- `behavioral_guidelines/platform_engineer_workflow.md`: platform execution flow.
- `behavioral_guidelines/incident_workflow.md`: incident workflow story.
- `examples/platform_task_flow.md`: example platform task flow.

Overlap rules
- Implementation tasks still follow `engineer` execution discipline.
- Security-sensitive work should reference `security_engineer` guidance.

Unknowns Gate
- Apply the canonical policy in
  `agent_onboarding/default/general/skills/unknowns_gate_reference.md`.


