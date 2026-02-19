

# Engineer Example: Artifact Workflow

Context
- A engineer needs to refactor Spellbook cleanup to keep logger teardown last.
- The agent wants to capture scratch thoughts before committing to a ticket.

Scratch capture (workspace)
- Path: `workspace/agent/ideas/interceptor_cleanup_refactor.md`
- Example content:

```md
# idea: spellbook_cleanup_ordering
## Why now
- logger cleanup runs early, masking downstream cleanup errors.
- failures show inconsistent logger teardown ordering across tests.

## Early hypothesis
- keep logger cleanup as the final cleanup step.
- capture cleanup ordering expectations in integration tests.

## Risk notes
- cleanup ordering changes could hide existing cleanup bugs.
- logger cleanup late may surface new exceptions.

## Promote when
- tests consistently pass after repeated attach/detach cycles.
```

- Path: `workspace/agent/todo/interceptor_cleanup_refactor.md`
- Example content:

```md
# todo: spellbook_cleanup_ordering
- [ ] trace cleanup ordering in Spellbook._cleanup_core
- [ ] ensure logger cleanup remains last
- [ ] confirm integration logging tests cover the ordering
```

Promote to ticket (curated)
- Path: `tickets/stories/YYYY-MM-DD_interceptor_cleanup_story.md`
- Example content:

```md
# story: spellbook_cleanup_ordering
## Goal
- cleanup ordering keeps logger teardown last and deterministic

## Scope
- Spellbook cleanup ordering and logging teardown

## Out of scope
- broader refactors outside Spellbook cleanup

## Files to touch
- src/melder/spellbook/spellbook.py
- tests/integration/melder/spellbook/test_spellbook_integration_logging.py

## Risks
- cleanup ordering change hides existing errors
- logger cleanup failures surface as new test noise

## Tests
- pytest tests/integration/melder/spellbook/test_spellbook_integration_logging.py

## Done criteria
- logger cleanup remains the final cleanup step
- logging integration tests pass consistently
```

Strategy alignment
- Path: `attention_board.md` (route active work item to the canonical ticket)
- Path: active ticket `## Notes` (store rationale, evidence, and next actions)

Tactics / runbook
- Path: `tickets/tasks/YYYY-MM-DD_interceptor_cleanup_task.md`
- Example content:

```md
# task: spellbook_cleanup_ordering
## Preconditions
- failing tests reproduced
- scope constrained to Spellbook cleanup ordering

## Steps
1) update Spellbook cleanup order
2) confirm logger cleanup remains last
3) run logging integration test
4) confirm idempotent cleanup under repeat runs
```

Work queue conversion
- When approved, convert the todo into a story/task ticket in `tickets/stories/` or `tickets/tasks/`.
- Example work items (summarized):
  - Task: adjust cleanup order
  - Task: harden detach restore logic



