

# Documentation Standards (Skill)

## Purpose
Architecture and components docs must be deep enough to reorient from a blank slate
without relying on memory, oral tradition, or "obvious" assumptions.

These standards exist so *agents* (human or AI) can safely extend the system without inventing behavior.

## Non-Negotiables (Hardlines)
- **No handwaving.** Every claim must be grounded in source evidence or marked as **UNKNOWN**.
- **Explicit entrypoints and flows.** If it's core behavior, show how it is entered and how it executes.
- **Ownership + lifecycle clarity.** Who creates it, who owns it, how it is cleaned up, and in what order.
- **Concurrency is first-class.** Document locks, queues, gates, thread-affinity rules, and failure modes.
- **Consistency across layers.** C4 architecture and C3/C2/C1 components must not contradict.
- **Diagrams are required.** Maintain ASCII + Mermaid for key flows.

## Core Rules
- No handwaving. Every claim must be grounded in source evidence or marked as unknown.
- Use explicit entrypoints, flows, and ownership boundaries.
- Record lifecycle and cleanup order for each core component.
- Capture invariants, failure modes, and concurrency constraints.
- Keep C4 (architecture) and C3/C2/C1 (components) consistent.
- Maintain ASCII and Mermaid diagrams for key flows.

## Evidence Discipline
What counts as evidence:
- A concrete file + symbol reference: `src/path/file.py:Class.method` or `src/path/file.py:function`
- A reference to a previously approved doc section that was itself code-grounded

What **does not** count as evidence:
- "Typical framework behavior"
- "Probably"
- Naming conventions, patterns, or vibes

### Required behavior when evidence is missing
- Write **UNKNOWN** explicitly.
- Add the item to an **Unknowns** section with:
  - why it matters,
  - where to investigate (file + symbol),
  - and status (uninvestigated / investigating / blocked).

### Inline evidence style (recommended)
Use one of these patterns inside the text:
- `EVIDENCE: src/.../file.py:Symbol`
- `UNKNOWN: ... (investigate src/.../file.py:Symbol)`

## Required Sections

### Architecture Docs (C4)
Required sections (minimum):
- Scope and Intent
- System Context and Boundaries
- Entrypoints and Boot Sequence
- Major component responsibilities and interactions
- Ownership, lifecycle, and cleanup rules
- Invariants and failure modes
- Evidence and information sources

Strongly recommended additions:
- Operational playbook (bring-up + teardown)
- Troubleshooting section (common failure modes -> where to look)
- Diagram legend (how to interpret optional vs core subsystems)

### Component Docs (C3/C2/C1)
Required sections (minimum):
- C3 components with responsibilities and contracts
- C2 subcomponents with wiring and data structures
- C1 code map for entrypoints and core files
- Method-level call flows for core behaviors
- Wiring tables / registry keys for runtime lookups

Strongly recommended additions:
- Registry "quick reference" for common string keys and defaults
- Ownership matrix (who owns what; who may call what)
- Cleanup cascade (parent -> child teardown order)

### Patch Docs (Temporary, When Patch Lane Is Active)
Required minimums for patch docs under `system_docs/patches/active/<patch_id>/`:
- `architecture_patch.md`: objective/non-goals, changed components, invariants,
  interface deltas, migration order, rollback, ticket coverage matrix.
- `component_patch_<component>.md`: before/after behavior, interface deltas,
  state/failure deltas, dependency/ordering, validation expectations.
- `code_description_patch_<component>.md` (conditional): control flow,
  edge/error semantics, invariants/idempotency, explicit non-goals.

Gate rule
- For system-impacting work, implementation should not start until required
  patch docs exist and are linked from the active ticket.

## Metadata & Status (If Present)
When a doc includes a Metadata block:
- Update the `Updated:` date whenever you change behavior descriptions.
- Keep `Status:` honest (draft / current / deprecated).
- If the doc is a "durable context" artifact, prefer **append-only enrichment** over rewriting history.

## Diagram Standards
- Provide **ASCII** for terminal scanning and diffs.
- Provide **Mermaid** for higher fidelity.
- Label edges with verbs when it improves clarity (e.g., "creates", "owns", "enqueues").
- Show optional subsystems with dashed arrows/edges.
- Don't let diagrams become "art": clarity > completeness.

## Consistency Rules (Across Docs)
- Names and terms should match across C4 and C3/C2/C1 docs (e.g., "Spectrum", "CommandCenter", etc.).
- If you rename a component, update:
  - component catalog,
  - diagrams,
  - wiring tables,
  - and code map references.

## Review Checklist (Before You Call It "Current")
- [ ] No unverified claims (or they are marked UNKNOWN)
- [ ] Core flows have method-level call sequences
- [ ] Ownership/lifecycle/cleanup ordering is explicit
- [ ] Concurrency constraints are called out where relevant
- [ ] ASCII + Mermaid diagrams reflect the written description
- [ ] Information Sources list includes every file used as evidence

