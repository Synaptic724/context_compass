
# test_evidence_policy

Purpose
- Require evidence for any test/quality claims.

Policy
- When claiming coverage or correctness, include evidence:
  - test file paths and test names,
  - CI command + result summary,
  - or explicit statement that tests were not run.
- Never pretend tests were run.
- If tool output truncates, summarize deterministically and provide pointers.

References
- `agent_onboarding/default/engineer/policies/engineer_quality_policy.md`


