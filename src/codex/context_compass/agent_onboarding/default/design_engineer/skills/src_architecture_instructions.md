

# src_architecture_instructions

## Purpose
- Define the exact build protocol for
  `context_compass/system_docs/src_architecture.md`.
- Produce a durable C4 architecture document that is re-entry safe after
  compaction.

## Canonical Output
- `context_compass/system_docs/src_architecture.md`

## Example Documents (Required Read)
- `context_compass/examples/example_architecture/src_architecture.md`
- `context_compass/examples/example_components/src_components.md`
- `context_compass/examples/example_components/tests_components.md`
- `context_compass/system_docs/src_architecture.md` (active baseline)

## Required Inputs (Read First)
- `context_compass/system_docs/src_components.md`
- `context_compass/system_docs/tests_architecture.md`
- `context_compass/system_docs/tests_components.md`
- `context_compass/agent_onboarding/default/design_engineer/skills/src_components_instructions.md`
- Active ticket and `context_compass/attention_board.md` route

## Unknowns Gate (Non-Negotiable)
- New claims start as `UNKNOWN`.
- Promote to `FACT` only with direct evidence.
- Evidence must be concrete code/doc references, not naming inference.

## Required Section Contract
`src_architecture.md` must contain these sections in order:
1. `## Metadata`
2. `## Scope and Intent`
3. `## DO NOT ASSUME / Unknowns Gate`
4. `## Unknowns`
5. `## System Context (C4)`
6. `## System Boundary and External Interfaces`
7. `## Architecture Summary (C4)`
8. `## Entrypoints and Runtime Guardrails`
9. `## Boot and Configuration Sequence`
10. `## Data Flows and Sequences`
11. `## Operational Invariants`
12. `## Failure Modes and Error Paths`
13. `## C1 Code Map (Core Only)`
14. `## Diagrams`
15. `## Information Sources`
16. `## Context / Handoff Summary`

## C1 Code Map Contract
Every C1 entry must include:
- `path`
- `start_line`
- `end_line`
- `loc`
- `verified_at` (UTC DateTime `YYYY-MM-DDTHH:MM:SSZ`)

If exact range is not verified, keep claim `UNKNOWN` and add an investigation
target in `## Unknowns`.

## Diagram Contract
- Include one ASCII architecture diagram.
- Include one Mermaid architecture diagram.
- Keep labels operational (ownership, flow, boundary), not decorative.
- Keep diagram terms aligned with section terminology.

## Build Sequence (Top-Down, Required)
1. Confirm active ticket route and architecture scope.
2. Read required example documents and note formatting patterns to preserve.
3. Re-read companion component/test docs for boundary alignment.
4. Draft/refresh `Metadata`, `Scope and Intent`, and Unknowns sections.
5. Define system boundary, interfaces, and high-level runtime summary.
6. Write entrypoints and boot/configuration sequence.
7. Write data-flow sequences (normal path and failure path).
8. Capture invariants and failure modes with source evidence.
9. Build C1 core map with line ranges, LOC, and verification timestamps.
10. Refresh diagrams to match narrative and naming.
11. Refresh `Information Sources` and `Context / Handoff Summary`.

Do not skip sequence order. If blocked, write a `BLOCKER` note in the active
ticket before expanding scope.

## Quality Gate (Pass/Fail)
Pass only when all checks are true:
- [ ] Required section order exists and is complete.
- [ ] Unknowns are explicit and carry investigation targets.
- [ ] Boundary/interfaces and boot sequence are concrete and testable.
- [ ] C1 entries include path, range, LOC, and verified_at.
- [ ] Diagrams match written flow and use aligned terminology.
- [ ] Information Sources cover every promoted FACT.

## Validation Commands
- `rg -n "^## " context_compass/system_docs/src_architecture.md`
- `rg -n "UNKNOWN|C1 Code Map|Information Sources|Context / Handoff Summary" context_compass/system_docs/src_architecture.md`
- `rg -n "path|start_line|end_line|loc|verified_at" context_compass/system_docs/src_architecture.md`

## Staleness Triggers (When Update Is Mandatory)
- Boundary or integration contracts changed.
- Boot/configuration ordering changed.
- Invariants/failure modes changed.
- C1 line ranges became stale from code edits.
- `src_components.md` introduces term/boundary changes.

## Anti-Patterns (Reject)
- Placeholder claims without evidence.
- C1 map entries without ranges/LOC/verified_at.
- Diagrams that do not match section content.
- Mixing component-level deep dives into architecture sections.

## Handoff Rule
- End with a concise `Context / Handoff Summary` that states:
  - what changed,
  - what remains unknown,
  - where the next reader should start.


