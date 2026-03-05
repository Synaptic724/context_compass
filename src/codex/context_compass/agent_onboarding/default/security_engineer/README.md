
# Security Engineer Career

Purpose
- Security-engineer-specific onboarding deltas on top of the shared `general` baseline and the `engineer` implementation baseline.
- Optimized for threat modeling, secure design reviews, dependency risk, and vulnerability handling.

Scope rule
- Keep only security-engineer-specific policy/behavior here.
- Shared rules remain in:
  - `agent_onboarding/default/general/` (process, ticketing, gates, certification)
  - `agent_onboarding/default/engineer/` (implementation discipline and architecture docs mechanics)
- Security Engineer extends `engineer` and must remain a delta layer:
  no path overlap with `agent_onboarding/default/engineer/SKILLS.MD`.

Security Engineer inventory
- `agent_onboarding/default/security_engineer/SKILLS.MD`: security-engineer-specific read sequence.
- `skills/security_engineer_execution.md`: security execution discipline and artifacts.
- `skills/threat_modeling.md`: threat model method and output structure.
- `skills/secure_architecture_review.md`: architecture review for security posture.
- `skills/secure_coding_review.md`: secure coding review checklist.
- `skills/dependency_and_supply_chain.md`: dependency and supply-chain risk posture.
- `skills/vulnerability_management.md`: triage, remediation, and disclosure discipline.
- `skills/authn_authz_basics.md`: authn/authz design review checklist.
- `skills/logging_audit_privacy.md`: audit logging and privacy considerations.
- `skills/incident_response_security.md`: security incident workflow.
- `policies/security_review_policy.md`: mandatory review gates for security-sensitive work.
- `policies/risk_acceptance_policy.md`: risk acceptance and approval rules.
- `policies/secrets_and_keys_policy.md`: secrets/keys discipline (references baseline secrets policy).
- `behavioral_guidelines/security_workflow.md`: security execution flow.
- `behavioral_guidelines/security_signoff_and_escalation.md`: escalation and signoff workflow.
- `examples/security_review_flow.md`: example security review flow.

Overlap rules
- Use baseline secrets policy as canonical:
  `agent_onboarding/default/general/skills/security_and_secrets.md`.
- For operational/incident posture, reference `platform_engineer` guidance.

Unknowns Gate
- Apply the canonical policy in
  `agent_onboarding/default/general/skills/unknowns_gate_reference.md`.


