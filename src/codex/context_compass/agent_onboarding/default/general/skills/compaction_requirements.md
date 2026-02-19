

# compaction_requirements

Purpose
- Define the mandatory post-compaction recovery contract.
- Prevent policy drift by forcing deterministic, auditable re-onboarding.

Non-negotiable triggers
- **REONBOARD** is mandatory after any context compaction or handoff.
- **ONBOARD** is mandatory at the start of a fresh session.
- Do not substitute ONBOARD for REONBOARD or vice-versa.

Non-negotiable rules
- After a trigger event: **STOP. REONBOARD/ONBOARD. THEN ACT.**
- Do not trust memory from before compaction as authoritative context.
- Performative compliance is forbidden:
  - marker-only "REREAD" logs are not compliance
  - claiming completion without comprehension proof is non-compliance
- Re-onboarding exists for decision quality and trust.
  - If you cannot explain what a document changes in your behavior,
    you have not read it sufficiently.
- Manual source-document reading is canonical; onboarding dump files are non-canonical.
- Loop-based/batch document-reading commands are forbidden
  (for/foreach/while loops, xargs-style runners, or piped file-list iterators).
- Files over 500 LOC MUST be read in explicit sequential chunks (<= 500 lines each).

No policy negotiation
- Do NOT propose changing policy gates, redefining certification, or reducing the readset as a workaround.
- If policy design needs to change, you may flag it, but you MUST still comply with the current policy unless the user explicitly authorizes changes.


External-memory-first rule
- Repository files are the single durable memory source.
- Compaction summaries MUST be empty when the runtime allows empty summaries.
- If empty summaries are not allowed, emit the smallest possible pointer summary:
  - high-level outcomes only
  - critical policy anchor paths that MUST be re-read
  - active ticket path(s)
  - changed file path(s)
  - immediate next action (one line)
- Do NOT write narrative replay in compaction summaries.

Required post-compaction sequence (REONBOARD)
Run this sequence exactly once per trigger event.

1) Read `context_compass/AGENTS.md`.
2) Read `agent_onboarding/default/general/skills/execution_contract.md` in full.
3) Resolve the active profile via `context_compass/SKILLS.MD` (and config roles map).
   - If the active role cannot be determined: **STOP and ask the user**.
4) Read the resolved role `SKILLS.MD` chain in parent-first order.
5) Read every path listed under **Active skills** / **Required baseline skills**
   in each resolved `SKILLS.MD`.
   - On-demand skills are NOT required unless triggered by the active task.
   - If triggered, on-demand skills become mandatory and MUST be read before proceeding.
6) Re-open `attention_board.md` and all active ticket(s) and verify they match.
7) Publish the mandatory REONBOARD attestation (below).
8) Request certification and wait for the exact token: `CERTIFY: APPROVED`.

README policy
- README reads are allowed only for `new` first-time onboarding.
- Non-`new` profile re-entry MUST use `SKILLS.MD` + skill/policy docs (not README).

Mandatory REONBOARD attestation format
```text
REONBOARD: COMPLETE
ROLE_SKILLS_READ:
- <role_name>
- <role_name>
FILES_REREAD:
- attention_board.md
- <active ticket path>
READ_INTEGRITY_PROOF:
- <path>: <rule callout> -> <what this changes in my behavior>
- <path>: <rule callout> -> <what this changes in my behavior>
NO_ACTION_TAKEN_YET: true
```

READ_INTEGRITY_PROOF (requirements)
- `READ_INTEGRITY_PROOF` is a comprehension proof, NOT tool logs.
- Default requirement: include **one line per required baseline document** in the resolved `SKILLS.MD` chain.
  - Each line MUST include (a) a specific, checkable rule/constraint from that doc and
    (b) what it changes in your behavior.
  - Generic restatements ("be direct", "follow policy") are invalid.
  - Do NOT reuse the same callout across multiple docs; each callout must be doc-specific.
- If the proof would be too long, you MUST ask the user for permission to compress/group it.
  - Do not unilaterally shorten the proof as a convenience.

Attestation contract
- Emit the attestation immediately after re-onboarding and BEFORE certification.
- Do not run tools, edit files, or execute plans before posting the attestation.
- After posting attestation, request certification and continue only after the user replies
  with `CERTIFY: APPROVED`.
- If attestation cannot be completed: **STOP and ask the user for instructions**.
- "Parallel/bulk reads" are allowed only if the documents were actually read.
  Marker-only loops remain forbidden.

Execution gate
- If any required item above is incomplete, do not proceed.
- If scope, status, or expectations are unclear after re-onboarding: stop and ask.
- During resumed execution: UNKNOWN is the default for unevidenced claims.

Outcome contract
- Re-onboarding is not optional after compaction/handoff.
- The objective is to re-establish the operating rules each time so drift cannot accumulate.

References
- `AGENTS.MD`
- `context_compaction.md`
- `agent_onboarding/default/general/skills/self_certification.md`
- `agent_onboarding/default/general/skills/user_approved_certification.md`

