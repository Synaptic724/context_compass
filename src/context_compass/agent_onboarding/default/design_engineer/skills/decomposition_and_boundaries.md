
# decomposition_and_boundaries

Purpose
- Teach a consistent way to decompose systems into components with clean boundaries.
- Reduce coupling and increase change safety.

Boundary rules (practical)
- Prefer stable seams:
  - public interfaces, adapters, service boundaries, domain modules.
- Keep dependencies directional:
  - dependencies flow from higher-level policy to lower-level mechanisms (not the reverse).
- Avoid "shared mutable state" across boundaries unless explicitly designed.
- Use contracts:
  - data contracts (schemas),
  - behavior contracts (docstrings, invariants),
  - interface contracts (API versioning, error semantics).

Decomposition workflow
1) Identify the smallest set of responsibilities required.
2) Group responsibilities that must change together.
3) Split responsibilities that change for different reasons.
4) Define boundaries and interfaces.
5) Identify cross-cutting concerns:
   - logging, auth, retries, caching, migrations.
6) Define dependency rules:
   - what is allowed to import/call what.
7) Validate with scenarios:
   - "What changes when requirement X changes?"

Output checklist
- Components list with responsibilities
- Dependency graph (even a bullet list)
- Interfaces between components
- Failure-handling strategy per boundary
- Test boundaries (unit vs integration)

References
- `agent_onboarding/default/design_engineer/skills/architecture_contexts.md`
- `agent_onboarding/default/design_engineer/skills/api_and_interface_design.md`


