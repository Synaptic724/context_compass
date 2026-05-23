# pytest_integration

Purpose
- Define when this role should escalate from unit/component tests to
  integration tests.

Use integration tests when
- the real boundary is multi-component orchestration
- concurrency or gating behavior depends on real interaction
- serializer, adapter, or runtime wiring behavior is itself the contract
- unit or component tests would become fake by mocking too much

Integration-test rules
- Keep scope minimal but real.
- Use the smallest real set of components that proves the contract.
- Make the boundary under test explicit in the test name and setup.
- Avoid environmental flakiness unless the environment is part of the contract.
- Mark integration tests clearly if the repo uses markers.

Finishing-role emphasis
- Reach for integration tests when the docstring or system docs describe a
  runtime flow that spans multiple owned/borrowed boundaries and a component
  slice is not enough.

Examples
- real revalidation flow across spell/system state and change control
- real room command -> codegen engine -> memory/event emission flow
- real refresh/gate coordination when that is the contract under discussion

References
- `agent_onboarding/user_defined/synaptic_python_developer/skills/testing/pytest_integration.md`
- `agent_onboarding/default/qa_engineer/skills/regression_and_release_quality.md`
