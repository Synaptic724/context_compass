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

**These are the EXAMPLE documents, and reading them whole is correct.** They are
small and you are reading them to learn a shape. Do not carry that habit across to
the live documents in this directory: once your repository has real maps, only
`src_architecture.md` and the two indexes are read whole, and `src_components.md`
and `src_graph.md` are entered through their indexes and sliced. That split is
defined in `agent_onboarding/default/engineer/SKILLS.MD`, and it is the difference
between a 200-line orientation and a 33,000-line one.

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

1. `system_docs/src_architecture.md` **and `src_architecture_index.md`**
   Create this when the system boundary, entrypoints, and major flows are
   understood.
2. `system_docs/src_components.md` **and `src_components_index.md`**
   Create this when concrete modules, ownership seams, and responsibilities are
   understood.
3. `system_docs/tests_architecture.md` and `tests_architecture_index.md`
   Create this when the test model and validation layers are real enough to map.
4. `system_docs/tests_components.md` and `tests_components_index.md`
   Create this when test surfaces, helpers, and fixtures need explicit
   ownership mapping.
5. `system_docs/src_graph_index.md` and `system_docs/src_graph.md`
   Create these only if graph-details workflow is actually needed for the repo.

**Every authored document gets its index in the same pass.** An index is not an
optional extra you add later when the document gets big - it is how the document
is meant to be entered, and roles read it as baseline orientation.
`src_architecture_index.md` and `src_components_index.md` in particular are what
let an agent onboard holding the maps without loading the territory: an
architecture narrative plus two indexes is a few thousand lines, while the
documents they point into run to tens of thousands.

An authored document shipped without its index is half-built. Regenerate the
index every time you edit the document - an index that lags still returns line
numbers, they are simply the wrong ones.

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
