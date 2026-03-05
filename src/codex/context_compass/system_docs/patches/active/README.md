# Active Patch Lane

Purpose
- Hold temporary patch artifacts for the current implementation lane.
- Keep patch docs separate from canonical `system_docs/src_*` docs until merge.

Usage
1) Copy `_template_patch_id/` to a new patch folder:
   - `system_docs/patches/active/<patch_id>/`
2) Fill in:
   - `architecture_patch.md`
   - `component_patch_<component>.md` (one per changed component)
   - `code_description_patch_<component>.md` (conditional)
3) Link artifacts in active ticket `Artifact Links`.
4) Validate artifacts with:
   - `python context_compass/scripts/validate_patch_gate.py --patch-id <patch_id> --components <component_a> <component_b>`
5) On closure:
   - merge durable deltas into canonical docs,
   - remove temporary patch folder unless explicit retention is approved.

Notes
- Patch artifacts are temporary by default.
- Ticket state remains the canonical execution tracker.
