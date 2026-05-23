
# security_review_policy

Purpose
- Enforce security review gating for security-sensitive work.

Policy
Security review is mandatory when a task touches:
- authn/authz, permissions, tokens, sessions,
- secrets, cryptography,
- sensitive/PII data handling,
- audit logging,
- dependency additions or major upgrades.

Review rule
- Provide a threat model or security checklist summary.
- Request explicit approval for high-risk changes.

References
- `agent_onboarding/default/security_engineer/skills/threat_modeling.md`


