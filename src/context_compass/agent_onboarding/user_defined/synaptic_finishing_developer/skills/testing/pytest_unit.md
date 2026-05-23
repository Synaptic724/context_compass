# pytest_unit

Purpose
- Define how this role writes unit tests for public-library contract work.

Unit-test mission
- Prove the direct contract of the class or method under test:
  - outputs
  - raises
  - invariants
  - lifecycle behavior
  - cleanup semantics

What unit tests should target first
- return values and visible state changes
- invalid inputs and error messages
- idempotent cleanup
- post-cleanup behavior
- state-transition legality
- public methods that enforce ownership or borrowing boundaries

When unit tests are enough
- when the behavior can be proved without real collaborator wiring
- when the contract is local and deterministic
- when mocking true external boundaries does not hide the real behavior

Unit-test rules
- Use pytest fixtures for setup and teardown.
- Prefer public APIs over private fields.
- Assert behavior, not incidental shape.
- Include error-path coverage when the docstring promises it.
- Prefer a few high-signal tests over a carpet of filler assertions.

Finishing-role emphasis
- If the docstring mentions:
  - cleanup ordering
  - non-throwing cleanup
  - fail-fast invalid state
  - explicit error remediation
  then the unit test suite should reflect that.

Bad unit tests
- attribute existence checks
- implementation-detail snapshots with no contract value
- “did not crash” assertions with no stronger claim

References
- `agent_onboarding/user_defined/synaptic_finishing_developer/skills/documentation/docstring_craft.md`
- `agent_onboarding/user_defined/synaptic_python_developer/skills/testing/pytest_unit.md`
