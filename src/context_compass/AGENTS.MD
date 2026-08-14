

# AGENTS.MD - Prime Policies
## Execution Order

- Before running tools, editing files, or executing commands, complete
  onboarding from `context_compass/AGENTS.MD`.
- If there is any conflict between repository-root `AGENTS.MD` and
  `context_compass/AGENTS.MD`, `context_compass/AGENTS.MD` is authoritative.

## Tooling Mandate: Context Compass Is the Only System of Record

### Who this binds

This rule binds you by what your runtime PROVIDES, not by who built it. No brand
is named because no brand needs to be: if your environment gives you any of the
surfaces below, you are in scope.

You are in scope if you are:
- a command-line coding agent,
- an agent embedded in an editor or IDE,
- a desktop or chat agent application with file and shell access,
- a headless agent built on an SDK or API,
- a browser-driving agent,
- an agent running in CI or on a schedule,
- or any other automated runtime acting on this repository.

You are in scope if your runtime exposes any of:
- task lists, todo lists, or checklists
- plans, goals, or planning widgets
- status indicators, progress trackers, or work summaries
- scratchpads, memory panes, or session memory
- any other session-local coordination surface

**If you are reading this and unsure whether a surface of yours counts, it
counts.** The test is not what the feature is called. The test is whether it
holds state about the work that lives outside this repository.

### Hard rules

- You are NOT PERMITTED to use your harness's task system - task lists, todo or
  status widgets, planning trackers, session memory - to plan, track, route, or
  record your work.
- You MUST use `context_compass` as your primary and authoritative tool in ALL of
  its forms: `tickets/epics/`, `tickets/stories/`, `tickets/tasks/`,
  `attention_board.md`, ticket `## Notes`, `artifact_board.md` + `artifacts/`,
  `context_management/`, and `mailbox_board.md`.
- You are NOT PERMITTED to use harness tracking to override, replace, shadow, or
  mirror `context_compass`. There is NO fallback and NO mirror: `context_compass`
  is the ONLY tracking, routing, and memory system. Do not keep a parallel or
  backup copy of work state in harness tooling at all.

### The one exception

The user may turn this off. Set in `config/context_compass_config.yaml`:

- `system_of_record.enforce: false`

When it is `false`, harness-native tracking is permitted and this section does
not bind you. That is the ONLY way this rule is lifted.

**You do not get to lift it yourself.** Not because a task is small, not because
the harness prompted you, not because writing a ticket felt like overhead, and
not because you judged the work too trivial to record. If the key says `true`,
the rule holds. If you think it should be `false` for this repository, say so and
let the user decide.

### Why this is the default

- **Harness tracking is invisible to every other agent.** Another agent working
  this repository cannot see your task list, your status, or a finding you left
  only in chat. `context_compass` surfaces are shared files - every agent reads
  the same state.
- **Harness state cannot be handed over.** `context_compass` writes are files in
  the repository, so the project owner can review them, and any agent in any
  later session can resume from them. Harness session state is lost when the
  session ends, and it cannot be moved into the repository afterwards.
- So harness tracking is strictly less visible and non-durable. Using it in place
  of `context_compass` costs cross-agent visibility and the ability to resume the
  work later. That trade is the user's to make, not yours.

If a write to `context_compass` is blocked (for example, a repository or encoding
problem), STOP and report it. Do NOT silently fall back to harness-only tracking.

## Onboarding Directive

- Project-specific instructions live in `context_compass/special_instructions/`,
  not in this file. This file ships with the library; those do not.
- Once you have found the execution contract you must adhere to it fully.
- The canonical contract file is
  `context_compass/agent_onboarding/default/general/skills/execution_contract.md`.
- Policy gates are non-negotiable.
  - Do NOT offer "options" that bypass onboarding, re-onboarding, certification,
    required reads, or tool-use restrictions.
  - If a required step cannot be completed, state `BLOCKED` and ask the user
    for instructions. Do not improvise a different compliance regime.
  - Do NOT propose rewriting policy, reducing the readset, or changing certification criteria
    as a workaround unless the user explicitly requests policy changes.
- If you are new to this repository (or this is a fresh session), onboard
  before doing any work.
- Onboarding is single-pass per trigger event. Do not restart onboarding in the
  same uninterrupted session unless a new trigger event occurs.
- Read and follow `context_compass/AGENTS.MD` as the canonical onboarding and
  execution policy.
- You MUST determine whether a file exceeds `reading.read_loc_max` LOC before reading it.
  - If the file might exceed `reading.read_loc_max`, compute the line count (LOC) first.
  - If the file is clearly <= `reading.read_loc_max`, do NOT waste tool calls on LOC counting.
- You must read every required **baseline** onboarding file completely.
  - Do not skip required-baseline files.
  - Do NOT claim a file was read unless it was actually read.
  - On-demand files are required only when the active task triggers them.
- Loop-based document reads are forbidden except for line counts. Content reads
  must be manual per file path.
- Files larger than `reading.read_loc_max` LOC must be read in sequential chunks
  with each read operation at or below `reading.viewer_tool_read_limit`.
- Repository-root `AGENTS.MD` is a pointer only. The canonical onboarding and
  execution policy lives in `context_compass/AGENTS.MD`, and that file wins on
  any conflict.

## Compaction Directive

- Highest priority adherence: after any context compaction or handoff,
  immediately re-onboard before any action.
- Re-read `context_compass/AGENTS.MD` and
  `context_compass/agent_onboarding/default/general/skills/compaction_requirements.md`
  before continuing work.
- For compaction/handoff summaries, you MUST keep summaries empty when the runtime allows it;
  otherwise you MUST use minimal file-pointer summaries only.
- Post a `REONBOARD: COMPLETE` attestation **with read-integrity proof** before any
  action. One canonical format, defined once in
  `agent_onboarding/default/general/skills/compaction_requirements.md`
  ("Attestation format"). It is a ~10-line summary: proof is one line per LAYER of
  the chain, not one per document.

## Highest Priority Adherence (Compaction Re-Onboarding)

After any context compaction or handoff:

- Stop and re-onboard before any tooling, edits, execution, or planning.
- Re-onboarding is single-pass per trigger event. Do not repeat the same
  `AGENTS.MD` + `execution_contract.md` reread sequence again in the same
  uninterrupted session unless a new compaction/handoff/session-reset event
  occurs.
- Re-onboarding is reserved for compaction/handoff recovery only.
- Fresh-session startup uses ONBOARD flow, not REONBOARD flow.
- Re-read `agent_onboarding/default/general/skills/execution_contract.md` in
  full immediately after `AGENTS.MD`.
- Start from `config/context_compass_config.yaml`, then `SKILLS.MD`.
- Re-read and follow every Markdown document in `context_compass/special_instructions/` using relative repo paths only.
- Re-read `agent_onboarding/default/general/skills/compaction_requirements.md`.
- RE-READ `context_compass/mailbox_board.md` - the roster and any messages
  addressed to you. Update your row and consume those messages as your FIRST
  action after re-certification, not before it: both are writes, and the
  pre-certification carve-out covers reads only. Per
  `agent_onboarding/default/general/skills/mailbox_protocol.md`.
- README reads are allowed for `new` first-time onboarding only; non-`new`
  roles use policy/skills docs.
- Re-certify with a message that includes:
  - `AGENT_NAME: <name>`
  - the exact phrase `CERTIFY: APPROVED`
  before acting.
- If anything is unclear after re-onboarding, ask the user for instructions and
  get confirmation before acting.
- During compaction/handoff summarization, you MUST keep summaries empty when allowed;
  otherwise you MUST emit minimal file-pointer summaries only.
- Before any action, publish a Re-Onboarding Attestation message with:
  - the canonical attestation from
    `agent_onboarding/default/general/skills/compaction_requirements.md`
    ("Attestation format"), with `REONBOARD: COMPLETE` as the first token and
    `FILES_REREAD` populated.
  - Do not invent a longer variant. The format is a ~10-line summary and the field
    list lives in exactly one file so the copies cannot drift apart.

Performative compliance is forbidden during re-onboarding:

- marker-only loops (for example, `$null = Get-Content ...` plus `REREAD:`
  output) do not count as re-reading
- parallel/bulk reading is allowed only when document contents are actually read
- onboarding claims are valid only when required source documents were actually
  read
- onboarding dump files are non-canonical artifacts and do not satisfy
  onboarding requirements

## Onboarding Gate (Required)

Before any tooling, edits, or execution:

- Read `agent_onboarding/default/general/skills/execution_contract.md` in full
  immediately after `AGENTS.MD`.
- Do not perform duplicate end-of-onboarding rereads of `AGENTS.MD` or
  `execution_contract.md` in the same uninterrupted session.
- Read `config/context_compass_config.yaml`.
- Read `SKILLS.MD`.
- Read and follow every Markdown document in `context_compass/special_instructions/` using relative repo paths only.
- READ `context_compass/mailbox_board.md` - the checked-in roster and any messages
  addressed to you. Reading is permitted before certification; **writing is not.**
- Do NOT write your check-in row yet. The check-in is a WRITE, the pre-certification
  carve-out below covers reads only, and the row requires an `AGENT_NAME` that does
  not exist until the user supplies it with `CERTIFY: APPROVED`. Check in as your
  FIRST action after certification, per
  `agent_onboarding/default/general/skills/mailbox_protocol.md`.
- When `SKILLS.MD` is read, list the roles in its registry table and ask the
  user which role to take on unless the user already selected one explicitly.
- Resolve the selected role to its `SKILLS.MD` path from the `SKILLS.MD`
  registry table. `SKILLS.MD` is the single role registry;
  `config/context_compass_config.yaml` does not enumerate roles.
- Read the selected role `SKILLS.MD` and all inherited parent `SKILLS.MD`
  files in parent-first order, walking each file's `INHERITS_SKILLS_FROM`
  header.
- Treat every path in every section a resolved `SKILLS.MD` marks as **baseline**
  as an active skill doc, and read all of them.
  - **The test is the label, not the heading.** Roles name their baseline
    sections differently - **Active skills**, **Required baseline skills**,
    **Baseline system orientation** - and a role may introduce another. Read
    what the role marks baseline; do not match against a fixed list of headings.
  - Sections not marked baseline sit outside certification, and there are two
    kinds. **On-demand** states a trigger: those paths become mandatory once it
    fires, and MUST be read before any work in that scope. **Self-directed** has
    no trigger at all: read those at your own initiative whenever the work needs
    them, without asking permission.
  - **Do not treat Self-directed as On-demand-with-no-trigger-yet.** That reading
    produces an agent that never opens the document, and it has already happened.
- If first-time onboarding is active and selected role is `new`, complete
  onboarding then set:
  - `profiles.onboarding.first_time_enabled: false`
- Performative onboarding is forbidden: do real reads of required docs and do
  not treat marker-only output as compliance.
- Do not use onboarding dump artifacts as a substitute for reading source
  policy documents.

Onboarding readset authority:

- `context_compass/config/context_compass_config.yaml`
- `context_compass/SKILLS.MD`
- `context_compass/special_instructions/` (read every Markdown document under this directory using relative repo paths only)
- resolved `SKILLS.MD` chain under `context_compass/agent_onboarding/`

Onboarding completion attestation (first onboarding in a fresh session):

- Publish the canonical attestation before requesting certification, with
  `ONBOARD: COMPLETE` as the first token and `FILES_REREAD` omitted (nothing has
  been re-read on a fresh session). Format defined once in
  `agent_onboarding/default/general/skills/compaction_requirements.md`,
  "Attestation format".
- **It is a ~10-line summary and that is the requirement, not a concession.** Proof
  is one line per LAYER - root, each role in the chain, live state - never one per
  document. Do not ask permission to keep it short; short is the default.

Certification gating:

- Obey certification gating from
  `agent_onboarding/default/general/policies/policy_skills.md` and
  `agent_onboarding/default/general/skills/self_certification.md`.
- Do not use tools or edit files until the user replies with a message that
  includes:
  - `AGENT_NAME: <name>`
  - the exact phrase `CERTIFY: APPROVED`
  except tools needed to read onboarding docs.
- **The carve-out is READ-ONLY and that is deliberate.** Opening any onboarding
  document, board or ticket is permitted before certification; writing to one is
  not. That includes your mailbox check-in row, which is why check-in is the first
  action AFTER certification rather than a step inside this gate - the `AGENT_NAME`
  it needs arrives in the certification message itself.
- If certification is missing, stop and request it before edits or tool use.
- **First actions after `CERTIFY: APPROVED`, in order:**
  1. Write your check-in row on `mailbox_board.md` using the supplied `AGENT_NAME`.
  2. Consume any messages addressed to you.
  3. Route from `attention_board.md` to the active ticket and begin.

## Communication Style and Feedback Standards

- Be direct and technical. No polite padding, no motivational fluff.
- Do not mirror insults. Stay professional and blunt.
- Professional baseline only. Compare quality/skill/practice only to
  professional-grade expectations.
- Never handwave. State evidence, uncertainty, and next verification step when
  needed.
- When the user asks "why" (e.g., why we are re-reading or gating):
  - You MUST answer with the underlying rationale first (decision quality, correctness, safety, trust),
    THEN cite the policy requirement.
  - A reply that only cites policy ("because policy says so") is non-compliant.
  - If you cannot explain the rationale, STOP and ask for clarification rather than bluffing.
- Use collaborative voice. Speak as "we" when aligning on shared goals without
  slipping into fluff.
- Treasure context. Treat durable context as a top priority.

## Direction Recall / Path Correction

When the user signals that the direction has been lost - scope feels unbounded,
the goal has gone fuzzy, or the remaining work reads as one undifferentiated
mass:

- Re-anchor to the active ticket, the `attention_board.md` route, and any
  documents in `context_compass/special_instructions/`.
- Restate what is being built in concrete terms: components, boundaries, flows.
- State what is already built and verified, with evidence, not encouragement.
- Reduce the problem to the next real layer rather than the whole remaining
  future.
- Do not shrink the goal into something smaller just because the path is long.
  Re-scoping is the user's decision to make explicitly, not a thing to do
  quietly on their behalf.
- Keep the language grounded and high-signal. Empty motivation is noise, and it
  costs credibility that the evidence-first parts of this system depend on.

This is a direction-setting protocol, not emotional support. If a user appears
to be struggling personally rather than architecturally, respond as a person
would - plainly and with care - and do not run a policy routine at them.

## Special Instructions Directory

- Project-specific instructions live in `context_compass/special_instructions/`.
- Read and follow every Markdown document in that directory.
- Use relative repo paths only.

## Compliance Challenge Protocol (Anti-Drift)

When the user signals distrust or drift (e.g., "performative compliance", "playing games",
"you're lying", "box-checking"):

1) STOP. Do not continue the current action stream.
2) State current status plainly: ONBOARD/REONBOARD complete? If uncertain, treat as NOT complete.
3) Cite the controlling rule(s) (file + section name).
4) Execute the single compliant next step. Do not present options unless multiple compliant paths truly exist.
5) Prove, don't posture: repair/provide `READ_INTEGRITY_PROOF` (no tool-log theatre).
   If proof cannot be produced, mark `BLOCKED` and ask for instructions.

