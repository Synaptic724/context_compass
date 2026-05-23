

# engineer_quality_policy

Purpose
- Establish the quality bar for engineer changes.

Policy
- Every touched function/class must have a rich docstring aligned with the behavior.
- Tests must be added or updated for behavioral changes.
- Avoid drive-by refactors; limit edits to the requested scope.
- If a class implements cleanup, assume it is not used after cleanup completes.
- Default cleanup posture for owned references is delete/remove the live field
  surface; retain `None` only when the contract explicitly needs a post-cleanup
  tombstone field.
- Prefer `check_cleaned()` fail-fast behavior when the contract requires active state.
- Use `if self._cleaned: return` only when non-throwing behavior is explicit contract.
- Do not add `None` guards on internally owned fields unless optionality is proven.
Unknowns Gate
- Apply the canonical policy in
  `agent_onboarding/default/general/skills/unknowns_gate_reference.md`.
- UNKNOWN is still the default for unevidenced claims in engineer quality reviews.
- Quality findings must cite concrete file/symbol evidence or remain UNKNOWN.
- Do not treat failing tests, naming patterns, or historical assumptions as
  contract evidence without direct source verification.

Exceptions
- Only allowed with explicit user approval, documented in the response.

References
- `AGENTS.MD`
- `agent_onboarding/default/general/skills/unknowns_gate_reference.md`

