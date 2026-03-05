
# platform_security_basics

Purpose
- Provide baseline security posture for platform work.

Core rules
- Secrets are never written to repo, tickets, logs, or chat transcripts.
- Least privilege:
  - scope credentials to the minimum permissions required.
- Auditability:
  - changes should be traceable to tickets and diffs.
- Dependency posture:
  - prefer pinned dependencies and explicit updates.

Escalation
- If the task is security sensitive or involves authn/authz changes:
  - route to security specialist guidance (if selected/available):
    `agent_onboarding/default/security_engineer/SKILLS.MD`

References
- `agent_onboarding/default/general/skills/security_and_secrets.md`
- `agent_onboarding/default/security_engineer/skills/threat_modeling.md`


