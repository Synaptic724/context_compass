# Example: ADR

Decision
- Keep runtime entrypoint policy separate from role routing policy.

Options considered
- Merge all policy into one file.
- Keep layered policy documents.

Outcome
- Keep layered documents for deterministic re-onboarding and maintainability.
