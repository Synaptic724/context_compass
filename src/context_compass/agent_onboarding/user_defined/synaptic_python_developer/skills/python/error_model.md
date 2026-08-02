

# error_model

Purpose
- Keep error behavior explicit and documented.

Rules
- Document raises in docstrings with conditions.
- Do not swallow exceptions silently.
- Use clear, stable exception types.
- Log error context when raising or translating errors.
- Error messages must be expressive and user-facing: what failed, why, and how to fix.
- This is a public repo, so raise messages must be safe and explanatory.
- Use high-quality contract error messages as a reference for detail and remediation.
- Avoid vague messages like "invalid input" without context.

Example
- Raises: ValueError when input violates invariants.
- Logging: ERROR with target path, reason, and remediation hint.

Examples
- agent_onboarding/user_defined/synaptic_python_developer/examples/python/docstrings.py





