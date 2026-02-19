

# Tasks

## Purpose
Tasks are the smallest actionable units that produce concrete deliverables. They must be
precise, testable, and aligned with the MRP-first approach.

## MRP First (Required)
- Every task must contribute to a coherent, durable outcome.
- MRP means "reasonable," not "minimal." Avoid scope that forces a rewrite later.
- MVP shortcuts are disallowed. The task should not create debt that must be rewritten.
- Use MLP only when a task is explicitly about UI/UX polish after core stability.

## What Belongs Here
- A single, concrete unit of work with clear scope and deliverables.
- Work that can be validated and completed within a focused effort window.

## File Naming
Use date-first, descriptive names:
- `YYYY-MM-DD_<slug>_task.md`

Backlog location:
- park non-active tasks in `context_compass/tickets/tasks/backlog/`.

When completed, move to `context_compass/tickets/tasks/completed/` and rename to:
- `YYYY-MM-DD_<slug>_task_completed.md`

## How To Create A Task (Deep, Not Minimal)
1. Copy `context_compass/templates/task_template.md`.
2. Link the task to its story in Metadata.
3. Write a concrete Objective that defines the smallest meaningful outcome.
4. Fill `Ticket Contract` (`ENTRY_GATE`, `EXECUTION_BOUNDARY`,
   `DEPENDENCIES`, `EXIT_GATE`, `FAILURE_ESCALATION`).
5. Define Scope Boundaries (in scope / out of scope) to prevent creep.
6. Record a `State Transition Event` for status changes.
7. List Steps / Checklist with clear, ordered actions.
8. Define Deliverables and Files / Paths Impacted.
9. Record Validation status and recommended commands (or "Not run").
10. Capture Risks / Rollback Notes if relevant.
11. Fill `Applicable Anti-Patterns` with lane-specific checks (do not paste the
    full catalog).
12. Keep `Noting Behavior` aligned to tactical task-level notes and update
    `## Notes` on each meaningful finding.
13. Add `Artifact Links (Optional)` when the task creates supporting artifacts.
14. Record artifact disposition (`delete_on_close`, `retain_as_reference`, or
    `promote_to_documentation`) and closure trigger for each linked artifact.
15. Complete the Done Checklist and keep Context / Handoff Summary current.

## Depth Standard (No Handwaving)
- Be explicit about what will change and why.
- Reference relevant files, docs, or diagrams.
- Record open questions or blockers immediately.
- Keep notes tactical: concrete finding -> impact -> one-step next action.
- Keep anti-pattern enforcement lightweight: lane-specific checklist only.

## Completion Rules
- Add completion header at the top of the file (see `context_compass/agent_onboarding/default/general/skills/workflow.md`).
- Move the file to `context_compass/tickets/tasks/completed/` with the `_completed` suffix.

## References
- `context_compass/SKILLS.MD` (deep descriptive model and naming rules)
- `context_compass/agent_onboarding/default/general/skills/workflow.md` (ticket lifecycle and completion format)
- `context_compass/templates/task_template.md`



