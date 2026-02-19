

# tests_architecture_instructions

## Purpose
- Define the exact build protocol for
  `context_compass/system_docs/tests_architecture.md`.
- Turn test-architecture docs from placeholder state into evidence-led C4
  system context.

## Canonical Output
- `context_compass/system_docs/tests_architecture.md`

## Example Documents (Required Read)
- `context_compass/examples/example_architecture/src_architecture.md`
- `context_compass/examples/example_components/tests_components.md`
- `context_compass/examples/example_components/src_components.md`
- `context_compass/system_docs/tests_architecture.md` (active baseline)

## Required Inputs (Read First)
- `context_compass/system_docs/tests_components.md`
- `context_compass/system_docs/src_architecture.md`
- `context_compass/system_docs/src_components.md`
- `context_compass/agent_onboarding/default/design_engineer/skills/tests_components_instructions.md`
- Active ticket and `context_compass/attention_board.md` route

## Unknowns Gate (Non-Negotiable)
- Start unknown-heavy and explicit.
- Promote to `FACT` only when direct evidence is captured.
- If evidence is incomplete, keep `UNKNOWN` and list investigation targets.

## Required Section Contract
`tests_architecture.md` must contain these sections in order:
1. `## Metadata`
2. `## Scope and Intent`
3. `## DO NOT ASSUME / Unknowns Gate`
4. `## Unknowns`
5. `## System Context (C4)`
6. `## External Interfaces and Entry Points`
7. `## Core Responsibilities`
8. `## Data Flows and Lifecycle`
9. `## Invariants and Guarantees`
10. `## C1 Code Map (Key Paths)`
11. `## Diagrams`
12. `## Information Sources`
13. `## Context / Handoff Summary`

## Discovery-First Build Sequence (Required)
1. Confirm active ticket route and test-system scope.
2. Read required example documents and extract reusable C4 section patterns.
3. Inventory test entry surfaces (`tests/`, runner config, fixtures).
4. Capture unknowns before promoting any architecture claims.
5. Define C4 boundaries and external interfaces.
6. Document lifecycle flow (setup, execution, teardown) with evidence.
7. Capture invariants and failure paths observed in sources.
8. Build C1 key-path map with ranges, LOC, and verification timestamps.
9. Add ASCII + Mermaid diagrams aligned to written flow.
10. Refresh `Information Sources` and `Context / Handoff Summary`.

## C1 Map Contract
Each C1 key-path entry must include:
- `path`
- `start_line`
- `end_line`
- `loc`
- `verified_at` (UTC DateTime)

## Quality Gate (Pass/Fail)
Pass only when all checks are true:
- [ ] Required section order exists and is complete.
- [ ] Unknowns are explicit and tied to investigation targets.
- [ ] Interfaces, lifecycle, and invariants are evidence-backed.
- [ ] C1 map entries include path, range, LOC, and verified_at.
- [ ] Diagrams and narrative use consistent terms.

## Validation Commands
- `rg -n "^## " context_compass/system_docs/tests_architecture.md`
- `rg -n "UNKNOWN|System Context|Data Flows|C1 Code Map|Information Sources" context_compass/system_docs/tests_architecture.md`
- `rg -n "path|start_line|end_line|loc|verified_at" context_compass/system_docs/tests_architecture.md`

## Staleness Triggers (When Update Is Mandatory)
- Test runner/configuration behavior changed.
- Fixture lifecycle behavior changed.
- Test boundary/interfaces changed.
- C1 ranges became stale from test-file edits.

## Anti-Patterns (Reject)
- Generic "tests do X" statements without evidence.
- Missing unknown inventory in partially mapped docs.
- C1 map entries without verification fields.
- Copying src architecture claims into tests architecture without proof.

## Handoff Rule
- End with `Context / Handoff Summary` covering:
  - evidence-backed state,
  - unresolved unknowns,
  - next discovery target.


