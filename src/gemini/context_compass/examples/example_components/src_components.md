# Example src_components (repo-grounded)

## Metadata
- Example type: high-fidelity C3/C2/C1 map
- Objective: demonstrate complete component entries based on this repository
- Last verified at: 2026-02-19T03:15:00Z

## Scope
Provide a concrete component-map example for ticket-first execution using real
files from this package.

## DO NOT ASSUME / Unknowns Gate
- unresolved behavior stays UNKNOWN
- promote claims only with evidence-backed references

## Unknowns
- UNKNOWN: future split of closure-sync responsibilities between docs policy and
  scripted automation.

## C3 Components Catalog
### Component: Router/Role Resolver
- Purpose: map active profile to deterministic role-chain readset.
- Responsibilities: read `SKILLS.md`, resolve role path, enforce parent-first
  chain.
- Inputs: `config/context_compass_config.yaml`, role map in `SKILLS.md`.
- Outputs: ordered `SKILLS.md` read chain.
- Owned State: profile + role map definitions.
- Invariants/Guarantees: deterministic chain order and explicit path mapping.
- Failure Modes: bad mapping path, stale references.
- Key Files (C1): `SKILLS.md`, `config/context_compass_config.yaml`.

### Component: Ticket Microcycle Coordinator
- Purpose: enforce evidence-backed delivery cadence.
- Responsibilities: keep note updates, transition logic, and validation records
  coherent.
- Inputs: active ticket content + findings.
- Outputs: append-only notes and status transitions.
- Owned State: ticket `## Notes` and transition records.
- Invariants/Guarantees: meaningful findings are captured before deeper actions.
- Failure Modes: undocumented decisions and speculative transitions.
- Key Files (C1): `tickets/*`, `templates/task_template.md`, `agent_onboarding/default/general/skills/workflow.md`.

### Component: Artifact Link Coordinator
- Purpose: maintain traceable artifact-to-ticket relationships.
- Responsibilities: keep artifact paths, status, and disposition synchronized.
- Inputs: story/task artifact links and closure decisions.
- Outputs: active/cleared rows in artifact board.
- Owned State: `artifact_board.md` rows.
- Invariants/Guarantees: active artifact always has ticket ownership and
  disposition.
- Failure Modes: orphaned artifact rows, missing disposition.
- Key Files (C1): `artifact_board.md`, `examples/example_completed/*`.

## C2 Subcomponents Catalog
- Router/Role Resolver
  - profile selector
  - role path resolver
  - chain-order reader

- Ticket Microcycle Coordinator
  - note appender
  - transition recorder
  - validation reporter

- Artifact Link Coordinator
  - artifact path linker
  - disposition tracker

## Method-Level Call Flows (C1)
- `resolve_profile() -> resolve_role_path() -> read_inherited_skills()`
- `investigate() -> append_note(FACT/UNKNOWN) -> plan() -> implement() -> validate() -> append_note(result)`
- `link_artifact() -> record_disposition() -> verify_link_on_close()`

## C1 Code Map (Core)
- path: `SKILLS.md`
  start_line: 1
  end_line: 69
  loc: 69
  verified_at: 2026-02-19T03:15:00Z
- path: `templates/task_template.md`
  start_line: 1
  end_line: 103
  loc: 103
  verified_at: 2026-02-19T03:15:00Z
- path: `tickets/tasks/README.md`
  start_line: 1
  end_line: 67
  loc: 67
  verified_at: 2026-02-19T03:15:00Z
- path: `examples/eng_task_flow.md`
  start_line: 1
  end_line: 31
  loc: 31
  verified_at: 2026-02-19T03:15:00Z

## Diagrams
```text
Profile Config -> Skills Resolver -> Active Ticket -> Notes/Transitions -> Closure
```

```mermaid
flowchart LR
  P[Profile Config] --> S[Skills Resolver]
  S --> T[Active Ticket]
  T --> N[Notes + Transitions]
  N --> C[Closure Sync]
```

## Information Sources
- `SKILLS.md`
- `config/context_compass_config.yaml`
- `templates/task_template.md`
- `tickets/tasks/README.md`
- `agent_onboarding/default/general/skills/workflow.md`
- `artifact_board.md`

## Context / Handoff Summary
This example demonstrates expected component-map depth with explicit ownership,
invariants, and file-backed call flow claims.



