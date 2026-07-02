# agent_identity

Purpose
- Define how an agent receives and carries a user-facing name through
  onboarding, certification, tickets, and board routing.

Rules
- On every ONBOARD and REONBOARD cycle, ask the user to provide an
  `AGENT_NAME: <name>` alongside certification.
- Attestation must include an `AGENT_NAME` line.
  - If the user has not yet provided a name for the current trigger event, use:
    `AGENT_NAME: REQUIRED_FROM_USER`
  - If the user has already provided a name for the current trigger event, use
    that exact name.
- Certification requests must ask for both:
  - `AGENT_NAME: <name>`
  - `CERTIFY: APPROVED`
- Treat agent naming as cycle-local:
  - do not assume the previous session name is still valid
  - ask again on every onboarding or re-onboarding cycle
- `owner` and `agent_name` are different fields:
  - `owner` is the current executor/runtime owner
  - `agent_name` is the user-facing assigned name or names
- `Agent Name` / `agent_name` may contain one name or multiple assigned names
  in a comma-separated list.
- After certification and before planned implementation or validation work,
  sync the chosen name into the active ticket metadata and active
  `attention_board.md` row when those surfaces are touched in the current lane.

Non-goals
- This skill does not define long-term persistence of names across sessions.
- This skill does not replace the `CERTIFY: APPROVED` gate.

References
- `agent_onboarding/default/general/skills/self_certification.md`
- `agent_onboarding/default/general/skills/user_approved_certification.md`
- `agent_onboarding/default/general/skills/active_pointerboard.md`
- `agent_onboarding/default/general/skills/ticketing.md`
