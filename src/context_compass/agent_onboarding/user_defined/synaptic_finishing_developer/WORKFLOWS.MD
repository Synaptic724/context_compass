# WORKFLOWS.MD - synaptic_finishing_developer

Purpose
- Define role-local workflow availability for the
  `synaptic_finishing_developer` role.

Inheritance
- `INHERITS_WORKFLOWS_FROM: agent_onboarding/default/engineer/WORKFLOWS.MD`

Activation rule
- This role inherits workflow behavior from `general` then `engineer`.
- Additional finishing workflows, when created, are user-generated and
  user-approved only.

Active workflows
- `agent_onboarding/user_defined/synaptic_finishing_developer/workflows/polish_repo_documentation.md`
- `agent_onboarding/user_defined/synaptic_finishing_developer/workflows/optimize_pytests_for_repo.md`
