
# authn_authz_basics

Purpose
- Provide a checklist for reviewing authentication and authorization designs.

Checklist
- Authentication mechanism and session/token model
- Authorization model:
  - roles/permissions,
  - object-level access controls,
  - default-deny behavior.
- Auditability:
  - security-relevant actions are logged appropriately.
- Abuse protection:
  - rate limiting, lockouts, throttling.

Rules
- Auth is security-critical: request explicit approval for non-trivial changes.

References
- `agent_onboarding/default/security_engineer/policies/security_review_policy.md`


