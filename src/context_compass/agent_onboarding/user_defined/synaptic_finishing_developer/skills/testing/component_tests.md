# component_tests

Purpose
- Define component tests as a first-class layer between unit and integration
  testing for finishing work.

Component-test definition
- A component test uses a small real slice of collaborators to prove a
  meaningful boundary without dragging in the whole system.

Use component tests when
- a public contract depends on a few real collaborators
- a docstring describes behavior across a local boundary
- ownership, publication, refresh, or registry behavior is real but bounded
- unit mocks would re-implement the system instead of testing it

Examples of good component-test targets
- descriptor manager + published record behavior
- viewer/command/workstation interaction in one room slice
- cleanup cascade across one parent and its owned children
- ACL compile/validate behavior across a small real bundle

Component-test rules
- Keep the slice small and intentional.
- Use real collaborators where that materially increases signal.
- Do not pull in the whole runtime when a smaller slice proves the contract.
- Keep setup explicit and deterministic.
- Prefer clear boundary assertions over broad snapshot dumps.

Placement
- component tests belong in `tests/component/`

How component tests support docstrings
- They prove "this object coordinates X with Y" claims.
- They prove publication or refresh side effects.
- They prove ownership boundaries where multiple real objects interact.

Anti-patterns
- component tests that are really oversized integration tests
- component tests that still mock every meaningful collaborator
- component tests that assert a giant object dump instead of boundary behavior

References
- `agent_onboarding/default/qa_engineer/skills/test_strategy_and_planning.md`
- `agent_onboarding/user_defined/synaptic_python_developer/skills/testing/testing_overview.md`
