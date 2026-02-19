# Example src_components

## Metadata
- Example only; demonstrates C3/C2/C1 component mapping format.

## Scope
Map major components in the execution workflow.

## DO NOT ASSUME / Unknowns Gate
Unevidenced claims remain UNKNOWN.

## Unknowns
- UNKNOWN: future split of policy vs automation code ownership.

## C3 Components Catalog
### Runtime policy entrypoint
- Purpose: enforce bootstrap contract.
- Responsibilities: onboarding and certification gates.
- Inputs: user request, session state.
- Outputs: deterministic allowed action set.
- Owned State: none.
- Lifecycle/Cleanup: re-read on compaction/handoff.
- Concurrency/Threading: single-session sequencing.
- Invariants/Guarantees: no action before gate completion.
- Failure Modes: stale entrypoint references.
- Observability: attestation messages.
- Extension Points: runtime-specific adapter files.
- Key Files (C1): `AGENTS.MD`, `GEMINI.MD`.

## C2 Subcomponents Catalog
- profile router
- role skill chain
- ticket memory stream

## Method-Level Call Flows (C1)
- `bootstrap -> read_entrypoint -> read_config -> resolve_role`
- `execute -> append_note -> implement -> validate`

## C1 Code Map (Core)
- path: `SKILLS.md`
  start_line: 1
  end_line: 90
  loc: 90
  verified_at: 2026-02-19T00:00:00Z
- path: `attention_board.md`
  start_line: 1
  end_line: 160
  loc: 160
  verified_at: 2026-02-19T00:00:00Z

## Diagrams
```text
Policy -> Router -> Ticket Memory
```

```mermaid
flowchart LR
  P[Policy] --> R[Router]
  R --> T[Ticket Memory]
```

## Information Sources
- `AGENTS.MD`/`GEMINI.MD`
- `config/context_compass_config.yaml`
- `SKILLS.md`

## Context / Handoff Summary
Use this as a format guide for real component docs.