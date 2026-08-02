

# architecture_contexts

Purpose
- Maintain C4/C3/C2/C1 architecture and component context for this repo.

Artifacts
- `system_docs/src_architecture.md`
- `system_docs/tests_architecture.md`
- `system_docs/src_components.md`
- `system_docs/tests_components.md`
- `agent_onboarding/default/engineer/skills/src_graph_usage.md`
- `system_docs/src_graph.md`
- `system_docs/src_graph_index.md`
- `system_docs/patches/active/<patch_id>/architecture_patch.md` (when patch lane is active)
- `system_docs/patches/active/<patch_id>/component_patch_<component>.md` (when patch lane is active)
- `system_docs/patches/active/<patch_id>/code_description_patch_<component>.md` (conditional)

Strict source rule
- Architecture and component docs must reflect the actual codebase and ticket context.
- If docs are stale, update them before relying on them for design decisions.

Update cadence
- Update docs when boundaries, lifecycle, invariants, or wiring change.
- Keep `src_graph.md` synchronized with canonical graph state when
  architecture/components work changes source wiring coverage.
- Keep ASCII and Mermaid diagrams current.
- Keep active patch docs synchronized with canonical docs until merge+cleanup closes the patch lane.

References
- `agent_onboarding/default/design_engineer/skills/src_architecture_instructions.md`
- `agent_onboarding/default/design_engineer/skills/src_components_instructions.md`
- `agent_onboarding/default/design_engineer/skills/tests_architecture_instructions.md`
- `agent_onboarding/default/design_engineer/skills/tests_components_instructions.md`
- `agent_onboarding/default/design_engineer/skills/patch_framework_design.md`
- `agent_onboarding/default/design_engineer/skills/architecture_patch_contracts.md`
- `agent_onboarding/default/design_engineer/skills/component_patch_contracts.md`
- `agent_onboarding/default/design_engineer/skills/code_description_patch_contracts.md`

