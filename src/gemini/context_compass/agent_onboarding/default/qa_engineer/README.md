
# QA Engineer Career

Purpose
- QA-engineer-specific onboarding deltas on top of the shared `general` baseline and the `engineer` implementation baseline.
- Optimized for test strategy, test design, quality gates, and release signoff.

Scope rule
- Keep only QA-engineer-specific policy/behavior here.
- Shared rules remain in:
  - `agent_onboarding/default/general/` (process, ticketing, gates, certification)
  - `agent_onboarding/default/engineer/` (implementation discipline and architecture docs mechanics)
- QA Engineer extends `engineer` and must remain a delta layer:
  no path overlap with `agent_onboarding/default/engineer/SKILLS.MD`.

QA Engineer inventory
- `agent_onboarding/default/qa_engineer/SKILLS.MD`: QA-engineer-specific read sequence.
- `skills/qa_engineer_execution.md`: QA execution discipline and artifacts.
- `skills/test_strategy_and_planning.md`: how to build a test strategy for a feature/system.
- `skills/test_case_design.md`: how to design high-signal test cases.
- `skills/test_automation_practices.md`: test automation discipline and maintainability.
- `skills/regression_and_release_quality.md`: regression posture and release readiness.
- `skills/bug_triage_and_repro.md`: bug triage, repro steps, and severity.
- `skills/test_data_and_environments.md`: test data management and environment discipline.
- `skills/quality_metrics.md`: quality metrics that are actionable (not vanity).
- `policies/quality_gate_policy.md`: release quality gates.
- `policies/defect_severity_policy.md`: defect severity classification.
- `policies/test_evidence_policy.md`: evidence requirements for quality claims.
- `behavioral_guidelines/qa_workflow.md`: QA execution flow.
- `behavioral_guidelines/release_signoff_workflow.md`: release signoff workflow.
- `examples/qa_task_flow.md`: example QA task flow.

Overlap rules
- Implementation work still follows `engineer` execution discipline.
- For design-first tasks, reference `design_engineer` artifacts.

Unknowns Gate
- Apply the canonical policy in
  `agent_onboarding/default/general/skills/unknowns_gate_reference.md`.


