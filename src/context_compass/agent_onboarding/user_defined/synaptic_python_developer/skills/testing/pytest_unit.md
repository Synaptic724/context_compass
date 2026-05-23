

# pytest_unit

Purpose
- Establish unit test expectations for python code.

Rules: Unit Tests First (Mock + Isolated)
The default approach is mocked / isolated unit tests.

* Mock external boundaries (I/O, filesystem, network, subprocesses, clocks, OS calls, databases, thread scheduling, random sources).
* Validate contracts (inputs/outputs/raises), invariants, and side effects (including cleanup ordering) at the smallest reasonable unit.
* Prefer contract-level assertions over implementation-detail assertions.
* Avoid flakiness: tests must run reliably on repeated runs.

Contract-level assertion checklist
When writing a unit test, you should be able to answer "yes" to most of these:
* Does the test assert an observable outcome (return, raise, snapshot, state transition)?
* Would the test fail if a real regression happened?
* Would the test still pass after a harmless refactor (renaming locals, reordering statements, changing internal data structures)?
* Are mocks only used at true boundaries?
* Are we asserting behavior rather than "internal shape"?
If not, the test is probably Rank E/F.

Rules
- Use fixtures for setup/teardown and dependency injection.
- Mock only true boundaries (filesystem, OS, network, time).
- Assert public behavior and contract outcomes.
- Prefer contract-level assertions over private fields.
- Include error-path coverage when documented in docstrings.

Example assertions
- Return values match documented contract.
- Raises ValueError on invalid input.
- Cleanup is idempotent.

Examples
- agent_onboarding/user_defined/synaptic_python_developer/examples/python/pytest_unit_examples.py




