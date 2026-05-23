
# test_case_design

Purpose
- Teach high-signal test case design that catches real regressions.

High-signal patterns
- Boundary tests:
  - min/max sizes, empty/null behavior, off-by-one.
- Invariant tests:
  - properties that must always hold.
- State transition tests:
  - lifecycle sequencing and cleanup.
- Error semantics tests:
  - correct error codes and messages, retry behavior.
- Regression tests:
  - tests that reproduce known bugs.

Rules
- One test = one claim.
- Tests must be deterministic and easy to understand.
- Prefer readable failures over clever assertions.

References
- `agent_onboarding/default/qa_engineer/policies/defect_severity_policy.md`


