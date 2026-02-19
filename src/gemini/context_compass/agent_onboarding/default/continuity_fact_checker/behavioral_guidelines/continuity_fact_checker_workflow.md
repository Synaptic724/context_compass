# continuity_fact_checker_workflow

Purpose
- Provide an operator-friendly workflow for executing continuity_fact_checker tasks.

Workflow sequence
1) Confirm active ticket routing and task scope.
2) Confirm role-specific inputs and dependencies.
3) Execute role phases and produce required artifacts.
4) Run quality gate checks.
5) Publish handoff packet or blocker report.

Role-specific execution sequence
- Ingest manuscript, style logs, and research evidence.
- Build entity-event timeline matrix.
- Run canon conflict and plausibility checks.
- Classify findings and propose resolutions.
- Publish conflict report and clearance status.

Guardrails
- Maintain evidence-first claims.
- Keep unresolved uncertainty explicit.
- Block unsafe or incomplete handoffs.
