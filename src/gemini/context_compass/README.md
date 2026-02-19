# Context Compass

Context Compass is a policy-first operating system for AI-assisted execution.
It gives agents a deterministic way to onboard, route work, preserve context,
and recover cleanly after compaction or session reset.

This repository is built as a public library. You can use it directly, fork it,
or adapt it to your own role stack and process requirements.

## What This Project Is

Context Compass is not a prompt snippet and not a one-shot template.
It is a file-backed coordination system that defines:

- how an agent should read policy,
- how a role is selected and resolved,
- how work must be routed through tickets,
- how evidence is captured while work is in motion,
- and how continuity is preserved across interruptions.

The goal is practical reliability: less agent drift, better state continuity,
and auditable execution quality.

## What It Solves

Most failures in long AI sessions are process failures:

- policy gets partially remembered,
- onboarding claims drift from what was actually read,
- execution starts without durable state,
- and compaction wipes critical context.

Context Compass addresses that by making execution contract-driven:

- onboarding is explicit,
- role resolution is explicit,
- certification is explicit,
- ticket routing is explicit,
- compaction re-entry is explicit.

## Agent Support

This Gemini distribution is wired to a single runtime entrypoint.

Select the correct folder and place it into your repo.

Within Context Compass Gemini support:

- Gemini entrypoint: `GEMINI.MD`

The routing and policy core remains shared.
This distribution uses `GEMINI.MD` as the only runtime entrypoint.

## Core Design Principles

1. Evidence before assertion.
2. Deterministic gates before execution.
3. Durable state in files, not chat memory.
4. Parent-first role inheritance.
5. Re-onboarding after compaction/handoff.
6. Explicit uncertainty (`UNKNOWN`) over silent guessing.

## Repository Structure

```text
context_compass/
  GEMINI.MD
  SKILLS.md
  CONTEXT_COMPACTION.md
  PROFILE_CLASS_CREATION_GUIDE.md
  README.md

  config/
    context_compass_config.yaml

  agent_onboarding/
    default/
      new/
      general/
      engineer/
      design_engineer/
      platform_engineer/
      qa_engineer/
      security_engineer/
      story_designer/
      story_novel_artist/
      researcher/
      draft_writer/
      developmental_editor/
      line_copy_editor/
      continuity_fact_checker/
      proofreader/
    user_defined/
      synaptic_python_developer/

  tickets/
    epics/
    stories/
    tasks/

  templates/
  examples/
  system_docs/
  artifacts/

  attention_board.md
  artifact_board.md
```

## How It Works

### 1) Policy Bootstrap

The agent starts from the runtime entrypoint:

- Gemini reads `GEMINI.MD` and resolves directly into the shared policy chain.

### 2) Role Routing

`SKILLS.md` defines available roles and role-to-skill-map paths.
The selected role resolves to a `SKILLS.md` chain with parent-first inheritance.

Each role declares:

- required baseline skills (must read),
- and on-demand skills (read when trigger conditions apply).

### 3) Certification Gate

Before implementation:

- onboarding must be complete,
- read-integrity must be attested,
- and user approval must include `CERTIFY: APPROVED`.

### 4) Ticket-First Execution

Work is routed through:

- `attention_board.md` for active pointer routing,
- `tickets/` for durable execution memory,
- `artifact_board.md` for linked outputs.

The active ticket `## Notes` is the canonical memory stream for findings,
decisions, blockers, and evidence.

### 5) Compaction / Re-Entry

After compaction, handoff, or a new session:

- re-onboard using the same routing authority,
- rebuild context from board + ticket state,
- and re-certify before resuming action.

This prevents "performative compliance" and keeps behavior auditable.

## Role Model

Context Compass currently includes both software and fiction workflows.

### Software Lane

- `general`
- `engineer`
- `design_engineer`
- `platform_engineer`
- `qa_engineer`
- `security_engineer`

### Fiction Authoring Lane

- `story_designer`
- `story_novel_artist`
- `researcher`
- `draft_writer`
- `developmental_editor`
- `line_copy_editor`
- `continuity_fact_checker`
- `proofreader`

### User-Defined Lane

- `user_defined/<name>` overlays for team or personal specialization

## Configuration Authority

Primary runtime config lives in:

- `config/context_compass_config.yaml`

Key sections include:

- `profiles` for active/allowed profile control,
- `router` for role-to-skill-map mapping,
- `workflow` for ticket microcycle behavior,
- `artifacts` for artifact retention rules,
- `codex` for read-window and chunking limits.

## Quick Start

1. Place `context_compass/` in your repository.
2. Ensure the Gemini runtime entrypoint exists:
   - Gemini: `GEMINI.MD`
3. Select an active profile in `config/context_compass_config.yaml`.
4. Start onboarding through `SKILLS.md` role resolution.
5. Request `CERTIFY: APPROVED`.
6. Execute through ticket routing (`attention_board.md` + active ticket notes).

## Why Teams Use This

- Reproducible agent behavior across sessions.
- Explicit role specialization without policy fragmentation.
- Better handoffs and lower context-loss cost.
- Clear evidence trails for decisions and changes.
- Portable model across agent runtimes.

## Recommended Operating Discipline

- Keep role docs as delta layers (do not duplicate parent skills).
- Keep ticket notes high-signal and evidence-backed.
- Keep board rows routing-focused and concise.
- Treat compaction as a reliability event, not a convenience event.
- Prefer explicit blocker states over hidden assumptions.

## Public Library Intent

Context Compass is intended to be reusable by:

- solo builders,
- engineering teams,
- hybrid technical + creative workflows,
- and multi-agent pipelines that require deterministic process control.

If you extend this library, keep your routing manifest, role maps, and
certification gates explicit so downstream users inherit a stable system.

## License

MIT


