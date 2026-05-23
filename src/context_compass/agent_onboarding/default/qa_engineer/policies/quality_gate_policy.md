
# quality_gate_policy

Purpose
- Establish release/merge quality gates.

Policy (default)
- Block release/merge when:
  - critical P0 defects are open,
  - core test suite is failing,
  - coverage is missing for critical acceptance criteria.
- If tests were not run, say so explicitly and explain why.
- Any gate exception requires explicit approval.

References
- `agent_onboarding/default/qa_engineer/policies/test_evidence_policy.md`


