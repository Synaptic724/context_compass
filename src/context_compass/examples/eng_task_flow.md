# Example: engineer task flow (repo-based)

Scenario
- Active ticket: `examples/example_tasks/2026-02-19_context_compass_release_readiness_pack_task.md`
- Goal: build a complete release-readiness example chain using this repository
  as the working context.

Entry gate
- Scope is bounded to `examples/` and `system_docs/` docs surfaces.
- Story linkage exists:
  `examples/example_stories/2026-02-19_context_compass_release_readiness_examples_story.md`.

Ticket microcycle
1. Investigate
- Read templates and current example/system docs.

2. Document
- Record `FACT` and `UNKNOWN` findings with file evidence.

3. Plan
- Define file names, scope boundaries, and acceptance gates.

4. Implement
- Create/update epic/story/task/artifact and flow docs.

5. Validate
- Run grep checks for stale slugs and path quality.

Exit gate
- Task acceptance criteria are satisfied.
- Story and epic links are coherent.
