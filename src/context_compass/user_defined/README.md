# user_defined

Your space. Put anything here.

The package never writes into this directory. Not on upgrade, not on cleanup,
not in any mode. Nothing here is listed in `MANIFEST.md` as package content, and
no tool will restore, replace, or remove what you put in it.

## Why this exists

Everything else at the top level belongs to the package: `AGENTS.MD`, `SKILLS.MD`,
`agent_onboarding/default/`, `templates/`, `tools/`, `examples/`. An upgrade
conforms those to the new version, because they are the library and keeping a
local edit there only preserves a divergence you will have to re-resolve on every
future upgrade.

So when you need something the package does not provide, it goes here rather than
into a package file. That way an upgrade never has to choose between your work
and the new version - the question does not arise.

## What belongs here

- scripts, notes, checklists, conventions specific to this repository
- reference material you want agents to be able to find
- anything you would otherwise have been tempted to paste into a package file

## What does NOT belong here

- **role overlays.** Those go in `agent_onboarding/user_defined/<name>/` and need
  a row in the `SKILLS.MD` registry to be selectable. This directory is not on
  any role's readset, so a role placed here is invisible to routing.
- **project instructions agents must follow.** Those go in
  `special_instructions/`, which every role reads during onboarding. Files here
  are not read automatically - an agent finds them only if something points at
  them.

## The other lanes that are yours

| lane | holds |
| --- | --- |
| `user_defined/` | this directory - anything at all |
| `agent_onboarding/user_defined/` | role overlays, registered in `SKILLS.MD` |
| `special_instructions/` | project rules, read during onboarding |
| `system_docs/` | your architecture, component and test maps |
| `tickets/` | your work |
| `artifacts/` | your findings |
| `context_management/` | your context board |

Everything outside those is the package's and is conformed on upgrade.
