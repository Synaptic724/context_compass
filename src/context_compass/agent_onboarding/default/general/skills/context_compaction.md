

# Context Compaction Policy

## Purpose
Ensure continuity and minimize lost context when a session is compacted or handed off.

## External Memory Priority
- Repository artifacts are the source of truth for durable context.
- `attention_board.md` is the canonical active-attention state and is mandatory
  during active work.
- Compaction summaries MUST be empty when the runtime/platform allows empty summaries.
- If empty summaries are not allowed, write only minimal pointer summaries:
  - high-level outcomes (no narrative replay)
  - policy anchor paths that MUST be re-read
  - active ticket path(s)
  - changed file path(s)
  - next immediate action

## Required Review Set

Core review set (ALWAYS required) - review these files in order:
- `AGENTS.MD`
- `agent_onboarding/default/general/skills/execution_contract.md`
- `config/context_compass_config.yaml`
- `context_compass/SKILLS.MD`
- resolved role `SKILLS.MD` chain (parent-first; the SKILLS files themselves)
- `agent_onboarding/default/general/skills/compaction_requirements.md`
- `agent_onboarding/default/general/skills/workflow.md`
- `attention_board.md`
- Active epic/story/task tickets in `tickets/epics/`, `tickets/stories/`, `tickets/tasks/`

Conditional review set (ONLY when triggered):
- `artifact_board.md` (when active tickets include artifacts or artifact disposition changes)
- `artifacts/README.md` (when artifact lifecycle protocol is active)
- System-context / architecture docs are **ON-DEMAND** and MUST be reviewed only when:
  - the active ticket requires architecture/components/tests documentation work, OR
  - this session modified `system_docs/*`, OR
  - the handoff requires making architecture claims in the next step.
  If triggered, review:
  - `agent_onboarding/default/design_engineer/skills/src_architecture_instructions.md`
  - `agent_onboarding/default/design_engineer/skills/tests_architecture_instructions.md`
  - `agent_onboarding/default/design_engineer/skills/src_components_instructions.md`
  - `agent_onboarding/default/design_engineer/skills/tests_components_instructions.md`
  - `system_docs/src_architecture.md`
  - `system_docs/tests_architecture.md`
  - `system_docs/src_components.md`
  - `system_docs/tests_components.md`
  - `agent_onboarding/default/engineer/skills/src_graph_usage.md`
  - `system_docs/src_graph.md`

Read discipline (non-negotiable)
- Review-set document reads must be manual per file path.
- Loop-based/batch document-reading commands are forbidden (for/foreach/while
  loops, xargs-style runners, or piped file-list iterators).
- For files over 500 LOC, read in explicit 500-line chunks in sequential order.

## Required Updates
- Update `attention_board.md` during work so active items, status, blockers, and
  next actions stay current.
- Before compaction/handoff, verify `attention_board.md` is current and matches
  active ticket status.
- Update the `## Notes` section of all active tickets with latest findings and
  `path:start_line-end_line` evidence pointers (use `start=end` for single-line evidence).
- Ensure each meaningful finding was written as a note before the next investigation tranche.
- Ensure UNKNOWN-first discipline was followed (unverified claims remain `UNKNOWN`).
- Ensure note entries carry re-entry metadata when required by the ticket contract.
- Capture open questions, decisions, and next steps in the relevant ticket.
- Ensure status fields and checkboxes are accurate.
- Ensure tickets carry enough state so compaction summaries can stay empty or minimal.
- If artifacts exist: keep ticket `Artifact Links` sections and `artifact_board.md` synchronized.

## Handoff Summary Checklist
- Current state and progress (what is done vs remaining).
- Key decisions and rationale.
- Known risks and active blockers.
- Immediate next steps (1-3 concrete actions).
- References to any critical files or paths.

## Post-Compaction Verification
After compaction, re-open the core review set and confirm:
- `agent_onboarding/default/general/skills/compaction_requirements.md` has been re-applied before any action.
- A `REONBOARD: COMPLETE` attestation (with read-integrity proof) was posted before any action.
- `attention_board.md` was re-opened and still matches active ticket state.
- If artifacts are active: `artifact_board.md` was re-opened and is consistent with tickets.
- The active tickets still represent the correct plan.
- The next steps are unambiguous.
- Re-onboarding document reads were performed manually per file path (no loop-based/batch reads).

