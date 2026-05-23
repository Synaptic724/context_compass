# testing_overview

Purpose
- Define the finishing-role testing taxonomy and the depth bar for
  public-library contracts.

Testing stance
- We do not optimize for speed here.
- We optimize for:
  - contract coverage
  - lifecycle coverage
  - error-path coverage
  - cross-component behavior when the contract spans real collaborators

Primary test layers
- Unit:
  - default first move
  - direct contract behavior
  - error semantics
  - cleanup and state transitions
- Component:
  - small real wiring slices
  - preferred when a public contract depends on a few real collaborators
  - bridges the gap between isolated unit tests and broader integration tests
- Integration:
  - use when the boundary itself is the contract
  - use when concurrency/orchestration/serialization cannot be proved safely
    with unit or component tests

Finishing-role rule
- The test plan should be derived from the documented contract, not from a
  desire to "get coverage up."

What high-value tests look like
- they fail for a real regression
- they survive harmless refactors
- they prove a public or architectural contract
- they help keep docstrings honest

Depth expectations
- unit tests should cover:
  - returns
  - raises
  - invariants
  - cleanup
  - state transitions
- component tests should cover:
  - owner/borrower interactions
  - descriptor/publication/refresh boundaries
  - command/viewer/workstation or similar small real slices
- integration tests should cover:
  - real orchestration boundaries
  - real concurrency contracts
  - real multi-component runtime flows

Slow-finishing expectation
- For non-trivial surfaces, do not stop after one test pass.
- Revisit the contract after the first tests and ask:
  - what remains unproven?
  - what docstring claims are still too strong?
  - what layer needs one more slice?

Validation truthfulness
- Never imply tests ran if they did not.
- If not run, say `Not run.` exactly.
- Coverage numbers require actual measurement; do not guess.

References
- `agent_onboarding/user_defined/synaptic_finishing_developer/skills/documentation/docstring_test_alignment.md`
- `agent_onboarding/user_defined/synaptic_python_developer/skills/testing/testing_overview.md`
- `agent_onboarding/default/qa_engineer/skills/test_strategy_and_planning.md`
