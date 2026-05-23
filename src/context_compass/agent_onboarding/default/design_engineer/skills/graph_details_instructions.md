# graph_details_instructions

## Purpose
- Define the exact build and maintenance protocol for the canonical graph-details
  surfaces:
  - `context_compass/system_docs/graph_details_document.md`
  - `context_compass/system_docs/src_graph.json`
- Keep graph authoring aligned with the existing architecture/components doc
  stack instead of creating a competing prose layer.
- Treat graph-details as an optional repo-specific context surface, not as a
  mandatory shipped artifact for every fresh install.

## Canonical Outputs
- `context_compass/system_docs/graph_details_document.md`
- `context_compass/system_docs/src_graph.json`
- `context_compass/system_docs/readable_src_graph.json`

## Scope Boundary
This graph is for one chosen source/runtime surface only.

Include:
- every non-`__init__.py` file under the chosen source root when graph-details
  workflow is enabled for that repository
- example source roots may look like `src/**` or another repo-local runtime
  subtree chosen by the user

Exclude:
- `tests/**`
- examples
- docs/tickets/patch files as graph nodes

## Required Inputs (Read First)
- `context_compass/system_docs/src_architecture.md`
- `context_compass/system_docs/src_components.md`
- `context_compass/system_docs/graph_details_document.md`
- `context_compass/system_docs/readable_src_graph.json`
- `context_compass/examples/example_graph_details/graph_details_document.md`
- `context_compass/examples/example_graph_details/src_graph.expanded.json`
- `context_compass/examples/example_graph_details/src_graph.json`
- `context_compass/examples/example_graph_details/readable_src_graph.json`
- `agent_onboarding/default/engineer/skills/graph_details_readable_generation.md`
- active patch docs for the graph lane when patch gating is active
- active ticket and `context_compass/attention_board.md` route
- if repo-specific system docs do not exist yet, use the example graph-details
  pack as the shape guide and create the graph surfaces only when the user wants
  graph-based durable context

## Unknowns Gate (Non-Negotiable)
- New graph claims default to `UNKNOWN`.
- Promote to graph nodes/edges only when architecture/components evidence is
  strong enough to justify the relationship.
- Do not infer semantic edges from imports or filename shape alone.

## Authoring Contract
The graph is exhaustive for the eligible files inside the chosen repo-specific
scope and semantic about how those files are wired.

Include every eligible source file as a node-bearing graph entry, then enrich
important files with stronger role/responsibility/relationship detail where it
materially improves wiring comprehension.

Explicit exclusion:
- do not create graph nodes for anything under `tests/`
- do not create graph nodes for `__init__.py` files
- package meaning should come from real objects/components/modules, not from
  package marker files

Every node must include:
- `id`
- `label`
- `kind`
- `file`
- `role`
- `responsibilities`
- `owns_state`
- `phases`

Every edge must include:
- `from`
- `to`
- `relation`
- `why`
- `cardinality`
- `phase`
- `strength`

## Expand-Edit-Compress Workflow (Non-Negotiable)
Do not hand-edit the compressed canonical storage file directly.

Required workflow:
1. Read the compressed canonical graph:
   - `context_compass/system_docs/src_graph.json`
2. Expand the full document into one patch-lane working copy:
   - `context_compass/system_docs/patches/active/<patch_id>/src_graph.expanded.json`
3. Edit the expanded whole-document patch copy only.
   - keep `__init__.py` files excluded from graph nodes and edges
4. Validate the expanded JSON.
5. Recompress the whole document back into canonical storage.
6. Regenerate `context_compass/system_docs/readable_src_graph.json` from the
   compressed canonical graph by raw-text reflow at `220` characters.
   - use the PowerShell or Bash recipe from
     `agent_onboarding/default/engineer/skills/graph_details_readable_generation.md`
7. Validate the readable JSON file and the `220`-width contract.

## Build Sequence (Required)
1. Confirm active ticket route and graph scope.
2. Re-read architecture/components docs for the target subsystem.
3. Expand the canonical graph into a patch-lane working copy.
4. Add or update nodes first.
   - only for `src/` objects
5. Add or update semantic edges second.
6. Validate graph JSON and relationship coherence.
7. Recompress and overwrite canonical storage.
8. Regenerate and validate `readable_src_graph.json`.
9. Update any example files that demonstrate the workflow.

## Quality Gate (Pass/Fail)
Pass only when all checks are true:
- [ ] `src_graph.json` is valid JSON after compression.
- [ ] `readable_src_graph.json` is valid JSON after regeneration.
- [ ] `readable_src_graph.json` stays at `220` characters or less per line.
- [ ] the expanded patch copy is valid JSON before recompression.
- [ ] node ids are unique.
- [ ] every edge endpoint exists as a node.
- [ ] relation values remain inside the canonical vocabulary.
- [ ] graph changes do not duplicate long-form prose from architecture/components docs.

## Validation Commands
- `Get-Content context_compass/system_docs/src_graph.json -Raw | ConvertFrom-Json | Out-Null`
- `Get-Content context_compass/system_docs/readable_src_graph.json -Raw | ConvertFrom-Json | Out-Null`
- `Get-Content context_compass/system_docs/patches/active/<patch_id>/src_graph.expanded.json -Raw | ConvertFrom-Json | Out-Null`

## Staleness Triggers (When Update Is Mandatory)
- ownership changes
- creation responsibility changes
- borrowing vs hard lifecycle responsibility changes
- validation/publication/binding relationships change
- architecture/components docs change the canonical wiring story

## Anti-Patterns (Reject)
- editing compressed storage directly
- reading the compressed storage file by line instead of using the readable view
- failing to regenerate `readable_src_graph.json` after graph edits
- adding `tests/` objects into `src_graph.json`
- adding `__init__.py` files as graph nodes
- leaving eligible files inside the chosen graph scope uncovered
- using import-only edges as architecture truth
- duplicating architecture/components prose into the graph
- inventing new edge verbs without intentionally revising the schema

## Handoff Rule
- End graph updates by confirming:
  - what node/edge set changed,
  - what remains intentionally out of scope,
  - and where the next maintainer should expand/edit the graph next.
