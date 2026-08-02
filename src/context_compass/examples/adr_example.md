# Example: ADR - Repository-Local Example Strategy

Status
- Accepted

Context
- Top-level examples were not grounded in this repository and did not provide a
  complete workflow chain.

Decision
- Use this repository as the canonical public example.
- Require full epic/story/task/artifact examples under `examples/example_*`.
- Keep copy-safe entrypoint references to
  `context_compass/AGENTS.MD`.

Consequences
- Users can copy `context_compass/` and follow a complete workflow immediately.
- Documentation maintenance must keep all cross-links synchronized.

Implementation links
- epic:
  `examples/example_epics/2026-02-19_context_compass_release_readiness_example_pack_epic.md`
- story:
  `examples/example_stories/2026-02-19_context_compass_release_readiness_examples_story.md`
- task:
  `examples/example_tasks/2026-02-19_context_compass_release_readiness_pack_task.md`
- artifact:
  `examples/example_completed/2026-02-19_context_compass_release_overview_artifact.md`

