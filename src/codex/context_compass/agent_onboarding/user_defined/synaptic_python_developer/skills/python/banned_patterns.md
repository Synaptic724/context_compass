

# banned_patterns

Purpose
- Prevent unsafe or non-auditable behavior.

Attribute Access Rule (No Defensive Introspection in Owned Code)
If we own the file/module and the attribute names are visible in the code, do NOT use getattr() / hasattr() as a defensive pattern.

* Use direct access (obj.attr).
* Handle None explicitly where appropriate.
* If you genuinely need to handle a missing attribute on an external/optional dependency, call it directly and catch AttributeError instead of probing with hasattr. This keeps owned-code contracts strict while still being safe when the contract is ambiguous or external.

getattr() / hasattr() are allowed only in ambiguous situations, meaning at least one is true:
* The object is polymorphic/external and its attribute contract is not visible in our code.
* The attribute/method is optional by design (capability checks).
* The attribute name is truly dynamic.

Polymorphic lock cleanup exception (allowed):
* For lock-like objects that may be different implementations, capability checks are allowed:
  if hasattr(lock, "cleanup"): lock.cleanup()

Disallowed example (we own it / visible contract):
* getattr(self, "_foo", None) when _foo is clearly part of our class/object contract in this file.

Defensive local alias for nullable owned dependency (banned)
If a dependency is part of the owned class contract, do not treat it as optional at access time.
Do not create a local alias just to guard a potentially None owned dependency.
Guarantee initialization through the lifecycle and use direct self references.
Do not silently return defaults in hot path accessors.

Snapshotting owned structures for reads (banned)
Do not snapshot owned registries/maps/lists into locals or copies for read access.
Use the live structure directly when it is part of the owned contract.
Snapshotting is allowed only when required for correctness (for example, iterating
while mutation is expected or when a defensive copy is explicitly mandated by the
method contract). When snapshotting is required, document the reason in the
method docstring or a targeted comment.

Disallowed example (defensive local alias):
```
@property
def validated(self) -> bool:
    """ True if the validation phase has run and marked this spell as validated. """
    crafter = self._crafter
    return crafter.validated if crafter is not None else False

@property
def is_broken(self) -> bool:
    """ True if the validation phase classified this spell as broken / unsafe. """
    crafter = self._crafter
    return crafter.is_broken if crafter is not None else False
```

Banned / Disallowed Patterns
* Never use type: ignore.
* Never use # noqa.
* eval() / exec() / compile() are allowed for agent work when codegen is required.
* Never use wildcard imports (e.g., from module import *).
* Never use PEP 604 union syntax (e.g., A | B, T | None); use Optional/Union.

Never use
- type: ignore
- # noqa
- eval() / exec() / compile() for non-codegen work
- wildcard imports
- from __future__ import annotations (new files must not add this)
- PEP 604 unions (A | B, T | None); use Optional/Union
- TYPE_CHECKING blocks/imports; use Protocol/ABC interfaces instead

Dataclass restrictions
- Do not use dataclasses to store object references or owned resources.
- Dataclasses may only contain value types (str, int, float, bool, None) and containers of those value types.
- If object references are required, use a normal class with explicit cleanup.

Cleanup/disposal guidance
- Proper usage: `agent_onboarding/user_defined/synaptic_python_developer/skills/python/cleanup_and_disposal.md`
- Anti-patterns: `agent_onboarding/user_defined/synaptic_python_developer/examples/python/anti_patterns.py`
- Cleanup/disposal anti-patterns (summary):
  - Snapshotting owned `self._fields` into locals as defensive cleanup guards.
  - Defensive `None` checks on owned fields when lifecycle guarantees they exist.
  - Relying on GC for owned resources instead of explicit cleanup.
  - Skipping explicit null assignments after cleanup.
  - Cleaning loggers before owned children.
  - Placeholder comments like "already nulled above" instead of nulling fields.

Owned-code strictness
- Do not use getattr/hasattr for owned attributes.
- Handle AttributeError only for truly optional external interfaces.

Exception
- Polymorphic lock cleanup may use hasattr(lock, "cleanup").

Examples
- agent_onboarding/user_defined/synaptic_python_developer/examples/python/anti_patterns.py




