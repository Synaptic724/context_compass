
# SKILLS.MD - security_engineer

Purpose
- Define required baseline security skills for the `security_engineer` role.
- This role is optimized for threat modeling, secure reviews, and vulnerability handling.

Inheritance
- `INHERITS_SKILLS_FROM: agent_onboarding/default/engineer/SKILLS.MD`

Skill classes (non-negotiable)
- This role ADDS two classes of its own:
  A) **Required baseline skills** (always required for onboarding/certification)
  B) **On-demand security-context skills** (required only when the active task triggers them)
- It also INHERITS the parent chain's classes, which include `engineer`'s
  **Baseline system orientation** - `system_docs/system_docs_read_first.md`,
  `src_architecture.md`, `src_architecture_index.md`, `src_components_index.md`.
  Those are baseline for this role too. This section describes what this file adds;
  it is not the complete list of what you must read.

Rules
- You MUST read **all** paths listed under **Required baseline skills** for this role
  to be considered onboarded/certifiable as `security_engineer`, **plus** every
  baseline section in the inherited chain.
- You MUST NOT claim an on-demand skill was read unless:
  1) a trigger condition was met, AND
  2) you actually read it in full.
- When a trigger condition is met, the on-demand skills become mandatory and MUST be
  read **before** any work in that scope.

Required baseline skills
- `agent_onboarding/default/security_engineer/AGENTS.MD`
- `agent_onboarding/default/security_engineer/WORKFLOWS.MD`
- `agent_onboarding/default/security_engineer/skills/security_engineer_execution.md`
- `agent_onboarding/default/security_engineer/skills/threat_modeling.md`
- `agent_onboarding/default/security_engineer/skills/secure_architecture_review.md`
- `agent_onboarding/default/security_engineer/skills/secure_coding_review.md`
- `agent_onboarding/default/security_engineer/skills/dependency_and_supply_chain.md`
- `agent_onboarding/default/security_engineer/skills/vulnerability_management.md`
- `agent_onboarding/default/security_engineer/skills/authn_authz_basics.md`
- `agent_onboarding/default/security_engineer/skills/logging_audit_privacy.md`
- `agent_onboarding/default/security_engineer/skills/incident_response_security.md`
- `agent_onboarding/default/security_engineer/policies/security_review_policy.md`
- `agent_onboarding/default/security_engineer/policies/risk_acceptance_policy.md`
- `agent_onboarding/default/security_engineer/policies/secrets_and_keys_policy.md`
- `agent_onboarding/default/security_engineer/behavioral_guidelines/security_workflow.md`
- `agent_onboarding/default/security_engineer/behavioral_guidelines/security_signoff_and_escalation.md`
- `agent_onboarding/default/security_engineer/examples/security_review_flow.md`

On-demand security-context skills
Trigger conditions (any one makes these mandatory):
- The task touches authn/authz, permissions, secrets, cryptography, or sensitive data handling.
- The task changes logging, audit trails, or privacy-sensitive behavior.
- The user asks for threat modeling or security review as a primary deliverable.

If triggered:
- Apply the `engineer` on-demand system-context readset. The inheritance
  header at the top of this file already puts it in the resolved chain, so
  the paths are declared in the parent file and are not repeated here. The
  triggers above are additional to the parent's, not a replacement.


