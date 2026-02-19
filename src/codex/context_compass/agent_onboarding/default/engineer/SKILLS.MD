

# SKILLS.MD - engineer

Purpose
- Define required baseline engineering skills for the `engineer` role.

Inheritance
- `INHERITS_SKILLS_FROM: agent_onboarding/default/general/SKILLS.MD`

Skill classes (non-negotiable)
- This role defines two classes of skills:
  A) **Required baseline skills** (always required for onboarding/certification)
  B) **On-demand system-context skills** (required only when the active task triggers them)

Rules
- You MUST read **all** paths listed under **Required baseline skills** for this role
  to be considered onboarded/certifiable as `engineer`.
- You MUST NOT claim an on-demand skill was read unless:
  1) a trigger condition was met, AND
  2) you actually read it in full.
- When a trigger condition is met, the on-demand skills become mandatory and MUST be
  read **before** any work in that scope.

Required baseline skills
- `agent_onboarding/default/engineer/AGENTS.MD`
- `agent_onboarding/default/engineer/skills/engineer_execution.md`
- `agent_onboarding/default/engineer/skills/technical_expertise.md`
- `agent_onboarding/default/engineer/skills/system_orientation.md`
- `agent_onboarding/default/engineer/skills/documentation_standards.md`
- `agent_onboarding/default/engineer/skills/context_protocol.md`
- `agent_onboarding/default/engineer/skills/staleness_protocol.md`
- `agent_onboarding/default/engineer/policies/engineer_quality_policy.md`
- `agent_onboarding/default/engineer/policies/ctx_autonomy_policy.md`
- `agent_onboarding/default/engineer/policies/ctx_autonomy_rubric.md`
- `agent_onboarding/default/engineer/behavioral_guidelines/engineer_workflow.md`
- `agent_onboarding/default/engineer/behavioral_guidelines/task_execution_and_validation.md`
- `agent_onboarding/default/engineer/examples/artifact_workflow.md`
- `agent_onboarding/default/engineer/examples/eng_task_flow.md`

On-demand system-context skills
Trigger conditions (any one makes these mandatory):
- The active ticket requires architecture/system documentation work.
- The task touches `system_docs/` or claims about system/runtime/test architecture are required.
- You are changing cross-cutting behavior that depends on documented architecture or component boundaries.
- The user explicitly requests an architecture/components/tests deep dive.

If triggered, you MUST read the relevant items below (do not skip):
- `system_docs/tests_architecture.md`
- `system_docs/tests_components.md`
- `system_docs/src_architecture.md`
- `system_docs/src_components.md`
