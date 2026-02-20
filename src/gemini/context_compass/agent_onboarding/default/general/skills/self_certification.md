

# self_certification

Purpose
- Ensure onboarding is complete before any tool usage or edits.

Required flow
- Read routing authority from:
  - `context_compass/config/context_compass_config.yaml`
  - `context_compass/config/context_compass_config.yaml` `runtime_state` block
  - `context_compass/SKILLS.md`
  - `context_compass/agent_onboarding/default/general/SKILLS.md`
  - active role `SKILLS.md` path resolved from
    `runtime_state.active_default_role`
- Complete role-driven onboarding reads from:
  - `context_compass/config/context_compass_config.yaml`
  - `context_compass/SKILLS.md`
  - resolved role `SKILLS.md` chain for the active profile.
  - transient overlay role chain when active and unexpired.
- For a given trigger event, complete the readset once; do not duplicate-read
  the same onboarding set before certification unless a new
  compaction/handoff/session-reset event occurs.
- Manual source-document reading from the readset is required; onboarding dump
  files are non-compliant.
- Performative onboarding is forbidden: marker-only reread logs do not satisfy
  the read requirement.
- If the user challenges onboarding truthfulness (e.g., "you didn't read that", "you're lying",
  "performative compliance"):
  - Treat certification as NOT granted (or revoked) and STOP.
  - Re-onboard/re-onboard as required, then re-request `CERTIFY: APPROVED`.
  - Do not debate, rationalize, or offer bypass options.
- Before requesting certification, provide concise **read-integrity proof**:
  - concrete rule callouts from reread docs, AND
  - a one-line "what this changes in my behavior" per callout.
  - Tool logs/dumps are not proof.
- For ONBOARD/REONBOARD attestations, keep declarations concise with
  `ROLE_SKILLS_READ` and `NO_ACTION_TAKEN_YET: true`.
- Keep onboarding state truthful in YAML before certification:
  - calculate and update `runtime_state.step.next_reonboard_step` for REONBOARD events.
  - clear transient role fields when
    `runtime_state.transient_role.clear_on_reonboard: true`.
  - Append a proactive `PLAN` note to `attention_board.md` detailing the upcoming `next_reonboard_step` threshold, ensuring it is tracked as soon as the session starts.
- Summarize that onboarding is complete and request approval.
- Require the approval message to include the exact token
  `CERTIFY: APPROVED`.
- Do not use tools or edit files until the user provides that token.

Certification record
- Track certification in the session narrative and update `attention_board.md`
  routing when certification state affects execution.


