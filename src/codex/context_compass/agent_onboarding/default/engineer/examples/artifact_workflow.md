# Engineer Example: Artifact Workflow

Context
- An engineer needs to harden Context Compass entrypoint wiring so each runtime package references only its native entrypoint.
- The agent wants to capture scratch thoughts before committing to a ticket.

Scratch capture (workspace)
- Path: `workspace/agent/ideas/context_compass_entrypoint_wiring.md`
- Example content:

```md
# idea: context_compass_entrypoint_wiring
## Why now
- cross-runtime references confuse package consumers.
- runtime-specific docs must be deterministic after copy/paste install.

## Early hypothesis
- codex package should reference `AGENTS.MD` only.
- gemini package should reference `GEMINI.MD` only.

## Risk notes
- broad search/replace can break role-level policy references.
- docs can drift if validation commands are not captured.

## Promote when
- runtime-specific scans return zero cross-runtime tokens.
```

- Path: `workspace/agent/todo/context_compass_entrypoint_wiring.md`
- Example content:

```md
# todo: context_compass_entrypoint_wiring
- [ ] inventory cross-runtime references
- [ ] patch docs/examples/system docs to runtime-native entrypoints
- [ ] validate role-level entrypoint files still resolve
```

Promote to ticket (curated)
- Path: `tickets/stories/YYYY-MM-DD_context_compass_entrypoint_wiring_story.md`
- Example content:

```md
# story: context_compass_entrypoint_wiring
## Goal
- runtime packages reference only their native entrypoint documents

## Scope
- top-level readme, system docs, and example docs wiring

## Out of scope
- role-policy redesign or behavior changes

## Files to touch
- context_compass/README.md
- context_compass/system_docs/src_architecture.md
- context_compass/system_docs/src_components.md
- context_compass/examples/repo_overview.md

## Risks
- accidental deletion of required role-level references
- malformed path rewrites in code-map sections

## Tests
- rg -n "GEMINI" src/codex/context_compass
- rg -n "AGENTS" src/gemini/context_compass

## Done criteria
- codex distribution has no GEMINI entrypoint references
- gemini distribution has no AGENTS entrypoint references
```

Strategy alignment
- Path: `attention_board.md` (route active work item to the canonical ticket)
- Path: active ticket `## Notes` (store rationale, evidence, and next actions)

Tactics / runbook
- Path: `tickets/tasks/YYYY-MM-DD_context_compass_entrypoint_wiring_task.md`
- Example content:

```md
# task: context_compass_entrypoint_wiring
## Preconditions
- current entrypoint references are inventoried
- scope constrained to docs and policy wiring

## Steps
1) patch runtime-specific references
2) verify role-level entrypoint files remain valid
3) run strict cross-runtime token scans
4) document outcomes in ticket notes
```

Work queue conversion
- When approved, convert the todo into a story/task ticket in `tickets/stories/` or `tickets/tasks/`.
- Example work items (summarized):
  - Task: remove cross-runtime top-level entrypoint references
  - Task: validate role-chain entrypoint files after rewiring
