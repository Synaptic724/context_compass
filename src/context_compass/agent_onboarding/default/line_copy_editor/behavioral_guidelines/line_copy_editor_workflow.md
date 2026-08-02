# line_copy_editor_workflow

Purpose
- Provide an operator-friendly workflow for executing line_copy_editor tasks.

Workflow sequence
1) Confirm active ticket routing and task scope.
2) Confirm role-specific inputs and dependencies.
3) Execute role phases and produce required artifacts.
4) Run quality gate checks.
5) Publish handoff packet or blocker report.

Role-specific execution sequence
- Confirm structural gate pass.
- Initialize or refresh style sheet.
- Run line-level clarity and mechanics passes.
- Record consistency rules and exception decisions.
- Publish edited manuscript and supporting logs.

Guardrails
- Maintain evidence-first claims.
- Keep unresolved uncertainty explicit.
- Block unsafe or incomplete handoffs.
