

# docstrings

Purpose
- Ensure docstrings are contract-first, not descriptive fluff.

Prime Directive: Documentation-First Edits
Whenever you add or modify code:
* Every class must have a rich docstring.
* Every method/function must have a rich docstring.
* Comments must be preserved and improved when they are unclear or insufficient.
* Treat docstrings + comments as part of the API: they must remain accurate.

Non-Negotiables
Rich Docstrings Required (No Fluff)
This is not optional. For all public classes and public methods, write docstrings that include real contracts, not vibes.

Docstring style: follow the repo's existing style (Google / NumPy / reST). If the repo has a pattern, match it exactly.

Minimum content for public API:
* Purpose: what it does and why it exists.
* Contract: invariants / guarantees / side effects.
* Parameters: meaning + constraints.
* Returns: what is returned (or None).
* Raises: what can be raised, and under what conditions.
* Threading / Concurrency: locks, thread-safety, reentrancy, ordering (when relevant).
* Lifecycle / Cleanup: ownership, idempotence, teardown ordering (when relevant).
* Examples: only when it materially clarifies usage; keep short.
* Typing: Always add typehints to signatures, and document complex types in the docstring if needed for clarity.

No fluff rule: do not write marketing copy or filler sentences. If a docstring is "rich," it's because it contains precise guarantees.

Rules
- Every public class and function must have a rich docstring.
- Docstrings must be rich and expressive; this is a public repository.
- Match the repo's prevailing docstring style (Google/NumPy/reST).
- Include purpose, contract, parameters, returns, raises, threading, and lifecycle when relevant.
- Keep language precise, stable, and testable.
- Document ownership and cleanup responsibilities when the code manages resources.

Docstring rank ladder (highest to lowest)
- Rank 5 (Gold): full contract narrative like `normalize_names` in `agent_onboarding/user_defined/synaptic_python_developer/examples/python/docstrings.py`.
  Includes purpose, responsibilities, invariants, workflows, args/returns/raises, and clear
  failure modes with remediation guidance.
- Rank 4 (Strong): complete args/returns/raises with invariants and side effects, but less
  narrative or fewer workflow details.
- Rank 3 (Adequate): purpose + args/returns/raises, but missing invariants or error semantics.
- Rank 2 (Weak): short description with partial args/returns and vague error handling.
- Rank 1 (Thin): minimal one-liner with no contract detail.
- Rank 0 (Garbage): no docstring.

Comment discipline
- Comments must explain non-obvious logic and uphold the contract; they are part of the API.
- Add moderate, targeted comments for future readers when behavior is not obvious from code + docstring alone.

Template snippet
```
"""
Purpose: One sentence on what this does and why.

Contract:
  - Invariants and guarantees.
  - Side effects and ordering constraints.

Args:
  x (Type): Meaning and constraints.

Returns:
  Type: What is returned.

Raises:
  ValueError: When inputs violate invariants.
"""
```

Good vs bad
- Good: "Returns a validated FooModel; never mutates inputs."
- Bad: "Does stuff with foo."

Examples
- agent_onboarding/user_defined/synaptic_python_developer/examples/python/docstrings.py








