

# engineer_execution

Purpose
- Define how engineer agents plan and implement code changes in this
  repository.

Core rules
- Follow `AGENTS.MD` and the shared baseline skills in
  `agent_onboarding/default/general/`.
- Propose a plan before editing; keep scope tight and reviewable.
- Follow repository SQL rules in `AGENTS.MD` when touching SQL tools.
- Update docstrings for every touched function/class and add tests for
  behavioral changes.
- Keep scratch ideas and todos in `workspace/agent/`.
- Promote durable plans and execution artifacts into `tickets/epics/`,
  `tickets/stories/`, `tickets/tasks/`, and their completed folders.

Preferred workflow
1) Clarify the goal, constraints, and affected files.
2) Route from `attention_board.md` to the active ticket and follow the Ticket
   Microcycle.
3) Review existing docstrings and contracts in the target modules.
4) Implement changes with small, cohesive functions and explicit error handling.
5) Run tests (or report "Not run" with reasoning).
6) Summarize changes and list follow-ups.

Artifact discipline (engineer)
- Ideas/opinions/todo: `workspace/agent/` only.
- Plans and scope control: use `templates/` and create tickets in
  `tickets/epics/`, `tickets/stories/`, `tickets/tasks/`.
- Status updates: keep `attention_board.md` current and append detailed
  findings to ticket `## Notes`.
- Closures: move completed tickets to their matching completed folder with
  summary + date.
- Convert approved todos into tickets instead of leaving them in scratch.

Examples
- `agent_onboarding/default/engineer/examples/artifact_workflow.md`

References
- `AGENTS.MD`
- `agent_onboarding/default/general/skills/workflow.md`


