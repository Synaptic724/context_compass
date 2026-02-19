

# active_documentation

Purpose
- Keep durable, compaction-safe working memory directly inside active tickets.
- Ensure findings are captured with concrete evidence pointers while work is in
  flight.
- Prevent context loss by maintaining an always-current `## Notes` section.

Core rule
- Every active ticket (epic/story/task) must include a `## Notes` section.
- During active execution, append notes as meaningful findings happen; do not
  wait for end-of-pass summaries.
- Evidence pointers must include file paths with explicit start/end line ranges
  (`path:start_line-end_line`).
- UNKNOWN is the default claim state until evidence promotes a claim to FACT.
- Do not continue investigation to the next finding until the current finding
  is documented.
- Do not continue to code edits or validation until the current meaningful
  finding is documented in `## Notes` with evidence and next action.

Canonical storage
- Primary: `## Notes` in the active ticket being worked.
- Secondary: `attention_board.md` for routing state only.
- Do not move detailed findings into `attention_board.md`; keep detail in
  ticket notes.

Required note entry shape
For note entries:
- `DATETIME`: `YYYY-MM-DDTHH:MM:SSZ` (UTC)
- `TYPE`:
  `FACT` | `UNKNOWN` | `HYPOTHESIS` | `DECISION` | `DECISION_REQUEST` |
  `PLAN` | `STRATEGY_DISCUSSION` | `ASSUMPTION_CHALLENGE` | `CONFLICT` |
  `TRADEOFF` | `BLOCKER` | `ALIGNMENT_CHECK` | `MEASURE` | `RISK` |
  `RAISE`
- `CLAIM`: short technical finding.
- `EVIDENCE`: one or more `path:start_line-end_line` pointers.
- `IMPACT`: why this matters for current work.
- `NEXT`: one concrete next action.
- `REREAD`: `REQUIRED` | `HELPFUL`.
- `SCORE_0_TO_10`: must meet
  `workflow.ticket_microcycle.minimum_note_score`.
- `TYPE` semantics and conflict/strategy expectations are governed by:
  `context_compass/agent_onboarding/default/general/skills/execution_contract.md`.

Example
- `DATETIME`: 2026-02-14T00:00:00Z
- `TYPE`: FACT
- `CLAIM`: Conjure executes three scheduler lifecycles per run.
- `EVIDENCE`:
  - `src/melder/spellbook/spellbook_creation_system.py:637-637`
  - `src/melder/spellbook/spellbook_creation_system.py:743-743`
  - `src/melder/spellbook/spellbook_creation_system.py:757-757`
- `IMPACT`: Scheduler setup/teardown overhead compounds on startup.
- `NEXT`: Prototype a reduced scheduler lifecycle path behind existing contracts.

Update triggers (mandatory)
1) New verified finding.
2) New unknown/blocker.
3) Decision that changes scope or approach.
4) Measurement result (test/profile/benchmark).
5) Any meaningful finding that would be risky to lose on compaction.
6) Before handoff or compaction.

Quality bar
- Keep notes append-only unless correcting a factual error.
- Prefer high-signal claims with precise evidence over long narrative.
- If a finding is single-line evidence, still write a range with same start/end.
- Mark unverified items as `UNKNOWN`; never promote to fact without evidence.
- Never store secrets in notes.
- No implementation from `UNKNOWN` or `HYPOTHESIS` notes without evidence-backed promotion to `FACT` or `DECISION`.

References
- `agent_onboarding/default/general/skills/reactive_documentation.md`
- `agent_onboarding/default/general/skills/active_pointerboard.md`
- `agent_onboarding/default/general/skills/ticketing.md`
- `workflow.md`





