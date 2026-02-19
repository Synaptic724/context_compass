

# interfaces

Purpose
- Choose Protocol, ABC, or concrete types deliberately.

Rules
- Use Protocol for structural typing when multiple implementations are expected.
- Use ABC for shared behavior and explicit inheritance requirements.
- Use concrete types when there is a single stable implementation.
- Document the interface contract in the docstring, not just the type hints.
- Avoid widening types without a concrete compatibility reason.
- Interfaces may be exposed in public APIs when they mirror concrete classes.
  If exposed, the runtime object must be the concrete implementation and the
  interface contract must stay in lockstep with it.
- Prefer interfaces over typing.TYPE_CHECKING patterns for dependency
  boundaries; avoid guarded import hacks.

Example
- Protocol: "Supports .acquire() and .release()" without forcing inheritance.
- ABC: "BaseLogger" enforcing cleanup and level setting.

Examples
- agent_onboarding/user_defined/synaptic_python_developer/examples/python/protocols_and_abc.py





