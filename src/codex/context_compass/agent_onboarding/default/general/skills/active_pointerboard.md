

# active_pointerboard

Purpose
- Keep a single, compact routing view of active work.
- Make post-compaction re-entry fast without replacing ticket detail.
- Prevent "what am I working on?" ambiguity.

Canonical board path
- `context_compass/attention_board.md`

Scope
- Pointer data only.
- No deep analysis, no full history replay, no speculative claims.
- Detailed context remains in ticket files.
- Artifact pointers belong in ticket `Artifact Links` and `artifact_board.md`,
  not in `attention_board.md`.

Required columns
- `work_item`: short active event label.
- `status`: `ready` | `in_progress` | `blocked` | `review`.
- `mode`: `discovery` | `implementation` | `validation` | `handoff`.
- `owner`: current executor (for now usually `codex`).
- `blocker`: concrete blocker or `none`.
- `next`: one concrete next action.
- `outcome`: intended near-term result for this active item.
- `exit_signal`: explicit condition that indicates the row should route/switch.
- `ticket`: canonical context-compass-relative ticket path (no `context_compass/` prefix).
- `updated_at`: ISO-8601 UTC (`YYYY-MM-DDTHH:MM:SSZ`).
- `reread`: `REQUIRED` | `HELPFUL`.

Update triggers (mandatory)
1) When a work item changes status.
2) When mode/outcome/exit_signal changes.
3) When blocker state changes.
4) Before compaction/handoff.
5) Immediately after re-onboarding if board is stale.
6) When switch conditions become true and routing must change.

Operating rules
- Pointer board never overrides ticket truth.
- Every row must map to exactly one canonical ticket path.
- Keep row text short and operational.
- If a claim is uncertain, mark it in the ticket `Unknowns`, not on this board.
- Execution is blocked when active work has no matching board row; repair board routing before continuing implementation or validation.

Re-entry protocol
1) Open `context_compass/attention_board.md`.
2) Read rows with `reread=REQUIRED`.
3) Read `SWITCH_TRIGGER` and `RESUME_HIERARCHY` in active attention details.
4) Open linked ticket(s) and resume from `next`.

Ticket closure sync protocol (mandatory)
1) When a ticket is moved to a completed folder, update board rows in the same change pass.
2) Remove/replace any `## Active Items` row referencing the closed ticket.
3) Prune `## Active Attention Details` entries tied only to the closed ticket.
4) Add one compact row to `## Recently Closed Anchors` for traceability.
5) Keep anchors capped to 12 rows (drop oldest first).
6) Keep active rows free of completed-ticket paths.

Anti-patterns
- Using board as a second ticket system.
- Copying long narrative into rows.
- Leaving stale `in_progress` rows after handoff.
- Tracking artifact file paths in attention-board rows/details.

References
- `context_compass/agent_onboarding/default/general/skills/workflow.md`
- `context_compass/SKILLS.MD`
- `context_compass/agent_onboarding/default/general/skills/memory_management.md`
- `context_compass/agent_onboarding/default/general/skills/reactive_documentation.md`
- `context_compass/agent_onboarding/default/general/skills/active_documentation.md`
- `context_compass/agent_onboarding/default/general/skills/ticket_closure_attention_sync.md`





