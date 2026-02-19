

# Tickets

Purpose
- User-facing index for ticket storage.
- Keep ticket lanes grouped in one root for easier navigation.

Structure
- `tickets/epics/`: active and backlog epic tickets.
- `tickets/stories/`: active and backlog story tickets.
- `tickets/tasks/`: active and backlog task tickets.
- `tickets/*/completed/`: completed tickets per lane.

Backlog locations
- `tickets/epics/backlog/`
- `tickets/stories/backlog/`
- `tickets/tasks/backlog/`

Notes
- Active routing still comes from `attention_board.md`.
- Durable execution memory still lives in each active ticket `## Notes`.


