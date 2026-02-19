

# src_components_instructions

## Purpose
- Define the exact build protocol for
  `context_compass/system_docs/src_components.md`.
- Produce a bottom-up component contract map (C3/C2/C1) that stays aligned to
  architecture boundaries.

## Canonical Output
- `context_compass/system_docs/src_components.md`

## Example Documents (Required Read)
- `context_compass/examples/example_components/src_components.md`
- `context_compass/examples/example_components/tests_components.md`
- `context_compass/examples/example_architecture/src_architecture.md`
- `context_compass/system_docs/src_components.md` (active baseline)

## Required Inputs (Read First)
- `context_compass/system_docs/src_architecture.md`
- `context_compass/system_docs/tests_components.md`
- `context_compass/system_docs/tests_architecture.md`
- `context_compass/agent_onboarding/default/design_engineer/skills/src_architecture_instructions.md`
- Active ticket and `context_compass/attention_board.md` route

## Unknowns Gate (Non-Negotiable)
- Default to `UNKNOWN` for unevidenced component claims.
- Promote to `FACT` only with direct evidence.
- No behavior inference from naming or folder shape.

## Required Section Contract
`src_components.md` must contain these sections in order:
1. `## Metadata`
2. `## Scope`
3. `## DO NOT ASSUME / Unknowns Gate`
4. `## Unknowns`
5. `## C3 Components Catalog`
6. `## C2 Subcomponents Catalog`
7. `## Method-Level Call Flows (C1)`
8. `## C1 Code Map (Core)`
9. `## Diagrams`
10. `## Information Sources`
11. `## Context / Handoff Summary`

## Component Entry Contract (C3 Minimum)
Each C3 component entry must include:
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
- `Extension Points`
- `Key Files (C1)`

## C1 Flow/Map Contract
- Method-level call flows must include concrete method/function names.
- C1 map entries must include:
  - `path`
  - `start_line`
  - `end_line`
  - `loc`
  - `verified_at` (UTC DateTime)

## Build Sequence (Bottom-Up, Required)
1. Confirm active ticket route and component scope.
2. Read required example documents and note reusable structure patterns.
3. Re-read architecture boundaries and terms.
4. Draft/refresh `Metadata`, `Scope`, `Unknowns Gate`, and `Unknowns`.
5. Build C3 component catalog using the entry contract.
6. Build C2 subcomponent catalog with ownership and wiring.
7. Capture method-level C1 call flows for core paths.
8. Build C1 map entries with ranges, LOC, and verification timestamps.
9. Add/refresh diagrams aligned to catalog terminology.
10. Refresh `Information Sources` and `Context / Handoff Summary`.

If a component claim conflicts with architecture, log `CONFLICT` in ticket
notes and escalate before proceeding.

## Quality Gate (Pass/Fail)
Pass only when all checks are true:
- [ ] Required section order exists and is complete.
- [ ] Every C3 entry includes the minimum contract fields.
- [ ] C1 call flows use concrete method/function names.
- [ ] C1 map entries include path, range, LOC, and verified_at.
- [ ] Architecture terminology and boundaries are consistent.
- [ ] Information Sources support all promoted FACT claims.

## Validation Commands
- `rg -n "^## " context_compass/system_docs/src_components.md`
- `rg -n "C3 Components Catalog|C2 Subcomponents Catalog|Method-Level Call Flows|C1 Code Map" context_compass/system_docs/src_components.md`
- `rg -n "path|start_line|end_line|loc|verified_at" context_compass/system_docs/src_components.md`

## Staleness Triggers (When Update Is Mandatory)
- Component ownership/wiring changed.
- Lifecycle/cleanup ordering changed.
- Core method-level flows changed.
- Architecture boundaries/terms changed.
- C1 ranges became stale from code edits.

## Anti-Patterns (Reject)
- Component summaries without ownership/lifecycle details.
- C1 call flows without concrete methods.
- C1 map entries missing verification fields.
- Architecture mismatch left undocumented.

## Handoff Rule
- End with a concise `Context / Handoff Summary` that states:
  - what component contracts changed,
  - what is still unknown,
  - which subsystem should be verified next.


