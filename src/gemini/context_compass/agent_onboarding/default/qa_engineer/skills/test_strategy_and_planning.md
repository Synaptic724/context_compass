
# test_strategy_and_planning

Purpose
- Provide a repeatable method for building a test strategy for a feature or system.

Strategy steps
1) Identify acceptance criteria.
2) Identify failure modes and risky integrations.
3) Choose test layers:
   - unit (fast, isolated),
   - integration (module boundaries),
   - end-to-end (critical user journeys).
4) Define test data strategy:
   - fixtures, seeds, anonymized data,
   - determinism and cleanup.
5) Define quality gates:
   - what blocks merge/release.
6) Define observability for validation:
   - logs/metrics to confirm behavior in environments.

Output format (recommended)
- Acceptance criteria:
- Risk areas:
- Test layers:
- Key test cases:
- Test data:
- Quality gates:
- Evidence plan:


