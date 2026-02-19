# Example src_architecture

## Metadata
- Example only; demonstrates expected section contract.

## Scope and Intent
Show how to document C4 architecture for a file-backed execution system.

## DO NOT ASSUME / Unknowns Gate
Promote UNKNOWN to FACT only with direct evidence.

## Unknowns
- UNKNOWN: future runtime adapter abstraction strategy.

## System Context (C4)
Context Compass coordinates policy onboarding, role routing, and ticket memory.

## System Boundary and External Interfaces
- Entrypoints: `AGENTS.MD`, `GEMINI.MD`
- Router: `config/context_compass_config.yaml`, `SKILLS.md`
- Durable state: `attention_board.md`, `tickets/`, `artifact_board.md`

## Architecture Summary (C4)
- bootstrap policy layer
- role routing layer
- durable work-memory layer
- artifact lifecycle layer

## Entrypoints and Runtime Guardrails
No edits/tools before onboarding and certification gates complete.

## Boot and Configuration Sequence
1. Read entrypoint policy.
2. Read config and top-level skills map.
3. Resolve role chain.
4. Request certification.

## Data Flows and Sequences
User request -> ticket routing -> note capture -> implementation -> validation.

## Operational Invariants
- Unknowns stay explicit until proven.
- Ticket notes remain canonical in-flight memory.

## Failure Modes and Error Paths
- stale references
- missing role mapping
- missing certification gate

## C1 Code Map (Core Only)
- path: `config/context_compass_config.yaml`
  start_line: 1
  end_line: 140
  loc: 140
  verified_at: 2026-02-19T00:00:00Z
- path: `SKILLS.md`
  start_line: 1
  end_line: 90
  loc: 90
  verified_at: 2026-02-19T00:00:00Z

## Diagrams
ASCII
```text
Entrypoint -> Router -> Role Chain -> Tickets -> Artifacts
```

Mermaid
```mermaid
flowchart LR
  E[Entrypoint] --> R[Router]
  R --> C[Role Chain]
  C --> T[Tickets]
  T --> A[Artifacts]
```

## Information Sources
- `AGENTS.MD`
- `GEMINI.MD`
- `config/context_compass_config.yaml`
- `SKILLS.md`

## Context / Handoff Summary
Use this file as a structure reference when producing real architecture docs.