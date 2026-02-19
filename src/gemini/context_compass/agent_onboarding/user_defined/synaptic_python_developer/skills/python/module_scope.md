

# module_scope

Purpose
- Prevent hidden shared state and lifecycle confusion.

Module Scope: Types + Pure Helpers Only
* Avoid module-level mutable state (globals, caches, singletons, registries, shared clients).
* Prefer instance-bound methods/classes for anything with ownership/lifecycle (deps, logging, concurrency, cleanup, configuration).
* Allowed at module scope:
  * type aliases, Protocols, ABCs, TypeVar/ParamSpec, and other generic definitions
  * pure functions (no side effects, no hidden state, deterministic)
* Do not add module-level constants or hidden sentinels; define constants on classes/config objects instead.
* If a helper is not obviously pure/stateless or would introduce shared state, ask first.
* If an existing module already uses module-level helpers, you may follow the pattern, but do not add new module globals without asking.

Rules
- Avoid module-level mutable state (globals, caches, registries).
- Module scope is limited to type/generic definitions and pure helper functions.
- Do not introduce module-level constants; use class attributes or config objects.
- If a helper is not obviously pure, ask before adding.
- Prefer instance-owned resources for anything with lifecycle or cleanup.

Examples
- Allowed: ResultT = TypeVar("ResultT")
- Allowed: class SupportsClose(Protocol): ...
- Allowed: def normalize_name(value: str) -> str
- Not allowed: FOO_TIMEOUT_SECONDS = 10 (move to class/config)
- Not allowed: mutable caches or shared client instances

Examples
- agent_onboarding/user_defined/synaptic_python_developer/examples/python/anti_patterns.py





