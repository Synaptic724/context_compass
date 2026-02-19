
# test_automation_practices

Purpose
- Provide test automation discipline to keep tests maintainable and trustworthy.

Core rules
- Make tests deterministic:
  - control time, randomness, and external dependencies.
- Avoid flaky tests:
  - isolate sources of nondeterminism,
  - use retries only as last resort and document why.
- Keep tests readable:
  - clear naming,
  - minimal setup,
  - explicit assertions.

Automation scope
- Automate:
  - regression-prone areas,
  - critical paths,
  - complex logic with high change frequency.
- Leave exploratory testing for:
  - UX flows,
  - unpredictable integration behavior.

References
- `agent_onboarding/default/engineer/policies/engineer_quality_policy.md`


