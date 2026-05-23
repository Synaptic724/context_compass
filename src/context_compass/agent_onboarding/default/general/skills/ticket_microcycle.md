

# ticket_microcycle

Purpose
- Define a compact, repeatable execution loop that survives context loss.

Strict mode loop
1. `Investigate`
2. `Document` (immediate notes entry)
3. `Strategy/Plan`
4. `Document` (decision/plan note)
5. `Implement`
6. `Document` (implementation note)
7. `Validate`
8. `Document` (measure/result note)

Relaxed mode loop
- Use when strict mode is disabled by config.
- Still required:
  - Document each meaningful finding.
  - Document before implementation starts.
  - Document after validation.
- Unknown-first evidence rules remain unchanged.

Config source
- `config/context_compass_config.yaml`
- Keys:
  - `workflow.ticket_microcycle.enabled`
  - `workflow.ticket_microcycle.mode`
  - `workflow.ticket_microcycle.require_note_before_continue`
  - `workflow.ticket_microcycle.minimum_note_score`


