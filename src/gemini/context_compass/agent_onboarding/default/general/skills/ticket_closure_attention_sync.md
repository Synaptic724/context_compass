

# ticket_closure_attention_sync

Purpose
- Enforce deterministic synchronization between ticket closure and `attention_board.md`.
- Prevent stale routing rows and historical note buildup on the pointer board.

When to use
- Any time a ticket is moved to `tickets/epics/completed/`, `tickets/stories/completed/`, or `tickets/tasks/completed/`.
- Any time a ticket status changes to done/review/blocked and the board row should change.

Deterministic closure sync protocol (mandatory)
1) Identify the closed ticket path (`old_ticket`) and completion datetime (`YYYY-MM-DDTHH:MM:SSZ`).
2) Open `context_compass/attention_board.md`.
3) In `## Active Items`:
   - If a row points to `old_ticket` and no immediate successor ticket exists, remove the row.
   - If a successor ticket exists, replace the row `ticket`, `status`, `mode`, `next`, `outcome`, `exit_signal`, and `updated_at` values.
4) In `## Active Attention Details`:
   - Remove entries whose `NEXT` or `EVIDENCE` are only about `old_ticket` and no longer route active work.
   - Keep the section focused on current active rows only.
   - Ensure the active row still has a matching `SWITCH_TRIGGER` and `RESUME_HIERARCHY`.
5) In `## Recently Closed Anchors`:
   - Add one compact anchor row for `old_ticket` with status `done` and `next=none`.
   - Keep at most 12 anchor rows; remove oldest rows first when adding a new one.
6) Verify board invariants before saving.
7) If the closed ticket has artifacts:
   - apply artifact disposition (`delete_on_close`, `retain_as_reference`, or
     `promote_to_documentation`),
   - update `context_compass/artifact_board.md` active/cleared rows.

Board invariants (must hold)
- `## Active Items` rows must only reference non-completed tickets.
- Every active row must map to one canonical ticket path.
- `next` text must be one concrete action.
- `outcome` and `exit_signal` must be concrete and non-empty for active rows.
- `## Active Attention Details` must only contain active-routing details.
- Active routing details must include `SWITCH_TRIGGER` and `RESUME_HIERARCHY`.
- Board must remain compact; durable narrative belongs in ticket `## Notes`.

Verification commands
- `rg -n "context_compass/(epics|stories|tasks)/completed/" context_compass/attention_board.md`
- `rg -n "## Active Items|## Active Attention Details|## Recently Closed Anchors" context_compass/attention_board.md`

Anti-patterns
- Leaving closed ticket rows in `## Active Items`.
- Keeping deep historical narratives in board detail section.
- Using board detail section as a duplicate of ticket notes.

References
- `context_compass/agent_onboarding/default/general/skills/workflow.md`
- `context_compass/agent_onboarding/default/general/skills/ticketing.md`
- `context_compass/agent_onboarding/default/general/skills/active_pointerboard.md`




