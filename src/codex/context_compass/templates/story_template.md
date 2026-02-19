

# Story: <short, outcome-focused title>

## Metadata
- Story ID: STORY-YYYY-MM-DD-<slug>
- Epic: EPIC-YYYY-MM-DD-<slug>
- Status: draft | ready | in_progress | blocked | done
- Owner:
- Priority: p0 | p1 | p2 | p3
- Created: YYYY-MM-DDTHH:MM:SSZ
- Updated: YYYY-MM-DDTHH:MM:SSZ

## User Narrative
As a <user/persona>, I want <capability>, so that <outcome>.

## Value / MRP Alignment
<Explain how this story strengthens the holistic core.>

## Ticket Contract
- ENTRY_GATE: <active board row and linked task/story prerequisites satisfied>
- EXECUTION_BOUNDARY: <story-level surfaces allowed; no unrelated expansion>
- DEPENDENCIES: <task set and prerequisite tickets/stories/epic milestones>
- EXIT_GATE: <acceptance + child-task state + board-sync requirements>
- FAILURE_ESCALATION: <when to raise DECISION_REQUEST/CONFLICT/BLOCKER>

## Requirements (Functional)
- 

## Requirements (Non-Functional)
- 

## Scope Boundaries
- In scope:
- Out of scope:

## State Transition Event
- from_state: draft | ready | in_progress | blocked | review
- to_state: ready | in_progress | blocked | review | done
- transition_reason: <why this transition is valid now>

## Dependencies / Related Work
- 

## Tasks (Implementation Checklist)
- [ ] Task: <TASK-ID> - <short description>
- [ ] Task: <TASK-ID> - <short description>
- [ ] Enforce Ticket Microcycle across all linked tasks.
- [ ] Require meaningful-finding note updates during discovery/implementation.

## Acceptance Criteria
- 

## Validation / Test Plan
- 

## UX / API / Data Notes
- 

## Risks / Mitigations
- 

## Applicable Anti-Patterns
- [ ] No story-state transition without linked task-state evidence.
- [ ] No closure while required tasks remain active or un-routed.
- [ ] No cross-task synthesis claims without ticket-note evidence pointers.

## Open Questions
- 

## Decision Log
- 

## Artifact Links (Optional)
- ARTIFACTS_REQUIRED: true | false
- ARTIFACT_PATHS:
  - <artifacts/YYYY-MM-DD_<slug>.<ext>>
- DISPOSITION: delete_on_close | retain_as_reference | promote_to_documentation
- CLEANUP_TRIGGER: <when artifact cleanup/retention decision is applied>

## Notes
- DATETIME: YYYY-MM-DDTHH:MM:SSZ
  TYPE:
    FACT | UNKNOWN | HYPOTHESIS | DECISION | DECISION_REQUEST | PLAN |
    STRATEGY_DISCUSSION | ASSUMPTION_CHALLENGE | CONFLICT | TRADEOFF |
    BLOCKER | ALIGNMENT_CHECK | MEASURE | RISK | RAISE
  CLAIM: <short finding>
  EVIDENCE:
  - <path:start_line-end_line>
  - <path:start_line-end_line>
  IMPACT: <why this matters>
  NEXT: <one concrete next action>
  REREAD: REQUIRED | HELPFUL
  SCORE_0_TO_10: <0-10 compaction usefulness>

## Closure Confirmation
- [ ] Work walkthrough shared with user
- [ ] Acceptance criteria confirmed by user
- [ ] Applicable anti-pattern checks are clear or escalated with evidence.

## Noting Behavior
- Note focus: cross-task synthesis, dependency flow, and state-transition logic.
- Add notes when task routing changes, gate decisions are made, or risks shift.
- Reference child-task notes for evidence instead of duplicating tactical detail.
- Keep notes append-only and preserve UNKNOWN-first promotion discipline.

## Context / Handoff Summary
<Succinct summary of current state, key decisions, and next steps for future context.>



