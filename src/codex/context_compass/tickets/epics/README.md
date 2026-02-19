

# Epics

## Purpose
Epics capture multi-story outcomes that define durable, MRP-aligned changes. They are the
top-level planning unit and must be rich enough to survive context compaction.

## MRP First (Required)
- Every epic must describe the holistic core being built and why it is the right foundation.
- MRP means "reasonable," not "minimal." Avoid scope that forces a rewrite later.
- MVP framing is disallowed. If there is doubt, default to MRP and durability.
- Use MLP only when explicitly tied to UI/UX polish after the core is solid.

## What Belongs Here
- Multi-story outcomes that change core system behavior or architecture.
- Cross-cutting initiatives that require multiple stories and tasks.
- Policy or documentation programs that affect how we work or ship.

## File Naming
Use date-first, descriptive names:
- `YYYY-MM-DD_<slug>_epic.md`

Backlog location:
- park non-active epics in `context_compass/tickets/epics/backlog/`.

When completed, move to `context_compass/tickets/epics/completed/` and rename to:
- `YYYY-MM-DD_<slug>_epic_completed.md`

## How To Create An Epic (Deep, Not Minimal)
1. Copy `context_compass/templates/epic_template.md`.
2. Fill Metadata and keep `Status` and `Updated` current.
3. Document Problem / Opportunity with concrete evidence and context.
4. Write MRP Alignment as a durable, coherent core (not a quick experiment).
5. Fill `Ticket Contract` (`ENTRY_GATE`, `EXECUTION_BOUNDARY`,
   `DEPENDENCIES`, `EXIT_GATE`, `FAILURE_ESCALATION`).
6. Define Goals, Non-Goals, Scope Boundaries, and Requirements.
7. Record a `State Transition Event` for status changes.
8. Add Success Metrics and Acceptance Criteria that are observable.
9. Add Milestones with clear success criteria (`- [ ]` checkboxes required).
10. List Stories required to complete the epic, each with an ID.
11. Add Epic-level Tasks like "Complete story <STORY-ID>" to make progress explicit.
12. Fill `Applicable Anti-Patterns` with program-level checks (not full catalog).
13. Keep `Noting Behavior` focused on cross-story tradeoffs and sequencing.
14. Add `Artifact Links (Optional)` only when the epic tracks concrete artifacts.
15. Record artifact disposition (`delete_on_close`, `retain_as_reference`, or
    `promote_to_documentation`) for linked artifacts.
16. Record Risks / Mitigations, Validation plan, and Decision Log.
17. Keep the Context / Handoff Summary current and specific (context is gold).

## Depth Standard (No Handwaving)
- Use concrete evidence and references (docs, code paths, diagrams).
- Make assumptions explicit and list open questions.
- Write so a future reader can resume without hidden knowledge.
- Keep notes program-level; reference story/task notes for tactical evidence.

## Completion Rules
- Add completion header at the top of the file (see `context_compass/agent_onboarding/default/general/skills/workflow.md`).
- Move the file to `context_compass/tickets/epics/completed/` with the `_completed` suffix.

## References
- `context_compass/SKILLS.MD` (deep descriptive model and naming rules)
- `context_compass/agent_onboarding/default/general/skills/workflow.md` (ticket lifecycle and completion format)
- `context_compass/templates/epic_template.md`




