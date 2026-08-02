# proofreader_workflow

Purpose
- Provide an operator-friendly workflow for executing proofreader tasks.

Workflow sequence
1) Confirm active ticket routing and task scope.
2) Confirm role-specific inputs and dependencies.
3) Execute role phases and produce required artifacts.
4) Run quality gate checks.
5) Publish handoff packet or blocker report.

Role-specific execution sequence
- Ingest continuity-cleared manuscript.
- Run typo and punctuation pass.
- Run format and style-lock pass.
- Finalize waivers and issue logs.
- Publish final manuscript and lock confirmation.

Guardrails
- Maintain evidence-first claims.
- Keep unresolved uncertainty explicit.
- Block unsafe or incomplete handoffs.
