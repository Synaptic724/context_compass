# docstring_craft

Purpose
- Define how this role writes public-library docstrings that are rich,
  system-aware, and worth rereading later.

Finishing stance
- A good docstring is not a local summary.
- It explains why the symbol exists, what it guarantees, what it owns, what it
  borrows, and how it behaves inside the wider system.

Mandatory pre-write loop
1) Identify the symbol's system role:
   - which subsystem it belongs to
   - what layer it sits in
   - what other objects depend on it
2) Identify its contract:
   - invariants
   - valid inputs
   - outputs
   - raises
   - side effects
3) Identify its operational context:
   - threading/locks/gates
   - lifecycle/cleanup ordering
   - registration/publication impacts
4) Identify what tests should prove those claims.

Required public-library sections
- Purpose:
  - what it does
  - why it exists
- System Role:
  - where it sits in the architecture/components graph
  - what it collaborates with
- Contract:
  - invariants and guarantees
  - what is stable for callers
- Args / Returns / Raises:
  - explicit and precise
- Threading / Concurrency:
  - locks, gates, ordering, reentrancy, or why none apply
- Lifecycle / Cleanup:
  - ownership
  - teardown ordering
  - idempotence expectations
- Side Effects / State Impact:
  - registry mutation
  - descriptor/publication changes
  - dirty-state or validation effects

When to go deeper
- Use richer narrative when the symbol:
  - coordinates multiple collaborators
  - mutates shared system state
  - participates in cleanup/lifecycle
  - gates validation or concurrency
  - sits on a public surface that future readers will rely on

Non-negotiables
- Do not write one-liner public docstrings for non-trivial code.
- Do not describe only mechanics if the system role matters.
- Do not promise guarantees the tests and source do not support.
- Do not ignore cleanup or concurrency when they are part of the contract.

Docstring quality ladder
- Gold:
  - purpose, system role, contract, lifecycle, threading, failure semantics,
    and testable guarantees
- Strong:
  - complete contract sections with less system narrative
- Adequate:
  - basic args/returns/raises but missing deeper system or lifecycle detail
- Weak:
  - only local mechanics, little contract value

Review questions
- Could a new engineer understand why this symbol matters in the system?
- Could a tester derive a meaningful test plan from the docstring?
- Would a harmless refactor keep this docstring true?

References
- `system_docs/src_architecture.md`
- `system_docs/src_components.md`
- `system_docs/src_graph.md`
- `agent_onboarding/user_defined/synaptic_python_developer/skills/python/docstrings.md`
