# Example tests_components

## Metadata
- Example only; demonstrates tests component mapping format.

## Scope
Map key test-validation components for workflow integrity.

## Indexing

This document is authored. Its only generated companion is `tests_components_index.md`,
rebuilt in the same pass as any edit:

```bash
python context_compass/tools/system_documents/index_document.py \
    --doc context_compass/examples/example_components/tests_components.md
```

That command indexes THIS example, and it works - run it and compare the
output to the `tests_components_index.md` beside it. When you write your own, the
target becomes `context_compass/system_docs/tests_components.md`, which does not exist
until you create it: the package ships `system_docs/` empty.

Format rules the index depends on, demonstrated throughout this example:
- exactly one H1 (the document title)
- the navigable unit is H3 `### Component: <Name>`, at consistent depth
- section names unique and stable - index rows are selected by name
- container headings organise, but are never the read target: a heading wrapping
  only other headings indexes as a range covering all of them

Spec: `agent_onboarding/default/engineer/skills/system_document_build.md`

## DO NOT ASSUME / Unknowns Gate
Keep unresolved test assumptions as UNKNOWN.

## Unknowns
- UNKNOWN: final CI matrix for multi-runtime validation.

## C3 Components Catalog
### Component: Reference Integrity Scanner
- Purpose: detect broken internal references.
- Responsibilities: scan docs and resolve paths.
- Inputs: markdown/yaml files.
- Outputs: missing reference findings.
- Owned State: scan report.
- Lifecycle/Cleanup: run on release hardening.
- Concurrency/Threading: serial scan pass.
- Invariants/Guarantees: findings include file references.
- Failure Modes: false negatives from incomplete patterns. A pattern narrower
  than the file set it claims to cover reports a clean sweep over a subset,
  which is worse than reporting nothing.
- Observability: ticket validation notes.
- Extension Points: new reference shapes extend the resolver's match set; the
  finding format stays fixed so downstream triage does not change.
- Key Files (C1): `tickets/*/README.md`, `templates/*.md`.

## C2 Subcomponents Catalog
- path resolver
- missing-target reporter
- severity triage layer

## Method-Level Call Flows (C1)
- `scan_files -> resolve_targets -> emit_findings`
- `triage_findings -> gate_release`

## C1 Code Map (Core)
- path: `examples/example_graph_details/src/example/core/resource.py`
  start_line: 1
  end_line: 15
  loc: 15
  verified_at: 2026-08-01T16:16:14Z
- path: `examples/example_graph_details/src/example/storage/store.py`
  start_line: 1
  end_line: 20
  loc: 20
  verified_at: 2026-08-01T16:16:14Z

## Diagrams
```text
Docs -> Scanner -> Findings -> Release Gate
```

```mermaid
flowchart LR
  D[Docs] --> S[Scanner]
  S --> F[Findings]
  F --> G[Release Gate]
```

## Information Sources
- `templates/*.md`
- `tickets/*/README.md`
- `agent_onboarding/default/qa_engineer/skills/*`

## Context / Handoff Summary
Use this structure when mapping real test components.