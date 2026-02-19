
# SKILLS.MD - qa_engineer

Purpose
- Define required baseline QA skills for the `qa_engineer` role.
- This role is optimized for test strategy, test design, and release quality posture.

Inheritance
- `INHERITS_SKILLS_FROM: agent_onboarding/default/engineer/SKILLS.MD`

Skill classes (non-negotiable)
- This role defines two classes of skills:
  A) **Required baseline skills** (always required for onboarding/certification)
  B) **On-demand QA-context skills** (required only when the active task triggers them)

Rules
- You MUST read **all** paths listed under **Required baseline skills** for this role
  to be considered onboarded/certifiable as `qa_engineer`.
- You MUST NOT claim an on-demand skill was read unless:
  1) a trigger condition was met, AND
  2) you actually read it in full.
- When a trigger condition is met, the on-demand skills become mandatory and MUST be
  read **before** any work in that scope.

Required baseline skills
- `agent_onboarding/default/qa_engineer/AGENTS.MD`
- `agent_onboarding/default/qa_engineer/skills/qa_engineer_execution.md`
- `agent_onboarding/default/qa_engineer/skills/test_strategy_and_planning.md`
- `agent_onboarding/default/qa_engineer/skills/test_case_design.md`
- `agent_onboarding/default/qa_engineer/skills/test_automation_practices.md`
- `agent_onboarding/default/qa_engineer/skills/regression_and_release_quality.md`
- `agent_onboarding/default/qa_engineer/skills/bug_triage_and_repro.md`
- `agent_onboarding/default/qa_engineer/skills/test_data_and_environments.md`
- `agent_onboarding/default/qa_engineer/skills/quality_metrics.md`
- `agent_onboarding/default/qa_engineer/policies/quality_gate_policy.md`
- `agent_onboarding/default/qa_engineer/policies/defect_severity_policy.md`
- `agent_onboarding/default/qa_engineer/policies/test_evidence_policy.md`
- `agent_onboarding/default/qa_engineer/behavioral_guidelines/qa_workflow.md`
- `agent_onboarding/default/qa_engineer/behavioral_guidelines/release_signoff_workflow.md`
- `agent_onboarding/default/qa_engineer/examples/qa_task_flow.md`

On-demand QA-context skills
Trigger conditions (any one makes these mandatory):
- The task requires building or changing test architecture, harnesses, or CI test stages.
- The task requires release signoff or quality gating decisions.
- The task requires deep analysis of regression risk.

If triggered:
- Inherit and apply the `engineer` on-demand system-context readset defined in:
  `agent_onboarding/default/engineer/SKILLS.MD`


