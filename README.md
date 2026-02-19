# Context Compass

Context Compass is a policy-driven context orchestrator for long-running
AI-assisted work.

It gives agents a deterministic way to:
- onboard correctly,
- route work through durable artifacts,
- enforce evidence and quality gates,
- survive compaction without losing the plot,
- recover across new chats, handoffs, and context resets.

At its core, this is a robust documentation system for active execution:
- `attention_board.md` for routing,
- ticket lanes for durable work state,
- structured notes for evidence-backed reasoning,
- artifact indexing for output lifecycle control.

This project exists for people who are done with fragile, one-thread memory
workflows and want execution that holds up under real pressure.

---

## What This System Actually Is

Context Compass is not a one-shot prompt and not a chat style guide.
It is a process control layer for agent behavior.

It defines:
- authority order and policy precedence,
- role selection and inheritance,
- baseline vs on-demand skill activation,
- certification gates before edits/tools,
- ticket-first execution and note contracts,
- compaction and re-onboarding recovery behavior.

Core idea:
- chat memory is volatile,
- repository state is durable,
- process should be recoverable from files, not vibes.

---

## Why Teams Use It

Most AI execution failures are process failures:
- onboarding gets skipped or faked,
- assumptions get promoted to facts,
- important decisions stay in chat and disappear,
- compaction wipes key context,
- handoffs lose ownership and next actions.

Context Compass fixes that by making each stage explicit and auditable.

What improves:
- less drift,
- clearer role boundaries,
- stronger handoff quality,
- better continuity over long projects,
- fewer "what were we doing?" resets.

---

## Runtime Support

Context Compass supports Codex and Gemini runtime setups.

Canonical split runtime layout:
- `src/codex/context_compass/AGENTS.MD`
- `src/gemini/context_compass/GEMINI.MD`

In this layout:
- policy mechanics stay the same,
- role map and skill chain behavior stay the same,
- compaction and re-onboarding behavior stay the same.

Runtime-specific entrypoint filename is the only required difference.

---

## High-Level Flow

Every work cycle follows the same operating model.

1. Bootstrap policy
- Entry file loads authoritative policy.
- Agent aligns before action.

2. Resolve role chain
- Role selected from `SKILLS.MD` map + config.
- Parent-first inheritance is enforced.
- Required baseline skills are mandatory.
- On-demand skills activate only by trigger.

3. Complete onboarding gate
- Agent reads required chain.
- Agent posts integrity attestation.
- User must approve certification token before edits/tools.

4. Execute through tickets
- Active routing happens in `attention_board.md`.
- Durable technical context lives in active tickets.
- Findings are logged in structured notes with evidence pointers.

5. Handle compaction safely
- Re-onboarding is mandatory after compaction/handoff.
- Agent reopens policy + active work state.
- Re-certifies before resuming execution.

---

## Core Features

### 1) Compaction Durability

The system treats compaction as a reliability event, not a convenience step.

Key behavior:
- post-compaction action is blocked until re-onboarding is complete,
- attestation requires read-integrity proof,
- active board + active tickets must be reopened,
- claims must be anchored to current source/docs, not memory.

Practical effect:
- less continuity loss,
- fewer false "I remember" claims,
- cleaner restart across compressed contexts.

### 2) Multi-Chat Durability

Context lives in files:
- `attention_board.md` for routing,
- active ticket `## Notes` for in-flight findings,
- ticket context/handoff sections for state continuity,
- `artifact_board.md` for artifact lifecycle indexing.

New thread recovery becomes deterministic:
- open board,
- follow active ticket links,
- continue from latest evidence-backed notes and next actions.

### 3) Strict Re-Onboarding Contract

After compaction/handoff:
- re-read policy anchors,
- resolve and read role chain again,
- post `REONBOARD: COMPLETE` with integrity proof,
- request `CERTIFY: APPROVED`,
- only then continue execution.

This closes the door on performative compliance and policy theater.

### 4) Evidence + Unknowns Gate

Default claim state is `UNKNOWN` until evidence exists.

Promotion to `FACT` requires direct evidence pointers.
Inference by naming pattern is explicitly rejected as proof.

Result:
- fewer confident mistakes,
- better traceability,
- stronger review quality.

### 5) Ticket Microcycle

Strict loop:
- Investigate -> Document -> Strategy/Plan -> Document ->
  Implement -> Document -> Validate -> Document

Notes are not optional side output.
They are core execution memory and compaction fuel.

### 6) Baseline vs On-Demand Skills

Each role can define:
- required baseline skills (always needed),
- on-demand skills (triggered by task scope).

This keeps onboarding enforceable while still allowing deep specialization.

### 7) User-Defined Role Overlays

Custom profiles can extend defaults without forking core behavior.

Typical pattern:
- inherit from `engineer` or `general`,
- add domain-specific policy/behavior/skill deltas,
- keep parent baselines intact.

---

## Repository Anatomy

Primary control files:
- `context_compass/AGENTS.MD`
- `context_compass/SKILLS.MD`
- `context_compass/CONTEXT_COMPACTION.md`
- `context_compass/config/context_compass_config.yaml`
- `context_compass/attention_board.md`
- `context_compass/artifact_board.md`

Role and policy tree:
- `context_compass/agent_onboarding/default/...`
- `context_compass/agent_onboarding/user_defined/...`

Execution artifacts:
- `context_compass/tickets/epics/`
- `context_compass/tickets/stories/`
- `context_compass/tickets/tasks/`
- `context_compass/templates/`
- `context_compass/artifacts/`

System-context docs (when used):
- `context_compass/system_docs/src_architecture.md`
- `context_compass/system_docs/src_components.md`
- `context_compass/system_docs/tests_architecture.md`
- `context_compass/system_docs/tests_components.md`

---

## Role Model

### Shared Foundation
- `general`

### Software Roles
- `engineer`
- `design_engineer`
- `platform_engineer`
- `qa_engineer`
- `security_engineer`

### Fiction Workflow Roles
- `story_designer`
- `story_novel_artist`
- `researcher`
- `draft_writer`
- `developmental_editor`
- `line_copy_editor`
- `continuity_fact_checker`
- `proofreader`

### User-Defined
- `user_defined/<profile_name>`
- example included: `synaptic_python_developer`

---

## Setup Guide

### Step 1: Place Context Compass in your repo

Use split runtime trees:
- `src/codex/context_compass/...`
- `src/gemini/context_compass/...`

### Step 2: Confirm runtime entrypoints

For Codex:
- `src/codex/context_compass/AGENTS.MD`

For Gemini:
- `src/gemini/context_compass/GEMINI.MD`

### Step 3: Configure active profile

Edit:
- `context_compass/config/context_compass_config.yaml`

Set:
- `profiles.active_profile`

Validate:
- `profiles.available_profiles`
- `router.roles.<profile>`

### Step 4: Start onboarding

Boot sequence:
- read runtime entrypoint policy,
- read config,
- read top-level `SKILLS.MD`,
- resolve role chain,
- read baseline skills in parent-first order.

### Step 5: Certify before action

Before edits/tools:
- publish onboarding attestation,
- request exact approval token:
  - `CERTIFY: APPROVED`

No token, no implementation.

### Step 6: Run ticket-first

Always route through:
- `attention_board.md` active row,
- linked active ticket.

Capture meaningful findings in ticket notes with evidence pointers.

### Step 7: Treat compaction as gated re-entry

After compaction/handoff:
- re-onboard,
- post re-attestation with read-integrity proof,
- re-certify,
- resume only after gates pass.

---

## Configuration Model (YAML)

Main config:
- `context_compass/config/context_compass_config.yaml`

Key sections:
- `profiles.*`
  - active profile,
  - available profiles,
  - first-time onboarding behavior.
- `router.*`
  - role map to `SKILLS.MD` paths,
  - README routing policy.
- `workflow.*`
  - ticket microcycle strictness,
  - ticket contract gates,
  - note behavior requirements.
- `artifacts.*`
  - artifact root,
  - board path,
  - cleanup/disposition policy.
- `documentation_format.*`
  - line-length and evidence formatting standards.
- `codex.*`
  - read limits and chunking thresholds.

This lets teams tune behavior without rewriting the policy stack.

---

## Ticketing and Documentation Contracts

This is not lightweight "notes when convenient" documentation.
This is an always-on execution memory system.

Ticket types:
- Epic: cross-cutting initiative,
- Story: medium slice with multiple tasks,
- Task: smallest concrete deliverable.

Each active ticket should carry:
- ticket contract,
- state transition events,
- acceptance criteria,
- risks/mitigations,
- notes with evidence and next action,
- handoff summary.

Notes schema supports types such as:
- `FACT`, `UNKNOWN`, `HYPOTHESIS`,
- `DECISION`, `DECISION_REQUEST`,
- `PLAN`, `BLOCKER`, `RISK`, `MEASURE`, and others.

Core rule:
- no unevidenced claim promoted to fact.

Operational rule:
- every meaningful finding is documented before the next tranche continues.

---

## Board Design

### `attention_board.md`

Purpose:
- routing only,
- active status/mode/blocker/next/outcome,
- ticket linkage and re-read priority.

Not for:
- long narrative,
- deep analysis,
- artifact file indexing.

### `artifact_board.md`

Purpose:
- active artifact associations by ticket,
- disposition and cleanup tracking,
- recently cleared artifact history.

Allowed dispositions:
- `delete_on_close`
- `retain_as_reference`
- `promote_to_documentation`

---

## Compaction and Re-Entry Deep Dive

Compaction strategy:
- external memory first,
- keep compaction summary empty when runtime allows,
- if not possible, keep only minimal pointer summary.

Pre-compaction discipline:
- board must be current,
- active ticket notes and handoff state must be current,
- unresolved unknowns and blockers must be explicit.

Post-compaction discipline:
- mandatory re-onboarding,
- mandatory integrity attestation,
- mandatory re-certification,
- no implementation before gates are complete.

This is where the system gets its durability.

---

## User-Defined Role Inheritance Model

Use user-defined overlays when a team needs local conventions.

Pattern:
1. Create profile under:
   - `context_compass/agent_onboarding/user_defined/<name>/`
2. Create profile `SKILLS.MD`.
3. Set inheritance header:
   - `INHERITS_SKILLS_FROM: <parent path>`
4. Add only deltas (no parent duplication).
5. Register role in YAML router/profile lists.
6. Activate and validate onboarding chain.

Guidance file:
- `context_compass/PROFILE_CLASS_CREATION_GUIDE.md`

---

## What Good Operation Looks Like

A healthy run usually has these signals:
- active board row maps cleanly to one active ticket,
- ticket notes are current and evidence-backed,
- unknowns are explicit, not buried,
- transitions are documented,
- certification gate is respected,
- compaction recovery is deterministic.

If those hold, drift stays low.

---

## Common Failure Modes This System Prevents

- "Agent started coding before onboarding."
- "Agent claimed it read docs but could not explain behavior impact."
- "Critical decisions vanished after compaction."
- "New chat had no reliable re-entry path."
- "Role responsibilities got blurred and quality gates vanished."

Context Compass exists to make those failure modes non-default.

---

## Practical Adoption Strategy

Recommended rollout:

1. Start with `general` + `engineer`.
2. Enforce board + ticket routing first.
3. Enforce unknowns/evidence discipline.
4. Enforce certification and compaction re-entry gates.
5. Add specialized roles as workflow matures.
6. Add user-defined overlays after baseline behavior is stable.

This sequence keeps adoption fast without weakening core controls.

---

## Final Word

Context Compass is built for serious, long-running AI execution.

If your goal is:
- fewer resets,
- less drift,
- stronger handoffs,
- cleaner ownership,
- and context that survives compaction,

this system is designed for exactly that.

Policy-driven, role-aware, and durable by design.
