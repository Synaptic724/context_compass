# System Docs Read First

## Purpose
This note explains how to approach `system_docs/` in a fresh Context Compass
install.

Context Compass ships example context maps and example workflows. It does not
assume that your repository already has a real architecture map, component
map, test map, or graph-details map.

## Default Truth
- `examples/` contains reference examples that show the expected shape and
  depth of documentation. That is where the quality bar lives.
- **`system_docs/` ships EMPTY.** No architecture, component, test or graph
  document is seeded. A placeholder sitting in a live lane gets read as
  repository truth no matter what banner is on it, so the package does not put
  one there.
- Everything in this directory is yours. Nothing here is replaced on upgrade.
- Missing repo-specific context maps are not a defect in a fresh install.
- Users should be encouraged to build context maps for their own repository as
  real structure emerges.

## Read Order
The four context maps are two mirrored pairs: a source map and its test map at
each of the architecture and component levels. Read each pair together - the
test map uses the same section contract as its source map, so reading them apart
hides the thing that makes them useful.

1. `examples/example_architecture/src_architecture.md`
   Read this to see what a strong repo-specific architecture map should look
   like.
2. `examples/example_architecture/tests_architecture.md`
   Read this to see the test-side mirror of the architecture map.
3. `examples/example_components/src_components.md`
   Read this to see what a strong repo-specific component map should look like.
4. `examples/example_components/tests_components.md`
   Read this to see the test-side mirror of the component map.
5. `agent_onboarding/default/engineer/skills/src_graph_usage.md`
   Read this if graph-details workflow is needed.
6. `examples/example_graph_details/src_graph.md`
   Read this to see the readable graph format.
7. `examples/example_epics/2026-02-19_context_compass_release_readiness_example_pack_epic.md`
   Read this for example ticket structure.
8. `examples/example_stories/2026-02-19_context_compass_release_readiness_examples_story.md`
   Read this for example story structure.
9. `examples/example_tasks/2026-02-19_context_compass_release_readiness_pack_task.md`
   Read this for example task structure.
10. `examples/example_completed/2026-02-19_context_compass_release_overview_artifact.md`
    Read this for example completed-output structure.

## What To Do In A New Library
If the library is new and there is little or no repo-specific context yet:

- do not pretend a real architecture map already exists
- do not invent fake runtime truth just to fill `system_docs/`
- use the example docs as templates and quality bars
- create repo-specific context maps only when there is enough real structure to
  document

## Recommended First Context Maps
When the repository is ready, build these in order:

1. `system_docs/src_architecture.md`
   Create this when the system boundary, entrypoints, and major flows are
   understood.
2. `system_docs/src_components.md`
   Create this when concrete modules, ownership seams, and responsibilities are
   understood.
3. `system_docs/tests_architecture.md`
   Create this when the test model and validation layers are real enough to map.
4. `system_docs/tests_components.md`
   Create this when test surfaces, helpers, and fixtures need explicit
   ownership mapping.
5. `system_docs/src_graph_index.md` and `system_docs/src_graph.md`
   Create these only if graph-details workflow is actually needed for the repo.

## Live Execution Note
- `attention_board.md` and `tickets/` are live coordination surfaces.
- In a fresh install they may be sparse, empty, or starter-only.
- Historical examples belong in `examples/`, not in live `tickets/*/completed/`
  lanes.

## Use
- Start here when `system_docs/` has little or no repo-specific content.
- Treat `examples/` as the model pack.
- Encourage the user to build real context maps rather than relying on empty
  placeholders.
