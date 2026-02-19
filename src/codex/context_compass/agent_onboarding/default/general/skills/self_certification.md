

# self_certification

Purpose
- Ensure onboarding is complete before any tool usage or edits.

Required flow
- Read routing authority from:
  - `context_compass/config/context_compass_config.yaml`
  - `context_compass/SKILLS.MD`
  - `context_compass/agent_onboarding/default/general/SKILLS.MD`
  - selected role `SKILLS.MD` path from `context_compass/SKILLS.MD`
- Complete role-driven onboarding reads from:
  - `context_compass/config/context_compass_config.yaml`
  - `context_compass/SKILLS.MD`
  - resolved role `SKILLS.MD` chain for the active profile.
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
- Summarize that onboarding is complete and request approval.
- Require the approval message to include the exact token
  `CERTIFY: APPROVED`.
- Do not use tools or edit files until the user provides that token.

Certification record
- Track certification in the session narrative and update `attention_board.md`
  routing when certification state affects execution.


