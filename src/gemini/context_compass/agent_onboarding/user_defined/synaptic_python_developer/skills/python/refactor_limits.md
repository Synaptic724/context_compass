

# refactor_limits

Purpose
- Keep changes scoped and reviewable.

No Drive-By Refactors
* Do not refactor unrelated code.
* Do not rename symbols unless explicitly requested.
* Do not reorder code for aesthetics.
* Do not reformat files beyond what is required for the change.

Reviewability and Change Hygiene
* Keep changes reviewable.
* Avoid touching large numbers of files in one change unless explicitly requested.
* When a large change is required, group it by a clear boundary (module/dir) and apply a consistent rule.

Mechanical Sweeps (Repo-Wide Imports / Class Vars / Headers)
For repo-wide mechanical edits (e.g., "add this import everywhere", "add a class variable to every class"):
* Prefer generating a deterministic codemod script (or equivalent automated edit) rather than manually editing N files.
* The codemod must be safe, predictable, and reviewable.
* The goal is to avoid partial application, missed files, and "creative" edits.

Public API Guardrail
* Do not change public API shape or semantics unless explicitly requested.
* If a public change is unavoidable, prefer:
  * compatibility adapters/shims, and/or
  * explicit deprecation paths with documentation.

Rules
- No drive-by refactors.
- No renames or reordering for aesthetics.
- Group large changes by clear module boundaries.
- Use codemods for mechanical repo-wide edits.
- Ask before touching many files or changing public API shape.
- Preserve existing formatting unless required by the change.

Examples
- agent_onboarding/user_defined/synaptic_python_developer/examples/python/anti_patterns.py




