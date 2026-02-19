# continuity_fact_checker_task_flow

Scenario
- Demonstrate a complete continuity_fact_checker pass with artifacts and gate decisions.

Example flow
1. Intake: validate scope and dependencies.
2. Execute role workflow and produce required artifacts.
3. Run quality checks and record gate outcome.
4. Build handoff packet with unresolved risks.
5. Transfer to downstream role or block with remediation path.

Expected outputs
- continuity_matrix.md
- timeline_validation.md
- fact_check_log.md
- canon_conflict_report.md
- resolution_recommendations.md

Expected pass conditions
- No unresolved high-severity canon conflicts.
- Factual red flags are resolved or explicitly waived.
- Timeline map is coherent and complete.
- Conflict logs include severity, evidence, and owner.
