
# test_data_and_environments

Purpose
- Define test data management discipline and environment hygiene.

Test data rules
- Prefer synthetic/fixture-based data when possible.
- Avoid leaking sensitive data into tests or artifacts.
- Ensure cleanup and isolation:
  - tests must not depend on shared state unless explicitly designed.

Environment rules
- Do not assume dev == staging == prod.
- For environment-dependent behavior, document differences and test them explicitly.

References
- `agent_onboarding/default/general/skills/security_and_secrets.md`


