

# interfaces

Purpose
- Choose Protocol, ABC, or concrete types deliberately.

Rules
- Use truthful concrete types plus `typing.TYPE_CHECKING` imports by default
  when the dependency is typing-only.
- In Python 3.14, deferred annotations are already the default.
  That means the concrete type name should be used directly in annotations
  after a `TYPE_CHECKING` import, with no quotes and no `else: TypeName = Any`
  fallback alias.
- Use Protocol for structural typing only when multiple implementations are
  expected and the receiving code truly depends on a shared behavioral subset.
- Use ABC for shared behavior and explicit inheritance requirements.
- Use concrete types when there is a single stable implementation.
- For injected object collaborators, default to `TYPE_CHECKING` imports of the
  concrete runtime class unless a real shared structural contract is required.
- "Injected object collaborator" means an externally supplied object the
  receiver uses or stores but does not construct itself.
- Use the concrete type when the concrete runtime class is the true contract:
  concrete-only behavior, lifecycle/identity semantics, or intentionally
  concrete public APIs.
- Document the interface contract in the docstring, not just the type hints.
- Avoid widening types without a concrete compatibility reason.
- Interfaces may be exposed in public APIs when they mirror concrete classes.
  If exposed, the runtime object must be the concrete implementation and the
  interface contract must stay in lockstep with it.
- Prefer `typing.TYPE_CHECKING` over invented structural shims when the problem
  is only import visibility. Reach for interfaces only when the structure
  itself is the contract.
- Do not widen those truthful concrete types to `Any` just to break an import
  edge. If `Any` appears genuinely unavoidable, raise that conflict to the user
  instead of silently weakening the contract.

Example
- Protocol: "Supports .acquire() and .release()" without forcing inheritance.
- ABC: "BaseLogger" enforcing cleanup and level setting.

Examples
- agent_onboarding/user_defined/synaptic_python_developer/examples/python/protocols_and_abc.py




