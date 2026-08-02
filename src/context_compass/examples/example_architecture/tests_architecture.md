# Example tests_architecture (repo-grounded)

## Metadata
- Example type: high-fidelity tests architecture example
- Objective: show what a strong tests architecture document looks like when
  based on real repository files
- Last verified at: 2026-08-01T16:16:14Z

## Scope and Intent
This example demonstrates the test-side mirror of `src_architecture.md`. It uses
this repository's actual testing skills, QA role docs, and ticket lanes rather
than invented surfaces.

The two documents are a matched pair. `src_architecture.md` describes how the
runtime is structured; this one describes how that structure is verified. They
share a section contract so a reader who knows one can navigate the other
without relearning anything.

## Indexing

This document is authored. Its only generated companion is `tests_architecture_index.md`,
rebuilt in the same pass as any edit:

```bash
python context_compass/tools/system_documents/index_document.py \
    --doc context_compass/examples/example_architecture/tests_architecture.md
```

That command indexes THIS example, and it works - run it and compare the
output to the `tests_architecture_index.md` beside it. When you write your own, the
target becomes `context_compass/system_docs/tests_architecture.md`, which does not exist
until you create it: the package ships `system_docs/` empty.

Format rules the index depends on, demonstrated throughout this example:
- exactly one H1 (the document title)
- the navigable unit is H2 `## <Concern>`, at consistent depth
- section names unique and stable - index rows are selected by name
- container headings organise, but are never the read target: a heading wrapping
  only other headings indexes as a range covering all of them

Spec: `agent_onboarding/default/engineer/skills/system_document_build.md`

## DO NOT ASSUME / Unknowns Gate
- Keep unresolved test claims marked UNKNOWN.
- A test that has never run is not evidence. Promote to FACT only when the run
  produced output you read.

## Unknowns
- UNKNOWN: whether contract checks over policy documents should run in CI or
  stay a release-hardening step.
- UNKNOWN: the boundary between component and integration suites for
  documentation-shaped systems.

## System Context (C4)
Testing here validates a document-backed system, so most surfaces are
structural rather than behavioural: references resolve, section contracts hold,
role chains are reachable, and evidence ranges match the files they cite.

## System Boundary and External Interfaces
- Test posture and strategy: `agent_onboarding/default/qa_engineer/skills/`
- Document contracts under test: `agent_onboarding/default/design_engineer/skills/`
- Evidence lanes: `tickets/`, active ticket `## Notes`
- Index tooling: `tools/system_documents/index_document.py`

## Architecture Summary (C4)
- reference-integrity checks over the routing graph
- section-contract checks over system documents
- index staleness checks against the documents they describe
- evidence-quality checks on cited line ranges

## Entrypoints and Runtime Guardrails
- a check that cannot fail is not a check
- findings carry `path:start_line-end_line`, never a bare assertion
- a stale index is a hard stop, not a rounding error

## Boot and Configuration Sequence
1. Resolve the role chain to know which documents are in scope.
2. Recompute each index's staleness proof before slicing anything.
3. Run reference resolution over the resolved readset.
4. Compare section contracts against the spec.
5. Record findings in the active ticket with file evidence.

## Data Flows and Sequences
- authoring change -> index rebuild -> checks -> evidence in ticket notes
- compaction -> re-onboard -> re-verify stale assumptions -> resume

## Operational Invariants
- every readset path resolves, or onboarding is blocked
- every index matches `line_count`, `line_ending`, and `content_sha256`
- every cited range is measured, never estimated

## Failure Modes and Error Paths
- a checker whose pattern is too narrow reports a clean sweep over a subset
- an index regenerated before the document is edited, so the proof passes and
  the ranges lie
- ranges copied forward from an earlier revision without remeasuring

## C1 Code Map (Core Only)
- path: `agent_onboarding/default/qa_engineer/skills/test_case_design.md`
  start_line: 1
  end_line: 27
  loc: 27
  verified_at: 2026-08-01T16:16:14Z
- path: `agent_onboarding/default/qa_engineer/skills/test_automation_practices.md`
  start_line: 1
  end_line: 30
  loc: 30
  verified_at: 2026-08-01T16:16:14Z
- path: `agent_onboarding/default/qa_engineer/skills/test_strategy_and_planning.md`
  start_line: 1
  end_line: 31
  loc: 31
  verified_at: 2026-08-01T16:16:14Z
- path: `agent_onboarding/default/qa_engineer/skills/regression_and_release_quality.md`
  start_line: 1
  end_line: 28
  loc: 28
  verified_at: 2026-08-01T16:16:14Z
- path: `tickets/tasks/README.md`
  start_line: 1
  end_line: 67
  loc: 67
  verified_at: 2026-08-01T16:16:14Z

## Diagrams
```text
Docs Change -> Index Rebuild -> Checks -> Evidence -> Ticket Notes
```

```mermaid
flowchart LR
  D[Docs Change] --> I[Index Rebuild]
  I --> C[Reference + Contract Checks]
  C --> E[Evidence with Line Ranges]
  E --> N[Ticket Notes]
```

## Information Sources
- `agent_onboarding/default/qa_engineer/skills/test_case_design.md`
- `agent_onboarding/default/qa_engineer/skills/test_strategy_and_planning.md`
- `tickets/tasks/README.md`
- `agent_onboarding/default/engineer/skills/system_document_build.md`

## Context / Handoff Summary
This example shows the expected depth standard for the test-side map: concrete
surfaces, explicit unknowns, and measured line ranges. It pairs with
`examples/example_architecture/src_architecture.md`; read them together to see how the
runtime map and its verification map stay structurally aligned.
