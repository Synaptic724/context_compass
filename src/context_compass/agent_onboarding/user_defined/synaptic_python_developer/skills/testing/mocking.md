

# mocking

Purpose
- Keep mocks stable and aligned with real boundaries.

Rules: Unit Tests First (Mock + Isolated)
* Mock external boundaries (I/O, filesystem, network, subprocesses, clocks, OS calls, databases, thread scheduling, random sources).
* Validate contracts (inputs/outputs/raises), invariants, and side effects (including cleanup ordering) at the smallest reasonable unit.
* Prefer contract-level assertions over implementation-detail assertions.

Test Mocks Skills
For reusable test-only classes and helpers, see `tests/mocks/`.

Rules
- Mock OS, filesystem, subprocess, network, and time.
- Avoid mocking internal logic or private fields.
- Do not over-specify call order unless it is part of the contract.
- Prefer asserting essential arguments and outcomes over full call sequences.

Good vs bad
- Good: assert a single boundary call with essential args.
- Bad: assert a long sequence of incidental internal calls.

Examples
- agent_onboarding/user_defined/synaptic_python_developer/examples/python/pytest_unit_examples.py




