# Example src_architecture (repo-grounded)

## Metadata
- Example type: high-fidelity architecture example
- Objective: show what a strong architecture document looks like when based on
  real repository files
- Last verified at: 2026-08-01T16:16:14Z

## Scope and Intent
This example demonstrates a credible C4 architecture narrative for Context
Compass using this repo's actual entrypoints, routing files, ticket lanes, and
board state files.

## Indexing

This document is authored. Its only generated companion is `src_architecture_index.md`,
rebuilt in the same pass as any edit:

```bash
python context_compass/tools/system_documents/index_document.py \
    --doc context_compass/examples/example_architecture/src_architecture.md
```

That command indexes THIS example, and it works - run it and compare the
output to the `src_architecture_index.md` beside it. When you write your own, the
target becomes `context_compass/system_docs/src_architecture.md`, which does not exist
until you create it: the package ships `system_docs/` empty.

Format rules the index depends on, demonstrated throughout this example:
- exactly one H1 (the document title)
- the navigable unit is H2 `## <Concern>`, at consistent depth
- section names unique and stable - index rows are selected by name
- container headings organise, but are never the read target: a heading wrapping
  only other headings indexes as a range covering all of them

Spec: `agent_onboarding/default/engineer/skills/system_document_build.md`

## DO NOT ASSUME / Unknowns Gate
- Keep unresolved claims marked UNKNOWN.
- Promote to FACT only with file evidence.

## Unknowns
- UNKNOWN: whether automated path/reference scanning will be part of the default
  release checklist.
- UNKNOWN: whether artifact retention defaults should differ by lane.

## System Context (C4)
Context Compass turns volatile chat context into durable, file-backed execution
state through policy bootstrap, role routing, and ticket-first notes.

## System Boundary and External Interfaces
- Entrypoints: `AGENTS.MD`
- Router/config: `SKILLS.MD`, `config/context_compass_config.yaml`
- Work memory: `attention_board.md`, `tickets/`
- Artifact memory: `artifact_board.md`, `artifacts/`

## Architecture Summary (C4)
- bootstrap/guardrails
- role-chain routing
- ticket microcycle execution
- closure and compaction continuity

## Entrypoints and Runtime Guardrails
- mandatory onboarding/certification before work
- parent-first role-chain reads
- explicit re-onboarding after compaction/handoff

## Boot and Configuration Sequence
1. Read runtime entrypoint.
2. Read execution contract and compaction policy.
3. Read config + top-level skills map.
4. Resolve and read role chain.
5. Route to active ticket.
6. Execute microcycle and document findings.

## Data Flows and Sequences
- request -> routing -> ticket loop -> validation -> closure sync
- compaction -> re-onboarding -> recertify -> resume

## Operational Invariants
- ticket notes are canonical in-flight memory
- UNKNOWN never becomes FACT without evidence
- sample assets stay in `examples/` lanes

## Failure Modes and Error Paths
- broken references
- stale attention-board pointer
- missing artifact disposition

## C1 Code Map (Core Only)
- path: `SKILLS.MD`
  start_line: 1
  end_line: 108
  loc: 108
  verified_at: 2026-08-01T16:16:14Z
- path: `config/context_compass_config.yaml`
  start_line: 1
  end_line: 101
  loc: 101
  verified_at: 2026-08-01T16:16:14Z
- path: `attention_board.md`
  start_line: 1
  end_line: 57
  loc: 57
  verified_at: 2026-08-01T16:16:14Z
- path: `artifact_board.md`
  start_line: 1
  end_line: 54
  loc: 54
  verified_at: 2026-08-01T16:16:14Z

## Diagrams
```text
Entrypoint -> Config/Skills -> Role Chain -> Ticket Loop -> Closure/Compaction
```

```mermaid
flowchart LR
  E[Entrypoint] --> R[Config + Skills]
  R --> C[Role Chain]
  C --> T[Ticket Loop]
  T --> H[Closure + Compaction Recovery]
```

## Information Sources
- `AGENTS.MD`

- `SKILLS.MD`
- `config/context_compass_config.yaml`
- `agent_onboarding/default/general/skills/workflow.md`

## Context / Handoff Summary
This example shows the expected depth standard: concrete boundaries, explicit
invariants, and repo-backed references.


