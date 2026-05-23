
# secure_coding_review

Purpose
- Provide secure coding review checklists for implementation work.

Review checklist (common)
- Input validation and sanitization
- Output encoding where needed
- Avoid injection patterns (SQL, shell, template)
- Principle of least privilege
- Error handling does not leak sensitive info
- Logging does not include secrets
- Rate limiting / abuse protection where relevant

Rules
- If unsure, mark UNKNOWN and request deeper source reads or security requirements.

References
- `agent_onboarding/default/general/skills/security_and_secrets.md`


