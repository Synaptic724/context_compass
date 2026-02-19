

# tests_components_instructions

## Purpose
- Define the exact build protocol for
  `context_compass/system_docs/tests_components.md`.
- Produce evidence-backed C3/C2/C1 test component mapping aligned to test
  architecture boundaries.

## Canonical Output
- `context_compass/system_docs/tests_components.md`

## Example Documents (Required Read)
- `context_compass/examples/example_components/tests_components.md`
- `context_compass/examples/example_components/src_components.md`
- `context_compass/examples/example_architecture/src_architecture.md`
- `context_compass/system_docs/tests_components.md` (active baseline)

## Required Inputs (Read First)
- `context_compass/system_docs/tests_architecture.md`
- `context_compass/system_docs/src_architecture.md`
- `context_compass/system_docs/src_components.md`
- `context_compass/agent_onboarding/default/design_engineer/skills/tests_architecture_instructions.md`
- Active ticket and `context_compass/attention_board.md` route

## Unknowns Gate (Non-Negotiable)
- New component claims default to `UNKNOWN`.
- Promote to `FACT` only with concrete evidence.
- Preserve unresolved UNKNOWNs; do not normalize into assumptions.

## Required Section Contract
`tests_components.md` must contain these sections in order:
1. `## Metadata`
2. `## Scope`
3. `## DO NOT ASSUME / Unknowns Gate`
4. `## Unknowns`
5. `## C3 Components Catalog`
6. `## C2 Subcomponents Catalog`
7. `## Method-Level Call Flows (C1)`
8. `## C1 Code Map (Key Paths)`
9. `## Diagrams`
10. `## Information Sources`
11. `## Context / Handoff Summary`

## Test Component Entry Contract (C3 Minimum)
Each C3 test component must include:
- `Purpose`
- `Responsibilities`
- `Inputs`
- `Outputs`
- `Owned State`
- `Lifecycle/Cleanup`
- `Concurrency/Threading`
- `Invariants/Guarantees`
- `Failure Modes`
- `Observability`
- `Key Files (C1)`

## C1 Flow/Map Contract
- Call-flow entries must include concrete test methods/functions/fixtures.
- C1 map entries must include:
  - `path`
  - `start_line`
  - `end_line`
  - `loc`
  - `verified_at` (UTC DateTime)

## Build Sequence (Bottom-Up, Required)
1. Confirm active ticket route and test component scope.
2. Read required example documents and extract reusable C3/C2/C1 patterns.
3. Re-read tests architecture boundaries and terminology.
4. Draft/refresh metadata, scope, unknowns gate, and unknowns inventory.
5. Build C3 test component catalog with entry-contract fields.
6. Build C2 subcomponents and wiring/dependency notes.
7. Capture method-level C1 flows (fixtures, harnesses, execution paths).
8. Build C1 key-path map with ranges, LOC, and verification timestamps.
9. Add diagrams aligned to terminology and flow.
10. Refresh `Information Sources` and `Context / Handoff Summary`.

## Quality Gate (Pass/Fail)
Pass only when all checks are true:
- [ ] Required section order exists and is complete.
- [ ] Every C3 entry includes the minimum contract fields.
- [ ] C1 call flows include concrete methods/functions/fixtures.
- [ ] C1 map entries include path, range, LOC, and verified_at.
- [ ] Terminology aligns with `tests_architecture.md`.
- [ ] Information Sources support promoted FACT claims.

## Validation Commands
- `rg -n "^## " context_compass/system_docs/tests_components.md`
- `rg -n "C3 Components|C2 Subcomponents|Method-Level Call Flows|C1 Code Map" context_compass/system_docs/tests_components.md`
- `rg -n "path|start_line|end_line|loc|verified_at" context_compass/system_docs/tests_components.md`

## Staleness Triggers (When Update Is Mandatory)
- Test component ownership/wiring changed.
- Fixture or harness lifecycle changed.
- Method-level test flow changed.
- C1 ranges became stale from test-file edits.

## Anti-Patterns (Reject)
- Test component entries without lifecycle/ownership detail.
- C1 call flows with generic statements and no concrete symbols.
- C1 map entries missing verification fields.
- Divergence from tests architecture terminology without escalation.

## Handoff Rule
- End with `Context / Handoff Summary` that states:
  - what component mapping is verified,
  - what remains unknown,
  - which test subsystem should be mapped next.


