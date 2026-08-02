# Example src_components (repo-grounded)

## Metadata
- Example type: high-fidelity C3/C2/C1 map
- Objective: demonstrate complete component entries based on this repository
- Last verified at: 2026-08-01T16:16:14Z

## Scope
Provide a concrete component-map example for ticket-first execution using real
files from this package.

## Indexing

This document is authored. Its only generated companion is `src_components_index.md`,
rebuilt in the same pass as any edit:

```bash
python context_compass/tools/system_documents/index_document.py \
    --doc context_compass/examples/example_components/src_components.md
```

That command indexes THIS example, and it works - run it and compare the
output to the `src_components_index.md` beside it. When you write your own, the
target becomes `context_compass/system_docs/src_components.md`, which does not exist
until you create it: the package ships `system_docs/` empty.

Format rules the index depends on, demonstrated throughout this example:
- exactly one H1 (the document title)
- the navigable unit is H3 `### Component: <Name>`, at consistent depth
- section names unique and stable - index rows are selected by name
- container headings organise, but are never the read target: a heading wrapping
  only other headings indexes as a range covering all of them

Spec: `agent_onboarding/default/engineer/skills/system_document_build.md`

## DO NOT ASSUME / Unknowns Gate
- unresolved behavior stays UNKNOWN
- promote claims only with evidence-backed references

## Unknowns
- UNKNOWN: future split of closure-sync responsibilities between docs policy and
  scripted automation.

## C3 Components Catalog
### Component: Router/Role Resolver
- Purpose: map the selected role to a deterministic role-chain readset.
- Responsibilities: read `SKILLS.MD`, resolve role path, enforce parent-first
  chain.
- Inputs: the registry table in `SKILLS.MD`.
- Outputs: ordered `SKILLS.MD` read chain.
- Owned State: none. The registry table in `SKILLS.MD` is the state;
  `config/context_compass_config.yaml` enumerates no roles.
- Lifecycle/Cleanup: resolved once per agent per session; nothing persists
  between sessions, so there is no state to clean up.
- Concurrency/Threading: read-only resolution, safe under concurrent agents.
  Role selection is per agent, so two agents resolving different roles in the
  same repository do not contend.
- Invariants/Guarantees: deterministic chain order and explicit path mapping.
- Failure Modes: bad mapping path, stale references.
- Observability: the resolved chain is stated in the onboarding attestation.
- Extension Points: add a role by adding one registry row and the `SKILLS.MD`
  it names; no resolver change is required.
- Key Files (C1): `SKILLS.MD`, `config/context_compass_config.yaml`.

### Component: Ticket Microcycle Coordinator
- Purpose: enforce evidence-backed delivery cadence.
- Responsibilities: keep note updates, transition logic, and validation records
  coherent.
- Inputs: active ticket content + findings.
- Outputs: append-only notes and status transitions.
- Owned State: ticket `## Notes` and transition records.
- Lifecycle/Cleanup: spans one ticket, from route to closure; on closure the
  ticket moves to its `completed/` lane rather than being deleted.
- Concurrency/Threading: single-writer per ticket. Two agents on one ticket is
  a coordination failure, not a supported mode.
- Invariants/Guarantees: meaningful findings are captured before deeper actions.
- Failure Modes: undocumented decisions and speculative transitions.
- Observability: note timestamps and transition records in the ticket itself.
- Extension Points: the microcycle phases are named in `workflow.md`; a lane
  with extra phases extends that list rather than forking the coordinator.
- Key Files (C1): `tickets/*`, `templates/task_template.md`, `agent_onboarding/default/general/skills/workflow.md`.

### Component: Artifact Link Coordinator
- Purpose: maintain traceable artifact-to-ticket relationships.
- Responsibilities: keep artifact paths, status, and disposition synchronized.
- Inputs: story/task artifact links and closure decisions.
- Outputs: active/cleared rows in artifact board.
- Owned State: `artifact_board.md` rows.
- Lifecycle/Cleanup: a row lives from artifact creation to disposition at
  ticket closure; cleared rows stay as history.
- Concurrency/Threading: append-oriented board writes; concurrent edits to the
  same row require ticket-level coordination.
- Invariants/Guarantees: active artifact always has ticket ownership and
  disposition.
- Failure Modes: orphaned artifact rows, missing disposition.
- Observability: the active/cleared split on the board is the status surface.
- Extension Points: new artifact classes add a disposition rule; the row shape
  stays fixed.
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
- path: `SKILLS.MD`
  start_line: 1
  end_line: 108
  loc: 108
  verified_at: 2026-08-01T16:16:14Z
- path: `templates/task_template.md`
  start_line: 1
  end_line: 111
  loc: 111
  verified_at: 2026-08-01T16:16:14Z
- path: `tickets/tasks/README.md`
  start_line: 1
  end_line: 67
  loc: 67
  verified_at: 2026-08-01T16:16:14Z
- path: `examples/eng_task_flow.md`
  start_line: 1
  end_line: 31
  loc: 31
  verified_at: 2026-08-01T16:16:14Z

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
- `SKILLS.MD`
- `config/context_compass_config.yaml`
- `templates/task_template.md`
- `tickets/tasks/README.md`
- `agent_onboarding/default/general/skills/workflow.md`
- `artifact_board.md`

## Context / Handoff Summary
This example demonstrates expected component-map depth with explicit ownership,
invariants, and file-backed call flow claims.



