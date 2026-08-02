# Rich Repository Overview (Context Compass)

## What This Package Is
`context_compass/` is a docs-first operating model for long-running AI work. It
provides deterministic onboarding, role routing, ticket memory, and compaction
recovery so execution can continue reliably across sessions.

## Core Entry Points
- `context_compass/AGENTS.MD`: agent startup contract.

- `context_compass/SKILLS.MD`: top-level role map.

## Folder Map
- `config/context_compass_config.yaml`: profile + role routing config.
- `agent_onboarding/`: role chains and policy/skill docs.
- `tickets/`: operational epic/story/task lanes.
- `artifact_board.md`: artifact association/disposition index.
- `attention_board.md`: active-ticket routing index.
- `templates/`: canonical ticket templates.
- `system_docs/`: architecture and component maps.
- `examples/`: runnable workflow examples.

## End-to-End Example Chain
- Epic:
  `examples/example_epics/2026-02-19_context_compass_release_readiness_example_pack_epic.md`
- Story:
  `examples/example_stories/2026-02-19_context_compass_release_readiness_examples_story.md`
- Task:
  `examples/example_tasks/2026-02-19_context_compass_release_readiness_pack_task.md`
- Artifact:
  `examples/example_completed/2026-02-19_context_compass_release_overview_artifact.md`

## How To Read This Repo Fast
1. Start with `AGENTS.MD`.
2. Read `SKILLS.MD` and resolve the role chain.
3. Read `config/context_compass_config.yaml`.
4. Read `system_docs/src_architecture.md` and `system_docs/src_components.md`.
5. Follow the example epic/story/task chain above.

## Public-Release Quality Bar
- examples are repo-local and realistic
- story/task examples are template-complete
- flow docs point only to files that exist
- architecture/component docs use clean copy-safe paths
- no sample files leak into real `tickets/` or `artifacts/` lanes

## Common Failure Patterns
- referencing source-tree-prefixed paths instead of `context_compass/...` in copy-facing docs
- using placeholder narratives unrelated to this package
- marking tickets done without evidence and validation notes

## Adoption Steps
1. Copy `context_compass/` to repo root.
2. Enter through `AGENTS.MD`.
3. Select role from `SKILLS.MD`.
4. Create tickets from templates.
5. Use this example chain as the baseline quality model.

## Context / Handoff Summary
Treat this file plus the linked epic/story/task/artifact as the default public
workflow reference for this package.


