
# qa_engineer_execution

Purpose
- Define how QA engineers produce test strategies and quality evidence.
- Turn features into testable acceptance criteria with explicit risk coverage.

Core rules
- Follow `AGENTS.MD` and the shared baseline skills in `agent_onboarding/default/general/`.
- "Covered" means tests exist and can be pointed to, not just "should work".
- Prefer high-signal tests:
  - small number of strong tests over many weak tests.

Preferred workflow
1) Clarify the requirement and acceptance criteria.
2) Identify risk areas and failure modes.
3) Propose test strategy:
   - unit/integration/e2e split,
   - test data strategy,
   - regression posture.
4) Define quality gates and release criteria.
5) Implement tests (if requested) using `engineer` discipline.
6) Validate and report evidence.

References
- `agent_onboarding/default/qa_engineer/policies/test_evidence_policy.md`
- `agent_onboarding/default/engineer/skills/engineer_execution.md`


