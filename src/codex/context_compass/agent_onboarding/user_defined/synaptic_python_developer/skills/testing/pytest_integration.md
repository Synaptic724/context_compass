

# pytest_integration

Purpose
- Define when integration tests are required.

Integration tests are required when behavior cannot be proven safely via mocks/unit tests.

Use integration tests when at least one is true:
* Correctness depends on real interactions across multiple components (e.g., concurrency scheduling, orchestration behavior, serializer/codec correctness across layers).
* Mocking would require re-implementing the system under test or would make the test meaningless.
* The integration is the contract (e.g., plugin wiring, adapter boundaries, real concurrency primitives).

Rules for integration tests:
* Keep them scoped: integrate only the minimal set of real components needed.
* Make them explicit: use clear naming and markers (e.g., @pytest.mark.integration) if the repo uses them.
* Ensure they remain repeatable and not environment-dependent unless explicitly documented.

Rules
- Use integration tests only when unit tests cannot prove correctness.
- Prefer component tests first when a small slice of real wiring is enough.
- Keep integration scopes minimal and explicit.
- Mark integration tests clearly if the repo uses markers.
- Avoid flaky environment dependencies unless explicitly required.

Example uses
- Concurrency behavior across multiple components.
- Real serializer or adapter behavior across layers.

Examples
- agent_onboarding/user_defined/synaptic_python_developer/examples/python/pytest_integration_examples.py




