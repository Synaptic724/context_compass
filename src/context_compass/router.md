# router

Purpose
- Provide a stable, human-readable summary of profile routing authority.
- Clarify how profile selection maps to onboarding skill chains.

Routing authority (highest to lowest)
1. `config/context_compass_config.yaml`
2. `SKILLS.md`
3. Resolved role `SKILLS.md` files under `agent_onboarding/`

Deterministic route sequence
1. Read runtime entrypoint policy.
2. Read `config/context_compass_config.yaml`.
3. Read `SKILLS.md` and select role.
4. Resolve the role path in `router.roles`.
5. Read inherited `SKILLS.md` chain in parent-first order.
6. Read required baseline skills.
7. Read on-demand skills only when a trigger condition is met.

Do not use this file as policy override.
Use it as a routing map only.
