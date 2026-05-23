# Engineer Example: Artifact Workflow

Context
- An engineer needs to harden the release surface so the package contains only
  intended runtime references and no stale local or private paths.
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
- the package should expose only intended runtime entrypoints.
- stale local paths and old package-layout references should be removed before
  release.

## Risk notes
- broad search/replace can break role-level policy references.
- docs can drift if validation commands are not captured.

## Promote when
- release-surface scans return zero stale private-path or old-layout tokens.
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
- release-facing docs and examples contain only intended public references

## Scope
- top-level readme, system docs, and example docs wiring

## Out of scope
- role-policy redesign or behavior changes

## Files to touch
- context_compass/README.md
- context_compass/system_docs/src_architecture.md
- context_compass/system_docs/src_components.md
- context_compass/system_docs/readable_src_graph.json
- context_compass/examples/repo_overview.md

## Risks
- accidental deletion of required role-level references
- malformed path rewrites in code-map sections

## Tests
- run a direct-path scan for absolute local or private workspace paths
- run a legacy-vocabulary scan for stale private project terminology

## Done criteria
- release-facing docs contain no stale local/private path references
- release-facing docs contain no unrelated legacy project vocabulary
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
3) run strict release-surface scrub scans
4) document outcomes in ticket notes
```

Work queue conversion
- When approved, convert the todo into a story/task ticket in `tickets/stories/` or `tickets/tasks/`.
- Example work items (summarized):
  - Task: remove cross-runtime top-level entrypoint references
  - Task: validate role-chain entrypoint files after rewiring
