
# configuration_map_guide

Purpose
- Explain where configuration lives, and why role routing is not controlled
  from it.

## Two files, two jobs

Role identity and routing
- `SKILLS.MD` - the **single role registry**.
- The registry table is the only place a role is declared. It carries the role
  name, its `SKILLS.MD` path, its parent role, whether it is user-defined,
  whether it is selectable after onboarding, and whether it reads READMEs.
- A role exists if and only if it has a row in that table.

Behaviour settings
- `config/context_compass_config.yaml` - **behaviour only**.
- It does not enumerate roles and is never consulted to discover or resolve a
  role. Do not look for a roles map, an available-profiles list, or a readme
  policy here; none of them exist.

## Config sections

- `profiles.onboarding`
  - first-time onboarding state and transition defaults.
- `system_of_record`
  - whether Context Compass is the only permitted place to track work.
- `workflow`
  - ticket microcycle and note behaviour controls.
- `artifacts`
  - artifact board and lifecycle controls.
- `documentation_format`
  - line length and evidence formatting rules.
- `reading`
  - per-read line limits for chunked reading.

## Keys that matter for onboarding

- `profiles.onboarding.first_time_enabled`
  - Whether first-time onboarding still needs to run.
- `profiles.onboarding.first_time_default_profile`
  - Entry role for first-time onboarding (typically `new`).
- `profiles.onboarding.post_onboarding_profile_mode`
  - `choose` = ask the user which role to take once onboarding completes.
- `profiles.onboarding.fallback_post_onboarding_profile`
  - Safe fallback if no explicit choice is made.

Which roles may be chosen after onboarding is **not** a config key. It is the
`selectable after onboarding` column in the `SKILLS.MD` registry.

## Role assignment basics

1. Confirm the role has a row in the `SKILLS.MD` registry table.
2. Confirm the `skills path` in that row points at a file that exists.
3. Confirm the row's `extends` value matches the `INHERITS_SKILLS_FROM` header
   inside the role's own `SKILLS.MD`.

If a directory exists under `agent_onboarding/user_defined/` but has no
registry row, it is not a role and is not selectable.

## Recommended defaults after onboarding

- For general code-development work: `engineer`.
- For specialized posture, choose the closest matching role from the registry
  table. The table's `extends` column shows what each role builds on, so a role
  extending `engineer` carries all engineering baseline behaviour plus its own
  delta.

## Validation checks

- Read `context_compass/SKILLS.MD` and confirm the registry table parses and
  every `skills path` resolves.
- For the selected role, read its `SKILLS.MD` and walk `INHERITS_SKILLS_FROM`
  to the root, confirming each parent file exists.
- Confirm `context_compass/config/context_compass_config.yaml` contains no role
  lists. If it does, the registry has been duplicated and must be collapsed
  back to `SKILLS.MD`.

References
- `SKILLS.MD`
- `agent_onboarding/default/new/skills/profile_model_explained.md`
- `PROFILE_CLASS_CREATION_GUIDE.md`
