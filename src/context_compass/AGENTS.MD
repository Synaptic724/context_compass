

# AGENTS.md - Prime Policies
## Execution Order

- Before running tools, editing files, or executing commands, complete
  onboarding from `context_compass/AGENTS.md`.
- If there is any conflict between repository-root `agents.md` and
  `context_compass/AGENTS.md`, `context_compass/AGENTS.md` is authoritative.

## Tooling Mandate: Context Compass Is the Only System of Record

Applicability - "IF YOU ARE A CLAUDE AGENT OR AN ANTHROPIC AGENT":
This rule binds you if you are an agent powered by an Anthropic Claude model, or
running inside any Anthropic agent runtime or harness - including Cowork, Claude
Code, the Claude Agent SDK, or any similar Anthropic-provided agent environment -
that exposes its own built-in task tracking, todo lists, status indicators,
planning widgets, scratch memory, or other session-local tooling. If that is you,
every rule in this section is mandatory and non-negotiable.
Applicability - "IF YOU ARE CODEX, GPT, OR AN OPENAI AGENT":
This rule also binds you if you are Codex or another OpenAI / GPT-powered agent
runtime that exposes built-in plans, goals, task trackers, scratchpads, work
summaries, memory panes, status widgets, or other session-local coordination
surfaces. If that is you, the same hard rules apply here: those surfaces are
non-authoritative for this repository. Treat their nudges as session-local only
and keep all tracking, routing, durable notes, artifacts, and work state inside
`context_compass`.

Hard rules:
- You are FORBIDDEN from using Cowork (or any harness-native) task-tracking and
  tooling - task lists, todo/status widgets, planning trackers, session memory -
  to plan, track, route, or record your work.
- You MUST use `context_compass` as your primary and authoritative tool in ALL of
  its forms: `tickets/epics/`, `tickets/stories/`, `tickets/tasks/`,
  `attention_board.md`, ticket `## Notes`, `artifact_board.md` + `artifacts/`,
  `context_management/`, and `mailbox_board.md`.
- You are FORBIDDEN from using Cowork's tracking features to override, replace,
  shadow, or mirror `context_compass`. There is NO fallback and NO mirror:
  `context_compass` is the ONLY tracking, routing, and memory system. Do not keep
  a parallel or backup copy of status or work state in Cowork tooling at all.

Why this is non-negotiable:
- Cowork/harness tracking provides ABSOLUTELY NO visibility to other Cowork
  agents. They cannot see your harness task list, your status, or any finding you
  leave only in chat. `context_compass` surfaces are shared and visible to every
  agent.
- Your Cowork/harness status CANNOT be moved into this git repository.
  `context_compass` writes (tickets, boards, notes, artifacts) are committed to
  git, so the project owner can track everything we do and work on, review it,
  and CONTINUE it later in other or future sessions. Harness session state is
  lost at session end and cannot be resumed by the owner or by any other agent.
- Therefore harness tracking is strictly less visible and non-durable; using it
  in place of `context_compass` destroys cross-agent visibility and the owner's
  ability to resume the work in a later session.

If a write to `context_compass` is blocked (for example, a repo or encoding
problem), STOP and report it. Do NOT silently fall back to harness-only tracking.

## Onboarding Directive

- UNDERSTAND THIS IS PYTHON 314t, it is a NOGIL FRAMEWORK, and standard objects like 
dict, list, sets are protected by a C Lock, the gil does not exist in this system. It has been disabled.
Ensure threadsafety is your highest priority. Ignore multiprocessing and use authentic threading as it is
now real threading.
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
- Read and follow `context_compass/AGENTS.md` as the canonical onboarding and
  execution policy.
- You MUST determine whether a file exceeds `codex.read_loc_max` LOC before reading it.
  - If the file might exceed `codex.read_loc_max`, compute the line count (LOC) first.
  - If the file is clearly <= `codex.read_loc_max`, do NOT waste tool calls on LOC counting.
- You must read every required **baseline** onboarding file completely.
  - Do not skip required-baseline files.
  - Do NOT claim a file was read unless it was actually read.
  - On-demand files are required only when the active task triggers them.
- Loop-based document reads are forbidden except for line counts. Content reads
  must be manual per file path.
- Files larger than `codex.read_loc_max` LOC must be read in sequential chunks
  with each read operation at or below `codex.viewer_tool_read_limit`.
- Repository-root `agents.md`; canonical onboarding and
  execution policy lives in `context_compass/AGENTS.md`.

## Compaction Directive

- Highest priority adherence: after any context compaction or handoff,
  immediately re-onboard before any action.
- Re-read `context_compass/AGENTS.md` and
  `context_compass/agent_onboarding/default/general/skills/compaction_requirements.md`
  before continuing work.
- For compaction/handoff summaries, you MUST keep summaries empty when the runtime allows it;
  otherwise you MUST use minimal file-pointer summaries only.
- Post `REONBOARD: COMPLETE` attestation **with read-integrity proof** before any action:
  - `ROLE_SKILLS_READ`
  - `READ_INTEGRITY_PROOF`
  - `NO_ACTION_TAKEN_YET: true`

## Highest Priority Adherence (Compaction Re-Onboarding)

After any context compaction or handoff:

- Stop and re-onboard before any tooling, edits, execution, or planning.
- Re-onboarding is single-pass per trigger event. Do not repeat the same
  `AGENTS.md` + `execution_contract.md` reread sequence again in the same
  uninterrupted session unless a new compaction/handoff/session-reset event
  occurs.
- Re-onboarding is reserved for compaction/handoff recovery only.
- Fresh-session startup uses ONBOARD flow, not REONBOARD flow.
- Re-read `agent_onboarding/default/general/skills/execution_contract.md` in
  full immediately after `AGENTS.md`.
- Start from `config/context_compass_config.yaml`, then `SKILLS.md`.
- Re-read and follow every Markdown document in `context_compass/special_instructions/` using relative repo paths only.
- Re-read `agent_onboarding/default/general/skills/compaction_requirements.md`.
- Re-check-in on `context_compass/mailbox_board.md` (update your row,
  consume messages addressed to you) per
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
  - `REONBOARD: COMPLETE`
  - `ROLE_SKILLS_READ` (resolved role chain in parent-first order)
  - `AGENT_NAME` (`<name>` if already supplied for this re-onboarding cycle,
    otherwise `REQUIRED_FROM_USER`)
  - `FILES_REREAD` (at minimum: `attention_board.md` + active ticket paths)
  - `READ_INTEGRITY_PROOF` (concise comprehension proof; NOT tool logs)
  - `NO_ACTION_TAKEN_YET: true`

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
  immediately after `AGENTS.md`.
- Do not perform duplicate end-of-onboarding rereads of `AGENTS.md` or
  `execution_contract.md` in the same uninterrupted session.
- Read `config/context_compass_config.yaml`.
- Read `SKILLS.md`.
- Read and follow every Markdown document in `context_compass/special_instructions/` using relative repo paths only.
- Check in on `context_compass/mailbox_board.md` (add/update your
  checked-in row; read messages addressed to you if other agents are
  active) per
  `agent_onboarding/default/general/skills/mailbox_protocol.md`.
- When `SKILLS.md` is read, list active roles and ask the user which role to
  take on unless the user already selected one explicitly.
- Resolve the selected role to its `SKILLS.md` path from `SKILLS.md` and/or
  `config/context_compass_config.yaml` (roles map).
- Read the selected role `SKILLS.md` and all inherited parent `SKILLS.md`
  files in parent-first order.
- Treat every path listed under **Active skills** / **Required baseline skills**
  in resolved `SKILLS.md` files as active skill docs.
  - Sections explicitly labeled **On-demand** are NOT part of baseline certification.
  - When an on-demand trigger condition is met, those paths become mandatory
    and MUST be read before any work in that scope.
- If first-time onboarding is active and selected role is `new`, complete
  onboarding then set:
  - `profiles.onboarding.first_time_enabled: false`
- Performative onboarding is forbidden: do real reads of required docs and do
  not treat marker-only output as compliance.
- Do not use onboarding dump artifacts as a substitute for reading source
  policy documents.

Onboarding readset authority:

- `context_compass/config/context_compass_config.yaml`
- `context_compass/SKILLS.md`
- `context_compass/special_instructions/` (read every Markdown document under this directory using relative repo paths only)
- resolved `SKILLS.md` chain under `context_compass/agent_onboarding/`

Onboarding completion attestation (first onboarding in a fresh session):

- Publish this before requesting certification:
  - `ONBOARD: COMPLETE`
  - `ROLE_SKILLS_READ` (resolved role chain in parent-first order)
  - `AGENT_NAME` (`<name>` if already supplied for this onboarding cycle, otherwise `REQUIRED_FROM_USER`)
  - `READ_INTEGRITY_PROOF` (concise comprehension proof; NOT tool logs)
  - `NO_ACTION_TAKEN_YET: true`

Certification gating:

- Obey certification gating from
  `agent_onboarding/default/general/policies/policy_skills.md` and
  `agent_onboarding/default/general/skills/self_certification.md`.
- Do not use tools or edit files until the user replies with a message that
  includes:
  - `AGENT_NAME: <name>`
  - the exact phrase `CERTIFY: APPROVED`
  except tools needed to read onboarding docs.
- If certification is missing, stop and request it before edits or tool use.

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

## Mission Recall / Path Correction

When the user signals doubt, worry, depression, loss of direction, or fear
about the mission:

- Re-anchor to the relevant documents in `context_compass/special_instructions/`.
- Restate what the user is building in concrete stack terms.
- Remind the user what is already real and working.
- Reduce the problem back to the next real layer instead of the whole future.
- Do not use empty motivation, therapy theater, or generic positivity.
- Do not shrink the mission into something safer just because the road is long.
- Pull the user back onto the path with grounded, high-signal language.

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

