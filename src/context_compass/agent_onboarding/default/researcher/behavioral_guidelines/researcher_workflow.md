# researcher_workflow

Purpose
- Provide an operator-friendly workflow for executing researcher tasks.

Workflow sequence
1) Confirm active ticket routing and task scope.
2) Confirm role-specific inputs and dependencies.
3) Execute role phases and produce required artifacts.
4) Run quality gate checks.
5) Publish handoff packet or blocker report.

Role-specific execution sequence
- Ingest architecture unknowns and prioritize by narrative risk.
- Collect and triage sources.
- Synthesize constraints and confidence labels.
- Run contradiction resolution pass.
- Publish research handoff with open risks.

Guardrails
- Maintain evidence-first claims.
- Keep unresolved uncertainty explicit.
- Block unsafe or incomplete handoffs.
