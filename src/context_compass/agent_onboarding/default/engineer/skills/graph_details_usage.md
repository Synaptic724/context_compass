# graph_details_usage

## Purpose
- Define how engineers read and use the canonical graph-details manifest:
  - `context_compass/system_docs/readable_src_graph.json`
- Keep the graph useful as a fast relationship map without treating it as a
  replacement for architecture/components docs.

## When To Use
- You need to understand object wiring fast.
- You need to know who owns lifecycle vs who only borrows a reference.
- You need to know what creates, validates, publishes, binds, or queries what.
- You need a structural map before opening deep code paths.

Scope rule:
- `src_graph.json` is the compressed storage artifact for a source-runtime graph.
- `readable_src_graph.json` is the primary line-based consumption artifact.
- Do not expect `tests/` objects or test harness relationships inside it.
- Use `tests_architecture.md` and `tests_components.md` for the test-side model.

## Required Read Order
When relationship questions are in scope:
1. `context_compass/system_docs/readable_src_graph.json`
2. `context_compass/system_docs/graph_details_document.md`
3. `context_compass/system_docs/src_architecture.md`
4. `context_compass/system_docs/src_components.md`
5. `context_compass/system_docs/src_graph.json` only when storage verification
   or raw canonical checks matter

Use the readable graph first for fast orientation.
Use architecture/components docs for the full narrative and deeper lifecycle
detail.

## Primary Consumption Rule
- Read `readable_src_graph.json` in bounded line chunks.
- Treat `src_graph.json` as storage, not as the normal reading surface.
- Use `src_graph.expanded.json` only when editing or doing full patch review.

## How To Read The Graph
Read nodes first:
- `id`
  - canonical object identity
- `label`
  - short name
- `kind`
  - class/component/interface/module
- `file`
  - where it lives
- `role`
  - what it is
- `responsibilities`
  - what it does
- `owns_state`
  - what important state/resources it owns
- `phases`
  - when it matters

Read edges second:
- `relation`
  - the relationship type
- `why`
  - what that relationship actually means
- `cardinality`
  - how many of the target exist from the source perspective
- `phase`
  - when the relationship matters
- `strength`
  - hard ownership vs borrowed/soft coupling

## Interpretation Rules
- `owns_lifecycle_of`
  - hard lifecycle responsibility
- `borrows`
  - uses a collaborator without owning cleanup
- `creates`
  - construction responsibility
- `validates`
  - validation responsibility
- `publishes`
  - publication or projection responsibility
- `binds`
  - workstation/binding-canvas or similar binding responsibility

## Conflict Handling
If graph, architecture/components docs, and source disagree:
- treat the graph as stale
- do not promote the graph claim to fact by itself
- reopen architecture/components docs and then source
- patch the graph only after the real relationship is evidenced

## Rules
- The graph is a fast relationship surface, not a narrative system doc.
- Do not use the graph alone for deep implementation claims.
- Do not infer absent relationships; if it is not in the graph and not in the
  docs, treat it as `UNKNOWN`.
- Prefer the graph when the question is structural and the docs when the
  question is narrative or lifecycle-heavy.
- Prefer `readable_src_graph.json` over `src_graph.json` for all line-based
  reading.

## References
- `context_compass/system_docs/readable_src_graph.json`
- `context_compass/system_docs/graph_details_document.md`
- `agent_onboarding/default/engineer/skills/graph_details_readable_generation.md`
- `context_compass/system_docs/src_architecture.md`
- `context_compass/system_docs/src_components.md`
