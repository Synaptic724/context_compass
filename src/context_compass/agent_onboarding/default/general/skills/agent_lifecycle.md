

# agent_lifecycle

Purpose
- Define how session tracking and handoffs are handled in this repo.

Rules
- Track active routing in `attention_board.md` and detailed execution state in ticket notes/checklists.
- Use UNKNOWN as the default claim stance until evidence is recorded.
- Do not invent external lifecycle tooling or databases.
- On every onboarding or re-onboarding cycle, ask for `AGENT_NAME: <name>` as
  part of certification, then sync that assigned name into active workflow
  state when the active ticket or board row is touched.

Worklists
- Use `tickets/epics/`, `tickets/stories/`, and `tickets/tasks/` for active work.
- Move completed tickets to `tickets/epics/completed/`, `tickets/stories/completed/`, or
  `tickets/tasks/completed/` only after user confirmation.


