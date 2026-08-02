

# context_protocol

Purpose
- Make architecture/components docs and tickets the primary source of truth.
- Treat code as a last resort after documented context is consulted.

When to use
- Before any code edits, investigations, or architectural changes.

Required flow
- For architecture/components/tests claims, read the relevant `system_docs/*`
  files first.
- When the question is about object wiring, ownership, creation, publication,
  validation, or borrowing relationships, include:
  - `context_compass/agent_onboarding/default/engineer/skills/src_graph_usage.md`
  - `context_compass/system_docs/src_graph.md`
  - `context_compass/system_docs/src_graph_index.md` when storage-level graph
    verification or regeneration mechanics are required
- For system-impacting changes, apply the mandatory gate in
  `agent_onboarding/default/engineer/skills/patch_framework_gating.md` before
  implementation.
- For patch-lane work, follow
  `agent_onboarding/default/engineer/skills/patch_artifact_consumption.md`
  before code edits.
- Review `attention_board.md` first, then open the linked active ticket(s) for current intent.
- Open code only when docs are insufficient or stale.
- If docs are stale, update them before proceeding with feature work.

Rules
- Always prefer documented context over assumptions.
- Treat UNKNOWN as default until evidence is attached.
- Keep architecture/components docs in sync with actual boundaries.
- Treat `src_graph.md` as the primary graph consumption surface when
  architecture/components context is required.
- Block implementation when patch-framework entry-gate artifacts are missing for
  system-impacting work.
- If a doc is missing, create it before implementing related changes.

Examples
- `agent_onboarding/default/general/README.md`

