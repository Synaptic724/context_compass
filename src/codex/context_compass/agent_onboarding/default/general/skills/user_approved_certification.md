

# user_approved_certification

Purpose
- Define the explicit approval step that unlocks tool usage and edits.

Approval script
- Ask the user to reply with a message that includes the exact token
  `CERTIFY: APPROVED`.
- Do not proceed with any tool use or file edits before approval.

Rules
- Only request approval after listing the skills read from:
  - `context_compass/config/context_compass_config.yaml`
  - `context_compass/SKILLS.MD`
  - `context_compass/agent_onboarding/default/general/SKILLS.MD`
  - selected role `SKILLS.MD` path from `context_compass/SKILLS.MD`
- Before requesting approval, complete role-driven onboarding reads from:
  - `context_compass/config/context_compass_config.yaml`
  - `context_compass/SKILLS.MD`
  - resolved role `SKILLS.MD` chain for the active profile
  - include read-integrity proof in the ONBOARD/REONBOARD attestation
  (concrete rule callouts -> behavior implications; not tool logs).
- Do not request approval based on onboarding dump artifacts; approval requires
  source-document read completion.
- After compaction/handoff/fresh-session re-entry, the same full-readset
  requirement applies again before requesting approval.


