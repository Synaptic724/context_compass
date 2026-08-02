
# SKILLS Role Map

Purpose
- This file is the **single registry of roles** in Context Compass.
- A role exists if and only if it has a row in the registry table below.
- Resolve the selected role to its `SKILLS.MD` entry point from this table.

## Registry contract (non-negotiable)

- This table is the only place roles are declared. No other file lists roles.
- `config/context_compass_config.yaml` holds **behaviour settings only**. It does
  not enumerate roles and is never consulted to discover or resolve a role.
- Adding a role is a two-step change: add one row here, and create the
  `SKILLS.MD` it points to. Nothing else needs editing.
- Role selection is **per agent, per session**. There is no stored or global
  active role. Multiple agents may hold different roles in the same repository
  at the same time, which is why no single value can represent "the" role.

## Role registry

| role | skills path | extends | user-defined | selectable after onboarding | reads README |
| --- | --- | --- | --- | --- | --- |
| `new` | `agent_onboarding/default/new/SKILLS.MD` | - | no | no | yes |
| `general` | `agent_onboarding/default/general/SKILLS.MD` | - | no | yes | no |
| `engineer` | `agent_onboarding/default/engineer/SKILLS.MD` | `general` | no | yes | no |
| `design_engineer` | `agent_onboarding/default/design_engineer/SKILLS.MD` | `engineer` | no | yes | no |
| `platform_engineer` | `agent_onboarding/default/platform_engineer/SKILLS.MD` | `engineer` | no | yes | no |
| `qa_engineer` | `agent_onboarding/default/qa_engineer/SKILLS.MD` | `engineer` | no | yes | no |
| `security_engineer` | `agent_onboarding/default/security_engineer/SKILLS.MD` | `engineer` | no | yes | no |
| `story_designer` | `agent_onboarding/default/story_designer/SKILLS.MD` | `general` | no | yes | no |
| `story_novel_artist` | `agent_onboarding/default/story_novel_artist/SKILLS.MD` | `general` | no | yes | no |
| `researcher` | `agent_onboarding/default/researcher/SKILLS.MD` | `general` | no | yes | no |
| `draft_writer` | `agent_onboarding/default/draft_writer/SKILLS.MD` | `general` | no | yes | no |
| `developmental_editor` | `agent_onboarding/default/developmental_editor/SKILLS.MD` | `general` | no | yes | no |
| `line_copy_editor` | `agent_onboarding/default/line_copy_editor/SKILLS.MD` | `general` | no | yes | no |
| `continuity_fact_checker` | `agent_onboarding/default/continuity_fact_checker/SKILLS.MD` | `general` | no | yes | no |
| `proofreader` | `agent_onboarding/default/proofreader/SKILLS.MD` | `general` | no | yes | no |
| `synaptic_finishing_developer` | `agent_onboarding/user_defined/synaptic_finishing_developer/SKILLS.MD` | `engineer` | yes | yes | no |
| `synaptic_python_developer` | `agent_onboarding/user_defined/synaptic_python_developer/SKILLS.MD` | `engineer` | yes | yes | no |
| `data_engineer` | `agent_onboarding/user_defined/data_engineer/SKILLS.MD` | `engineer` | yes | yes | no |

Column meanings
- **extends**: the parent role whose `SKILLS.MD` chain is read first. Must match
  the `INHERITS_SKILLS_FROM` header inside the role's own `SKILLS.MD`.
- **user-defined**: lives under `agent_onboarding/user_defined/` rather than
  `agent_onboarding/default/`. Project- or team-specific overlays.
- **selectable after onboarding**: may be chosen as a steady-state role once
  first-time onboarding is complete. `new` is entry-only and is never a
  steady-state role.
- **reads README**: whether this role reads role README files during onboarding.
  Only `new` does; every other role uses policy and skills docs. README files are
  user-facing.

Unregistered overlays
- `agent_onboarding/user_defined/<name>/SKILLS.MD` is the path convention for a
  new user-defined role, but a role at that path is **not selectable until it has
  a row in the table above**. A directory on disk with no row is not a role.

## Role selection directive (non-negotiable)

1. When this file is read, list the roles from the registry table.
2. Ask the user which role to take on, unless they already selected one.
3. Resolve the selected role to its `SKILLS.MD` path from the table.
4. Read that `SKILLS.MD`, then walk `INHERITS_SKILLS_FROM` upward and read the
   whole chain **parent-first**.
5. Treat the resolved chain as the routing manifest:
   - You MUST read every path listed under **Active skills** / **Required
     baseline skills** in each `SKILLS.MD` in the chain.
   - **On-demand** skills are conditional. Do NOT read them for certification
     unless a trigger condition is met.
   - When an on-demand trigger is met, those paths become mandatory and MUST be
     read before proceeding in that scope.

## Format contract for role `SKILLS.MD` files

Every role `SKILLS.MD` uses one dialect so a single parser reads them all:

- Inheritance header: ``- `INHERITS_SKILLS_FROM: <path|none>` ``
- Skill entries: ``- `<path>` `` — one backticked path per list item.

**There is one entry form, not two.** Baseline and on-demand entries look
identical; the section heading a path sits under is what classifies it. Do not
prefix on-demand entries with `Read:` or any other marker — a second form means
a second parser, and the parser written for the first one silently returns an
empty on-demand readset instead of failing.

Bare (unbackticked) paths are not valid, and a backticked path must be a list
item. A path indented under a sentence is prose, not an entry, and a parser will
not see it. If a path must be read, it is a list item; if it is illustration,
name the file without making it look like an entry.

A parser written for this dialect must be able to read every role file in the
package. If it cannot, the role file is wrong, not the parser.

## Notes

- This file is a routing manifest, not a license to read the whole repo.
- Baseline and on-demand triggers are defined in the resolved role `SKILLS.MD`
  files and enforced by `AGENTS.MD` and
  `agent_onboarding/default/general/skills/compaction_requirements.md`.
- The roles are delta layers, not separate systems:
  - `general` is the shared baseline for all work.
  - `engineer` extends `general` for implementation-focused engineering.
  - `design_engineer`, `platform_engineer`, `qa_engineer`, and
    `security_engineer` extend `engineer` for specialized software workflows.
  - The fiction-authoring roles extend `general`.
  - The `user_defined` roles extend `engineer`.
