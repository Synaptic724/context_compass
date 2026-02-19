
# quality_metrics

Purpose
- Define quality metrics that are actionable, not vanity.

Actionable metrics
- Defect rate by severity
- Flake rate (and trend)
- Mean time to detect regressions
- Coverage of critical paths (qualitative mapping to requirements)
- Escaped defects (prod issues) and root cause categories

Rules
- Do not optimize for metrics alone.
- Metrics must drive action:
  - fix flaky tests,
  - add missing coverage,
  - improve release gates.

References
- `agent_onboarding/default/qa_engineer/policies/quality_gate_policy.md`


