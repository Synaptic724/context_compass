
# SKILLS.MD - design_engineer

Purpose
- Define required baseline design-engineer skills for the `design_engineer` role.
- This role is optimized for designing software engineering projects with high-quality handoff.

Inheritance
- `INHERITS_SKILLS_FROM: agent_onboarding/default/engineer/SKILLS.MD`

Skill classes (non-negotiable)
- This role defines two classes of skills:
  A) **Required baseline skills** (always required for onboarding/certification)
  B) **On-demand design-context skills** (required only when the active task triggers them)

Rules
- You MUST read **all** paths listed under **Required baseline skills** for this role
  to be considered onboarded/certifiable as `design_engineer`.
- You MUST NOT claim an on-demand skill was read unless:
  1) a trigger condition was met, AND
  2) you actually read it in full.
- When a trigger condition is met, the on-demand skills become mandatory and MUST be
  read **before** any work in that scope.

Required baseline skills
- `agent_onboarding/default/design_engineer/AGENTS.MD`
- `agent_onboarding/default/design_engineer/skills/architecture_contexts.md`
- `agent_onboarding/default/design_engineer/skills/src_architecture_instructions.md`
- `agent_onboarding/default/design_engineer/skills/src_components_instructions.md`
- `agent_onboarding/default/design_engineer/skills/tests_architecture_instructions.md`
- `agent_onboarding/default/design_engineer/skills/tests_components_instructions.md`
- `agent_onboarding/default/design_engineer/skills/design_engineer_execution.md`
- `agent_onboarding/default/design_engineer/skills/requirements_to_architecture.md`
- `agent_onboarding/default/design_engineer/skills/system_design_method.md`
- `agent_onboarding/default/design_engineer/skills/decomposition_and_boundaries.md`
- `agent_onboarding/default/design_engineer/skills/api_and_interface_design.md`
- `agent_onboarding/default/design_engineer/skills/data_modeling.md`
- `agent_onboarding/default/design_engineer/skills/architecture_tradeoffs.md`
- `agent_onboarding/default/design_engineer/skills/adr_and_decision_hygiene.md`
- `agent_onboarding/default/design_engineer/skills/nonfunctional_requirements.md`
- `agent_onboarding/default/design_engineer/skills/design_review_protocol.md`
- `agent_onboarding/default/design_engineer/policies/design_quality_policy.md`
- `agent_onboarding/default/design_engineer/policies/decision_record_policy.md`
- `agent_onboarding/default/design_engineer/policies/design_review_policy.md`
- `agent_onboarding/default/design_engineer/behavioral_guidelines/design_engineer_workflow.md`
- `agent_onboarding/default/design_engineer/behavioral_guidelines/design_validation_and_handoff.md`
- `agent_onboarding/default/design_engineer/examples/design_task_flow.md`
- `agent_onboarding/default/design_engineer/examples/adr_example.md`

On-demand design-context skills
Trigger conditions (any one makes these mandatory):
- The user asks for a full system/software design, architecture plan, or component boundary redesign.
- The task requires a design that changes an existing public contract, API, schema, or lifecycle boundary.
- The task requires creating/updating `system_docs/*` or making P0/P1 claims about architecture/components/tests.

If triggered:
- Inherit and apply the `engineer` on-demand system-context readset defined in:
  `agent_onboarding/default/engineer/SKILLS.MD`
- Do not proceed with architecture claims or edits until that on-demand readset is satisfied.

