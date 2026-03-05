# patch_artifact_consumption

Purpose
- Define how `engineer` consumes patch artifacts before and during
  implementation.
- Make architecture/component/code-description patches executable inputs rather
  than optional background context.

Scope
- Applies when `patch_framework_gating.md` is triggered for system-impacting
  work.
- Covers consumption behavior only (authoring belongs to `design_engineer`).

Required read order (non-negotiable)
1) `system_docs/patches/active/<patch_id>/architecture_patch.md`
2) `system_docs/patches/active/<patch_id>/component_patch_<component>.md`
   for each changed component
3) `system_docs/patches/active/<patch_id>/code_description_patch_<component>.md`
   when present or required by trigger rules

Consumption contract
- Extract from `architecture_patch.md`:
  - boundary/interface deltas,
  - cross-component invariants,
  - migration order,
  - rollback constraints.
- Extract from each `component_patch_<component>.md`:
  - before/after behavior,
  - state/failure deltas,
  - validation expectations,
  - dependency ordering.
- Extract from each `code_description_patch_<component>.md`:
  - control flow commitments,
  - edge/error semantics,
  - idempotency expectations,
  - explicit non-goals.

Implementation mapping rule
- Before code edits, write a concise ticket-note mapping:
  - patch section -> implementation step -> validation step.
- If mapping cannot be produced from available artifacts, raise `BLOCKER`.

Mandatory stop conditions
- Missing required patch artifact.
- Patch docs conflict with each other.
- Patch docs conflict with canonical architecture/component docs and no accepted
  override note exists.
- Patch unknowns are unresolved for the target code path.

During implementation
- Keep edits within patch-defined boundaries.
- If scope expands, update patch docs and ticket links first.
- Do not silently "fix forward" patch-contract conflicts in code.

Before closure
- Verify implemented behavior matches patch contracts.
- Record validation evidence against patch expectations.
- Complete merge-and-cleanup gates from `patch_framework_gating.md`.

Validation command (recommended)
- `python context_compass/scripts/validate_patch_gate.py --patch-id <patch_id> --components <component_a> <component_b>`
- Include `--ticket <ticket_path>` when verifying artifact links are present.

References
- `agent_onboarding/default/engineer/skills/patch_framework_gating.md`
- `agent_onboarding/default/engineer/skills/engineer_execution.md`
- `agent_onboarding/default/general/skills/workflow.md`
- `context_compass/scripts/validate_patch_gate.py`
