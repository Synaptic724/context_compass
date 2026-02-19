# task: spellbook_cleanup_ordering

## Goal
Keep logger cleanup as the final teardown step in Spellbook lifecycle.

## Scope
- cleanup ordering in core teardown path
- regression test for teardown ordering

## Acceptance Criteria
- logger cleanup executes after child cleanup
- regression test protects ordering contract

## Notes
- 2026-02-19T00:00:00Z | FACT | current ordering executes logger cleanup early
- 2026-02-19T00:05:00Z | PLAN | move logger teardown to final step and validate