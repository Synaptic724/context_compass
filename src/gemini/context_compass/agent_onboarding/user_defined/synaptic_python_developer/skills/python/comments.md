

# comments

Purpose
- Preserve and improve comments as part of the API contract.

Prime Directive: Documentation-First Edits
Whenever you add or modify code:
* Every class must have a rich docstring.
* Every method/function must have a rich docstring.
* Comments must be preserved and improved when they are unclear or insufficient.
* Treat docstrings + comments as part of the API: they must remain accurate.

Non-Negotiables
* Preserve Documentation and Comments
* Never delete or strip docstrings.
* Never delete comments. If a comment is wrong, stale, or misleading, update it rather than removing it.
* Only rewrite docstrings/comments for code you touched unless an untouched doc/comment is provably wrong or dangerously misleading.

Rules
- Never delete comments; update them if stale or wrong.
- Add comments only to clarify non-obvious logic.
- Add moderate, targeted comments for future readers when intent or invariants are not obvious.
- Avoid narrative or redundant comments.
- Keep comments aligned with docstrings and invariants.
- If a comment conflicts with behavior, fix the comment and the code together.

Good vs bad
- Good: "# Guard against re-entrancy during cleanup."
- Bad: "# Set x to 1." when the code is self-explanatory.

Examples
- agent_onboarding/user_defined/synaptic_python_developer/examples/python/anti_patterns.py





