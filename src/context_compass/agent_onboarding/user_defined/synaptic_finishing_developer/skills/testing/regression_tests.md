# regression_tests

Purpose
- Define how this role writes regression tests that lock down previously
  observed failures without overfitting to implementation details.

Rules
- Name the test after the symptom.
- Keep the reproduction minimal.
- Assert the corrected behavior, not the internal workaround.
- Prefer a regression test whenever a docstring or comment is updated to record
  a historically broken contract.

High-value regression signals
- bug symptom is obvious from the test name
- failure is reproducible in a small setup
- the final assertion matches the public contract the repo wants to keep

Finishing-role emphasis
- If documentation becomes more explicit because a bug taught us something,
  pair that stronger documentation with a regression test whenever practical.

References
- `agent_onboarding/user_defined/synaptic_python_developer/skills/testing/regression_tests.md`
