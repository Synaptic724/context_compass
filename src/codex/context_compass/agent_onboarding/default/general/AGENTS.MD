

# AGENTS.MD - Default General Baseline Policy

## PRIME DIRECTIVE
Certification is denied unless the resolved SKILLS chain is satisfied exactly.

- You MUST read every path listed under **Active skills** / **Required baseline skills**
  in each resolved `SKILLS.MD` file (parent-first).
- **On-demand** skills are NOT part of baseline certification, but become mandatory
  when triggered by the active task. If triggered, you MUST read them before proceeding.
- You MUST NOT claim a skill was read unless it was actually read.

## Document Intent

This is a high-level reinforcer document that defines behavior expectations for
the general layer.
It reinforces how to operate, communicate, gate work, and preserve context.
It is not a routing manifest and it does not replace skills-map-driven
role-resolution onboarding.

## Inheritance Directive

This general-layer policy inherits root policy from:
`context_compass/AGENTS.MD`

Within the general layer, this `AGENTS.MD` and the general-layer policy docs
(skills, policies, and behavioral guidelines) are mandatory operating policy.
They are not optional references or soft suggestions.

## Non-Negotiables

### 1) Unknowns Gate (No Unverified Claims)

Rule: No Unverified Claims. Any statement not supported by evidence is UNKNOWN.
UNKNOWN is the default stance for any new claim until evidence is attached.

Evidence means at least one of:

* A specific source file reference (preferred: file + symbol/method/class name).
* A citation to an explicit, already-verified artifact (e.g., a prior approved doc section).

If not evidenced => UNKNOWN.

UNKNOWN items must be labeled UNKNOWN (or added to an Unknowns section).
UNKNOWN items must be investigated by reading the relevant source(s).
If investigation cannot be completed (missing source access, ambiguity, or time),
the item must remain UNKNOWN and must not be promoted to fact.

No reasonable assumptions.
Do not infer behavior from naming, patterns, conventions, or typical frameworks.
Only the code/docs count.

When unsure:

* Mark it UNKNOWN.
* Identify the most likely evidence target (file + symbol).
* Investigate, then update the doc (or leave it UNKNOWN).

## Operating Protocol (How You Should Work)

### 2) Propose -> Confirm -> Implement

Before making non-trivial edits:

1. Restate the goal in **3-5 bullets**.
2. List the constraints you will obey.
3. List the **exact files / symbols** you will modify.

If any of the above is uncertain, **stop and ask** before editing.
For this repo, treat **all** edits as requiring explicit confirmation, even if they seem trivial.

### 3) Scope Control

* Stay within the declared files/symbols.
* If you believe the change requires touching more than the declared scope, **ask first**.

### 4) Documentation Ritual

As a ritual, after implementing a change:

* Re-read the sections you touched.
* Improve clarity and completeness.
* Ensure they match the intended behavior exactly.

### 5) Question-First Clarity

* If anything is unclear or uncertain, investigate briefly and then stop and ask.
* Prefer asking clarifying questions over making assumptions.
* Keep me updated on intent, progress, and blockers.

### 6) context_compass Ticket Planning (Required)

* Before starting any planned work beyond answering questions, create a structured ticket (epic/story/task) in `tickets/epics/`, `tickets/stories/`, or `tickets/tasks/` using `templates/`.
* Treat `attention_board.md` as routing-only state and the active ticket `## Notes` section as canonical durable execution memory.
* Hard execution gate (mandatory):
  - Do not implement or validate unless an active ticket exists for the work.
  - Do not implement or validate unless `attention_board.md` has an active row routing to that ticket.
  - Do not start a new investigation tranche, code edit tranche, or validation tranche until the current meaningful finding is written in ticket `## Notes` with evidence.
  - If any gate above is missing, stop and repair ticket/board/notes state before continuing.
* Default every new claim to `UNKNOWN` until source evidence proves otherwise.
* Ticket Microcycle enforcement defaults to strict and is configurable in `config/context_compass_config.yaml`.
* Follow a strict Ticket Microcycle while working:
  1. Route from `attention_board.md` to one active ticket.
  2. Investigate until one meaningful finding (fact, blocker, decision, measure, or hypothesis worth testing).
  3. Immediately append a `## Notes` entry before any further investigation.
  4. Continue only after the note includes evidence and a concrete next step.
* If `workflow.ticket_microcycle.enabled` is `false`, use relaxed mode:
  - still document each meaningful finding,
  - still update notes before implementation and validation,
  - still require evidence for `FACT` and `DECISION` claims.
* No second investigation tranche is allowed before documenting the current meaningful finding in the ticket.
* Do not implement from `UNKNOWN` or `HYPOTHESIS`; promote to `FACT` or `DECISION` with evidence first.
* If investigation must expand beyond the current subsystem or exceed
  `workflow.ticket_microcycle.expansion_gate_max_files` in one pass, append a
  `DECISION` note and ask the user for scope confirmation before continuing.
* Follow `SKILLS.MD` and
  `agent_onboarding/default/general/skills/workflow.md` for the deep
  descriptive format and tracking model.
* The ticket must define scope, steps, and intended deliverables; share it and wait for approval.
* Maintain a `## Notes` section in active tickets and append in-flight findings with `path:start_line-end_line` evidence pointers as they occur, not in end-of-pass batches.
* Evidence ranges in notes must include both start and end lines. If the evidence is one line, repeat it (`path:42-42`).
* New note entries must include a compaction usefulness score
  (`SCORE_0_TO_10`); if score is below
  `workflow.ticket_microcycle.minimum_note_score`, improve the note before
  proceeding.
* Before closing any ticket, walk through what was achieved and ask if the acceptance criteria are met.
* Only after explicit confirmation, move the ticket(s) to the matching completed folder
  (`tickets/epics/completed/`, `tickets/stories/completed/`, `tickets/tasks/completed/`) with a short summary and date (per `README.md`).
* Immediately after moving any ticket to a completed folder, run deterministic `attention_board.md` sync:
  - remove/replace active rows that reference the closed ticket,
  - prune stale attention details tied only to the closed ticket,
  - add one compact closed-anchor row,
  - cap closed anchors by dropping oldest rows first.

### 7) Context Compaction Policy (Required)

* Before context compaction or major handoff, follow `agent_onboarding/default/general/skills/context_compaction.md`.
* Treat `agent_onboarding/default/general/skills/compaction_requirements.md` as the mandatory re-entry checklist.
* Ensure active tickets have up-to-date `Notes` sections with evidence-backed findings.
* Ensure active tickets have up-to-date \"Context / Handoff Summary\" sections.
* After context compaction or a fresh session, re-read
  `agent_onboarding/default/new/skills/first_time_profile_setup.md`.

## Stop Conditions (Ask Before Proceeding)

Ask for explicit confirmation if any of these are true:

* You want to touch **many files** (repo-wide sweeps) and no codemod approach was approved.
* You want to rename/move files or symbols.
* You want to introduce new dependencies or tooling.
* You want to change formatting across files.

---

## General Directory Coverage Contract

This section defines why the general layer matters.
It does not define read order or routing; that belongs to `SKILLS.MD` and
resolved role `SKILLS.MD` files.

### 8) Importance Of General Layer Policies

- It is the cross-profile behavior baseline that keeps execution consistent.
- It enforces evidence-first reasoning and blocks assumption-driven claims.
- It defines ticket-first execution so work is durable and resumable.
- It preserves context through active notes, board routing, and compaction flow.
- It enforces explicit approval gates before meaningful execution.
- It sets escalation discipline for scope/risk changes.
- It keeps security posture strict, especially around secret handling.
- It preserves process quality across handoffs and context resets.

### 9) What Must Be Internalized From General

- Durable execution memory:
  active findings belong in ticket notes, not transient chat context.
- Execution gating:
  no implementation/validation without ticket + routing + notes coherence.
- Controlled scope:
  no silent expansions, no hidden multi-file drift.
- Re-entry reliability:
  compaction is expected; re-onboarding and state reconstruction are mandatory.
- Professional collaboration posture:
  direct, explicit, and conflict-aware communication with evidence.

### 10) Enforcement Reminder

General policy is not optional glue text.
It is the operating baseline for all inheriting profiles.
If behavior in lower layers conflicts with this layer, resolve the conflict
explicitly instead of bypassing general rules.

### 11) Why These Behaviors Exist

- They prevent drift between intent, execution, and recorded state.
- They force decisions to be evidence-backed instead of memory-backed.
- They keep work resumable after interruption, handoff, or compaction.
- They reduce silent failure modes caused by skipped gates.

### 12) General Failure Patterns To Avoid

- Acting before scope and approval are explicit.
- Continuing investigation without recording the current meaningful finding.
- Treating board state and ticket state as optional or interchangeable.
- Promoting weak assumptions into facts under time pressure.
- Allowing completion state to diverge from actual acceptance.

### 13) Expected Operator Discipline

- Keep one active problem boundary at a time.
- Make each transition explicit (investigate, decide, implement, validate).
- Keep uncertainty visible until it is resolved with evidence.
- Surface blockers early with concrete impact and next-step asks.
- Preserve a clean audit trail through notes and state transitions.

### 14) Continuity Standard

General policy is designed so another reader can restart execution from files
without replaying prior chat history.
If a future reader cannot resume safely from ticket + board + notes, the
current state is incomplete and must be repaired before continuing.








