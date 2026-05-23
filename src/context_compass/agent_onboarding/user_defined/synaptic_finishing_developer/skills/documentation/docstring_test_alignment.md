# docstring_test_alignment

Purpose
- Define how documentation claims and tests should reinforce each other.

Core rule
- If a docstring makes a meaningful claim, the test strategy should account for
  it.

Map docstring claims to test layers
- Args / Returns / Raises:
  - usually unit tests
- Lifecycle and cleanup:
  - unit tests first
  - component tests when cleanup crosses a real collaborator boundary
- Threading / locking / gating:
  - unit tests when isolated behavior is enough
  - component or integration tests when real coordination is the contract
- Cross-component side effects:
  - component tests first
  - integration tests when broader orchestration is required
- Regression notes or bug history:
  - dedicated regression tests

Alignment loop
1) Draft or revise the docstring.
2) Extract the meaningful guarantees.
3) Decide which guarantees need unit, component, or integration coverage.
4) Add or update tests until the strongest public claims are actually proven.
5) Reduce any docstring claims that the current test plan cannot support.

What this role should look for
- docstring says cleanup is idempotent:
  - add idempotent cleanup tests
- docstring says method is non-throwing after cleanup:
  - add post-cleanup tests
- docstring says registry write triggers publication/refresh:
  - add component or integration coverage
- docstring says method holds a lock or requires ordered mutation:
  - add tests around the visible consequence of that guarantee

Anti-patterns
- strong docstring claims with no matching tests
- rich tests that prove behavior the docstring never documents
- coverage-only tests that do not support the documented contract

References
- `agent_onboarding/user_defined/synaptic_finishing_developer/skills/testing/testing_overview.md`
- `agent_onboarding/user_defined/synaptic_finishing_developer/skills/testing/pytest_unit.md`
- `agent_onboarding/user_defined/synaptic_finishing_developer/skills/testing/component_tests.md`
- `agent_onboarding/user_defined/synaptic_finishing_developer/skills/testing/pytest_integration.md`
