

# context_compass

Purpose
- Central control plane for planning, execution memory, and architecture context.
- Durable work state is ticket-first; board is routing-only.
- Supports both software-engineering and fiction-authoring role workflows.

Core operating model
- Active work lives in `tickets/epics/`, `tickets/stories/`, and `tickets/tasks/`.
- Parked backlog tickets live in `tickets/epics/backlog/`, `tickets/stories/backlog/`, and
  `tickets/tasks/backlog/`.
- Detailed state belongs in active ticket `## Notes` with evidence ranges.
- `attention_board.md` routes to the active ticket and next action only.
- `artifact_board.md` indexes ticket-linked artifacts when artifacts exist.
- Closed work moves to matching `*/completed/` folders.

Primary docs
- `AGENTS.MD`: repository operating contract.
- `SKILLS.MD`: onboarding/profile routing contract.
- `agent_onboarding/default/general/skills/workflow.md`: ticket lifecycle and closure rules.
- `agent_onboarding/default/general/skills/ticket_microcycle.md`: strict/relaxed ticket microcycle definition.
- `agent_onboarding/default/general/skills/context_compaction.md`: compaction/handoff policy.
- `agent_onboarding/`: onboarding policy modules.
- `system_docs/`: canonical docs:
  `src_architecture.md`, `src_components.md`,
  `tests_architecture.md`, and `tests_components.md`.
- `artifact_board.md`: artifact association index.
- `artifacts/`: ticket-linked supporting artifacts.
- `agent_onboarding/default/general/skills/configuration_standards.md`: canonical documentation formatting contract.

Policy anchors
- Unknowns gate: `agent_onboarding/default/general/skills/unknowns_gate_reference.md`.
- Certification gate (`CERTIFY: APPROVED`): `AGENTS.MD` and
  `agent_onboarding/default/general/skills/self_certification.md`.

Packaging model
- `agent_onboarding/`:
  - Default profile baselines and user-defined overlays.
- `SKILLS.MD`:
  - Active role routing and role-selection directive.
- `agent_onboarding/*/SKILLS.MD`:
  - Per-role active-skill lists and inheritance chaining.
- `config/context_compass_config.yaml`:
  - Ticket microcycle, documentation-format values, and read-window limits.
  - `codex.viewer_tool_read_limit` and `codex.read_loc_max` are line-count
    settings (default `500` each).

Completed Archive
- 2026-01-17 - Melder DI resolution contract docs (see `completed/2026-01-17_melder_di_resolution_contract_docs_task_completed.md`).
- 2026-01-17 - Melder DI contract decision alignment (see `completed/2026-01-17_melder_di_contract_decisions_doc_alignment_task_completed.md`).
- 2026-01-17 - Melder scan bind module work (see `completed/2026-01-17_melder_scan_bind_module_task_completed.md`).
- 2026-01-18 - Melder src architecture doc (see `completed/2026-01-18_melder_src_architecture_doc_task_completed.md`).
- 2026-01-18 - Melder src components doc (see `completed/2026-01-18_melder_src_components_doc_task_completed.md`).






