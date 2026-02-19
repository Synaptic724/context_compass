

# Stories

## Purpose
Stories define a user- or system-facing slice of value within an epic. They translate an
epic outcome into a coherent, testable unit of delivery that strengthens the MRP core.

## MRP First (Required)
- Every story must explain how it hardens or extends the core system.
- MRP means "reasonable," not "minimal." Avoid scope that forces a rewrite later.
- MVP framing is disallowed. Do not trade durability for speed.
- MLP is allowed only when the story is explicitly about UI/UX polish.

## What Belongs Here
- A single, cohesive slice of value inside one epic.
- A scope that can be completed by a small set of tasks with clear deliverables.

## File Naming
Use date-first, descriptive names:
- `YYYY-MM-DD_<slug>_story.md`

Backlog location:
- park non-active stories in `context_compass/tickets/stories/backlog/`.

When completed, move to `context_compass/tickets/stories/completed/` and rename to:
- `YYYY-MM-DD_<slug>_story_completed.md`

## How To Create A Story (Deep, Not Minimal)
1. Copy `context_compass/templates/story_template.md`.
2. Link the story to its epic in Metadata.
3. Write a precise User Narrative with a concrete outcome.
4. Explain Value / MRP Alignment with system-level impact.
5. Fill `Ticket Contract` (`ENTRY_GATE`, `EXECUTION_BOUNDARY`,
   `DEPENDENCIES`, `EXIT_GATE`, `FAILURE_ESCALATION`).
6. Define Functional + Non-Functional requirements.
7. Set Scope Boundaries and list Dependencies.
8. Record a `State Transition Event` for status changes.
9. Create a task checklist with explicit task IDs.
10. Define Acceptance Criteria that are observable and testable.
11. Add Validation / Test Plan and any UX/API/Data notes.
12. Fill `Applicable Anti-Patterns` with lane-specific checks (not full catalog).
13. Keep `Noting Behavior` aligned to cross-task synthesis notes.
14. Add `Artifact Links (Optional)` when story work produces supporting
    artifacts.
15. Record artifact disposition (`delete_on_close`, `retain_as_reference`, or
    `promote_to_documentation`) for linked artifacts.
16. Record Risks / Mitigations, Decision Log, and keep Context / Handoff
    Summary current.

## Depth Standard (No Handwaving)
- Cite relevant code paths, docs, or diagrams.
- Make uncertainties and open questions explicit.
- Write so a future reader can execute without additional context.
- Keep notes synthesis-focused (task outcomes, dependency shifts, gate changes).

## Completion Rules
- Add completion header at the top of the file (see `context_compass/agent_onboarding/default/general/skills/workflow.md`).
- Move the file to `context_compass/tickets/stories/completed/` with the `_completed` suffix.

## References
- `context_compass/SKILLS.md` (deep descriptive model and naming rules)
- `context_compass/agent_onboarding/default/general/skills/workflow.md` (ticket lifecycle and completion format)
- `context_compass/templates/story_template.md`




