

Hand this to your agent when you want help creating a role. It is large and is deliberately outside the normal skill paths except `new`.

# Profile Class Creation Guide

## Why this file exists
- This is a user-facing playbook for building and assigning profile classes.
- It is intentionally large and explicit so you can hand it to an agent during
  first-time onboarding.
- It is not meant to be loaded by every profile path.

## What context_compass is
- A code-development workflow system.
- A durable context system for AI-assisted engineering.
- A structure that keeps planning, execution, and handoff consistent.

## What it supports
- Any programming language.
- AI-agent-driven workflows.
- Other AI agents, as long as they obey the same policy contracts.

## Recommended execution mode
- Use the strongest reasoning setting your runtime offers.
- Other reasoning modes are not yet validated here.

## Core concepts

### 1) Profile class
- A class/profile is a curated read path for behavior and skills.
- Profiles are route targets resolved by the `SKILLS.MD` registry table to a
  role `SKILLS.MD`.

### 2) Inheritance
- Parent profile docs load first.
- Child profile docs load last.
- Child profile `SKILLS.MD` should add deltas, not duplicate parent paths.

> The registry table in `context_compass/SKILLS.MD` is the authoritative
> role list. The descriptions below are teaching material for first-time
> onboarding and do not include user-defined roles. If the two disagree,
> the registry wins.

### 3) Default class
- This is the profile loaded after onboarding.
- For general code work, `engineer` is the recommended default.
- Use specialized defaults when the work demands it:
  - software lane: `design_engineer`, `platform_engineer`, `qa_engineer`, `security_engineer`
  - fiction lane: `story_designer`, `story_novel_artist`, `researcher`, `draft_writer`,
    `developmental_editor`, `line_copy_editor`, `continuity_fact_checker`, `proofreader`

### 4) User-defined class
- A custom profile you create under `agent_onboarding/user_defined/`.
- Usually extends `engineer`.

## Current baseline classes
- `new`
  - first-time onboarding and class selection.
- `general`
  - shared system behavior, ticketing, process controls.
- `engineer`
  - general-purpose code-development execution layered on top of `general`.
- `design_engineer`
  - software/system design specialization layered on top of `engineer`.
- `platform_engineer`
  - CI/CD, deployment, observability, and operations specialization layered on top of `engineer`.
- `qa_engineer`
  - test strategy, quality gates, and release signoff specialization layered on top of `engineer`.
- `security_engineer`
  - threat modeling, security review, and hardening specialization layered on top of `engineer`.
- `story_designer`
  - narrative architecture specialization layered on top of `general`.
- `story_novel_artist`
  - visual language and art-direction specialization layered on top of `general`.
- `researcher`
  - evidence and plausibility specialization layered on top of `general`.
- `draft_writer`
  - manuscript drafting and rewrite specialization layered on top of `general`.
- `developmental_editor`
  - structural editing specialization layered on top of `general`.
- `line_copy_editor`
  - line/copy prose specialization layered on top of `general`.
- `continuity_fact_checker`
  - canon/timeline/fact integrity specialization layered on top of `general`.
- `proofreader`
  - final lock and surface-quality specialization layered on top of `general`.
- `user_defined/*`
  - personal or team overlays (usually extend the closest matching default role).
## Where classes are declared

A class is declared in exactly one place: the registry table in
`context_compass/SKILLS.MD`.

Each row carries everything the system needs:
- role name
- `SKILLS.MD` path
- `extends` (parent role)
- user-defined flag
- selectable-after-onboarding flag
- reads-README flag

`context_compass/config/context_compass_config.yaml` holds behaviour settings
only. It does not enumerate roles. Do not add role lists to it.

Inheritance is declared a second time inside the role's own `SKILLS.MD`:
- `` - `INHERITS_SKILLS_FROM: <skills_path|none>` ``

The registry `extends` column and that header must agree.

## Class creation checklist
- [ ] Choose class name.
- [ ] Create onboarding folder structure.
- [ ] Create profile `SKILLS.MD` file.
- [ ] Create profile `WORKFLOWS.MD` file if this role should own workflows.
- [ ] Create profile `workflows/` folder if this role should own workflows.
- [ ] Add class to config.
- [ ] Define `SKILLS.MD` inheritance header.
- [ ] Validate `SKILLS.MD` paths and overlap rules.
- [ ] Assign active/default class.

## Step-by-step: create a new class

### Step 1: Choose a class name
Example:
- `data_engineer`
- `frontend_engineer`
- `security_engineer`

Naming rules:
- lower_snake_case
- avoid spaces
- keep it short and descriptive

### Step 2: Create folder skeleton
Create this structure:

```text
context_compass/
  agent_onboarding/
    user_defined/
      <profile_name>/
        WORKFLOWS.MD
        profile_overrides.md
        policies/
          <profile_name>_policy_overrides.md
        behavioral_guidelines/
          <profile_name>_behavior_overrides.md
        skills/
          <profile_name>_skill_overrides.md
        workflows/
```

You can add subfolders under `skills/` as needed.

### Step 3: Create profile SKILLS file
Create:

```text
context_compass/agent_onboarding/user_defined/<profile_name>/SKILLS.MD
```

SKILLS.MD rules:
- one relative path per line, as a backticked list item
- inheritance header required for inheriting profiles:
  - `INHERITS_SKILLS_FROM: <skills_path|none>`
- no duplicated parent paths from inherited `SKILLS.MD`

**Group your paths under sections, and the section is what classifies them.**
This is the part that is easy to miss, because the entry form is identical either
way — a path is baseline or on-demand purely by the heading it sits under:

- **Baseline sections** are read for onboarding and certification. Name them for
  what they hold: `Active skills`, `Required baseline skills`, or something the
  role actually needs, such as `engineer`'s `Baseline system orientation`.
- **`On-demand`** is the one reserved name. A section marked on-demand is read
  only when its trigger fires. State the trigger.

A path in no section at all is ambiguous, and the enforcement rules treat anything
not marked on-demand as baseline — so an ungrouped path becomes a mandatory read
by default. That is the safe direction, but it is not the one you meant, so put
every path under a heading.

Your role may add a baseline section the parent chain does not have. Say so in the
role's own `Skill classes` block, and say that the inherited chain contributes its
own baseline sections too — a role file that describes only what it adds reads as
the complete list and is how a class goes missing.

Full dialect, including why there is only one entry form:
`context_compass/SKILLS.MD`, "Format contract for role `SKILLS.MD` files".

Workflow rules:
- actual workflow definitions should live in role-local `workflows/`
- role-local workflow manifest should be `WORKFLOWS.MD`
- use:
  - `INHERITS_WORKFLOWS_FROM: <workflow_manifest_path|none>`
- workflows are user-generated and user-approved only
- workflow manifests may contain:
  - `Active workflows`
  - `On-demand workflows`
- on-demand workflows should be discoverable but not baseline-read until
  explicitly selected by the user or clearly triggered by the task
- templates for workflow scaffolding live in:
  - `context_compass/templates/workflow_simple_template.md`
  - `context_compass/templates/workflow_advanced_template.md`

Example:

```text
INHERITS_SKILLS_FROM: agent_onboarding/default/engineer/SKILLS.MD
agent_onboarding/user_defined/data_engineer/profile_overrides.md
agent_onboarding/user_defined/data_engineer/policies/data_engineer_policy_overrides.md
agent_onboarding/user_defined/data_engineer/behavioral_guidelines/data_engineer_behavior_overrides.md
agent_onboarding/user_defined/data_engineer/skills/data_engineer_skill_overrides.md
```

### Step 4: Register the class in the registry

Add one row to the registry table in `context_compass/SKILLS.MD`:

```markdown
| `data_engineer` | `agent_onboarding/user_defined/data_engineer/SKILLS.MD` | `engineer` | yes | yes | no |
```

That single row registers the class, its path, its parent, its user-defined
status, whether it can be selected after onboarding, and its README policy.

No config edit is required. If you find yourself adding the role name to
`context_compass/config/context_compass_config.yaml`, stop: the registry has
been duplicated, and duplication is what produced orphaned and half-registered
roles in earlier versions of this package.

### Step 5: Validate class wiring
Run checks:

```powershell
rg -n "data_engineer" context_compass/SKILLS.MD
Get-Content context_compass/agent_onboarding/user_defined/data_engineer/SKILLS.MD
```

Confirm:
- the registry row exists and its `skills path` resolves
- the row's `extends` value matches the `INHERITS_SKILLS_FROM` header
- `context_compass/config/context_compass_config.yaml` does not mention the role

Validate `SKILLS.MD` path existence (manual method):
- open each path listed in the class `SKILLS.MD`
- confirm files exist and are readable

Validate overlap discipline:
- compare child `SKILLS.MD` lines against parent `SKILLS.MD` lines
- remove duplicates from child `SKILLS.MD`
- confirm child `SKILLS.MD` starts with inheritance header:
  - `INHERITS_SKILLS_FROM: <parent_skills_path>`

Validate workflow discipline (when used):
- confirm `<profile_root>/WORKFLOWS.MD` exists when the role owns workflows
- confirm the workflow manifest starts with:
  - `INHERITS_WORKFLOWS_FROM: <parent_workflows_path|none>`
- confirm actual workflow definitions live in `<profile_root>/workflows/`
- confirm agents did not invent or add workflows without user request/approval

## Recommended class design patterns

### Pattern A: Strict overlay
- Keep default behavior in `general` + `engineer`.
- Put only preferences and deltas in user-defined class.

### Pattern B: Domain overlay
- Add domain-specific workflows (data, UI, infra).
- Keep shared code-quality rules inherited from `engineer`.

### Pattern C: Team policy overlay
- Add team conventions, review gates, and naming rules.
- Keep system mechanics unchanged.

### Pattern D: Role-local workflows
- Put reusable macro behaviors in:
  - `<role_root>/WORKFLOWS.MD`
  - `<role_root>/workflows/`
- Keep actual workflow instances role-local.
- Keep templates global.
- Do not create a top-level workflow registry.

## Anti-patterns to avoid
- Duplicating entire parent `SKILLS.MD` path lists in child classes.
- Putting shared system rules in user-defined profiles.
- Mixing onboarding docs into non-`new` flow without role intent.
- Forgetting to add the registry row in `SKILLS.MD`.
- Re-adding role lists to the config file.
- Creating a top-level workflow registry when the workflow should live in the role.
- Letting agents create or modify workflows at their own discretion.

## Profile file templates

### profile_overrides.md

```markdown
# <profile_name> profile_overrides

Purpose
- Define user/team-specific profile behavior deltas.

Scope
- Applies only when the selected role is `<profile_name>`.

Rules
- Keep this profile as a delta layer over `engineer`.
- Do not duplicate inherited baseline docs.
```

### policy override template

```markdown
# <profile_name>_policy_overrides

Purpose
- Add policy deltas for this profile.

Policy
- <rule 1>
- <rule 2>
```

### behavior override template

```markdown
# <profile_name>_behavior_overrides

Purpose
- Define behavior and communication deltas for this profile.

Behavior
- <behavior 1>
- <behavior 2>
```

### skill override template

```markdown
# <profile_name>_skill_overrides

Purpose
- Define skills specific to this profile.

Skills
- <skill 1>
- <skill 2>
```

## How onboarding transitions should work

### First-time entry
- Route into `new`.
- Explain system + profiles + config.
- Ask user to select steady-state default class.

### Post-onboarding entry
- Route directly to selected default class path order.
- If class inherits `engineer`, `SKILLS.MD` headers resolve
  `general` then `engineer` then custom.

## Recommended default class choice
- For general code development, default to `engineer`.
- For specialized posture, default to the closest matching role:
  - `design_engineer` for architecture/design work,
  - `platform_engineer` for CI/CD/deploy/observability/ops,
  - `qa_engineer` for testing and quality gates,
  - `security_engineer` for security review and hardening,
  - `story_designer` for fiction narrative architecture,
  - `story_novel_artist` for visual language and art direction,
  - `researcher` for source-backed plausibility,
  - `draft_writer` for manuscript drafting and rewrites,
  - `developmental_editor` for structural editing and rewrite planning,
  - `line_copy_editor` for prose polish and consistency,
  - `continuity_fact_checker` for canon/timeline/fact checks,
  - `proofreader` for final typo/punctuation/format lock.
- Use user-defined classes when you need preference/domain overlays.

## Fast operator checklist
- [ ] I know the class name I want.
- [ ] I created class folder + files under `user_defined`.
- [ ] I created `SKILLS.MD` under `agent_onboarding/user_defined/<profile_name>/`.
- [ ] I updated config profile lists and roles-map role registration.
- [ ] I added the `SKILLS.MD` inheritance header.
- [ ] I validated `SKILLS.MD` paths and overlap contract.

## Troubleshooting

### Class does not load
Check:
- the class has a row in the `SKILLS.MD` registry table
- the row's `skills path` is correct and readable
- the row's `extends` value matches the class `SKILLS.MD` header

### Wrong docs load order
Check:
- `SKILLS.MD` inheritance header:
  - `INHERITS_SKILLS_FROM: <skills_path|none>`
- parent-first ordering resolved from `SKILLS.MD` inheritance headers
- path entries not duplicated across parent/child `SKILLS.MD` files

### Behavior looks unchanged
Check:
- the selected role is what you think it is
- class docs are actually listed in class `SKILLS.MD`
- class docs contain real deltas, not empty placeholders

## File index
- `context_compass/config/context_compass_config.yaml`
- `context_compass/SKILLS.MD`
- `context_compass/templates/workflow_simple_template.md`
- `context_compass/templates/workflow_advanced_template.md`
- `context_compass/agent_onboarding/default/new/SKILLS.MD`
- `context_compass/agent_onboarding/default/general/SKILLS.MD`
- `context_compass/agent_onboarding/default/general/WORKFLOWS.MD`
- `context_compass/agent_onboarding/default/engineer/SKILLS.MD`
- `context_compass/agent_onboarding/default/engineer/WORKFLOWS.MD`
- `context_compass/agent_onboarding/user_defined/<profile_name>/SKILLS.MD`
- `context_compass/agent_onboarding/user_defined/<profile_name>/WORKFLOWS.MD`
- `context_compass/agent_onboarding/user_defined/`

## Final note
- Use this guide through `new` onboarding when creating a class.
- Keep class changes explicit, additive, and validated before switching
  defaults.

