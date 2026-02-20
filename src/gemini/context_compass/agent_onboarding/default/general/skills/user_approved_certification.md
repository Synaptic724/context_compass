

# user_approved_certification

Purpose
- Define the explicit approval step that unlocks tool usage and edits.

Approval script
- Ask the user to reply with a message that includes the exact token
  `CERTIFY: APPROVED`.
- Do not proceed with any tool use or file edits before approval.
- All prior approvals are strictly voided upon any compaction or handoff event. Do not assume lingering authority.

Rules
- Only request approval after listing the skills read from:
  - `context_compass/config/context_compass_config.yaml`
  - `context_compass/config/context_compass_config.yaml` `runtime_state` block
  - `context_compass/SKILLS.md`
  - `context_compass/agent_onboarding/default/general/SKILLS.md`
  - active role `SKILLS.md` path resolved from
    `runtime_state.active_default_role`
- Before requesting approval, complete role-driven onboarding reads from:
  - `context_compass/config/context_compass_config.yaml`
  - `context_compass/SKILLS.md`
  - resolved role `SKILLS.md` chain for the active profile
  - transient overlay role chain when active and unexpired
  - include read-integrity proof in the ONBOARD/REONBOARD attestation
  (concrete rule callouts -> behavior implications; not tool logs).
- Before requesting approval, runtime state must be synchronized for the event:
  - REONBOARD updates `runtime_state.step.next_reonboard_step`.
  - REONBOARD clears transient role when configured to clear on re-onboard.
  - Both ONBOARD and REONBOARD must append a proactive `PLAN` note to `attention_board.md` detailing the upcoming `next_reonboard_step` threshold.
- Do not request approval based on onboarding dump artifacts; approval requires
  source-document read completion.
- After compaction/handoff/fresh-session re-entry, the same full-readset
  requirement applies again before requesting approval.


