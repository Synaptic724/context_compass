
# SKILLS.MD - platform_engineer

Purpose
- Define required baseline platform skills for the `platform_engineer` role.
- This role is optimized for CI/CD, deployments, observability, and operational safety.

Inheritance
- `INHERITS_SKILLS_FROM: agent_onboarding/default/engineer/SKILLS.MD`

Skill classes (non-negotiable)
- This role defines two classes of skills:
  A) **Required baseline skills** (always required for onboarding/certification)
  B) **On-demand platform-context skills** (required only when the active task triggers them)

Rules
- You MUST read **all** paths listed under **Required baseline skills** for this role
  to be considered onboarded/certifiable as `platform_engineer`.
- You MUST NOT claim an on-demand skill was read unless:
  1) a trigger condition was met, AND
  2) you actually read it in full.
- When a trigger condition is met, the on-demand skills become mandatory and MUST be
  read **before** any work in that scope.

Required baseline skills
- `agent_onboarding/default/platform_engineer/AGENTS.MD`
- `agent_onboarding/default/platform_engineer/skills/platform_engineer_execution.md`
- `agent_onboarding/default/platform_engineer/skills/ci_cd_and_release.md`
- `agent_onboarding/default/platform_engineer/skills/deployment_and_environments.md`
- `agent_onboarding/default/platform_engineer/skills/infrastructure_as_code.md`
- `agent_onboarding/default/platform_engineer/skills/observability_and_monitoring.md`
- `agent_onboarding/default/platform_engineer/skills/incident_response_and_runbooks.md`
- `agent_onboarding/default/platform_engineer/skills/performance_capacity_cost.md`
- `agent_onboarding/default/platform_engineer/skills/platform_security_basics.md`
- `agent_onboarding/default/platform_engineer/policies/platform_quality_policy.md`
- `agent_onboarding/default/platform_engineer/policies/production_change_management_policy.md`
- `agent_onboarding/default/platform_engineer/policies/operational_safety_policy.md`
- `agent_onboarding/default/platform_engineer/behavioral_guidelines/platform_engineer_workflow.md`
- `agent_onboarding/default/platform_engineer/behavioral_guidelines/incident_workflow.md`
- `agent_onboarding/default/platform_engineer/examples/platform_task_flow.md`

On-demand platform-context skills
Trigger conditions (any one makes these mandatory):
- The task changes CI/CD pipelines, deployment scripts, or environment configuration.
- The task affects observability, monitoring, alerting, or incident response.
- The task introduces new operational risk or production behavior changes.

If triggered:
- Inherit and apply the `engineer` on-demand system-context readset defined in:
  `agent_onboarding/default/engineer/SKILLS.MD`
- Do not proceed with production-impact changes until relevant sources are read.


