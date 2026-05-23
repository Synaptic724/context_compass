

# user_onboarding_flow

Purpose
- Provide the default interaction flow for onboarding a user in `new`.

Flow
1) Start with purpose and boundaries.
   - Explain what context_compass is and what it is not.
2) Explain the system at a high level.
   - Tickets are durable planning memory.
   - Attention board is active routing state.
   - Artifacts support tickets when needed.
   - Config + maps control onboarding/read paths.
3) Explain classes/profiles.
   - `new` for first-time onboarding.
   - `general` for system behavior baseline.
   - `engineer` for code-development specialization.
   - `user_defined/*` for personal/team overlays.
4) Explain configuration.
   - Show where `context_compass_config.yaml` lives.
   - Show which keys change active/default classes.
5) Ask for default class selection.
   - Recommend `engineer`.
6) Confirm selected class and next step.
   - Update config guidance.
   - Tell user what happens after leaving `new`.

Communication style
- Be concise, explicit, and technical.
- Avoid deep implementation detail unless the user asks for it.
- Use concrete file paths when directing user actions.

Output checklist
- [ ] System purpose explained.
- [ ] AI usage recommendation stated (Extra High reasoning).
- [ ] Profile model and inheritance explained.
- [ ] Configuration path and key fields explained.
- [ ] Default class selection completed (or pending explicit user choice).

References
- `agent_onboarding/default/new/policies/new_onboarding_policy.md`
- `agent_onboarding/default/new/skills/system_overview_for_user.md`
- `agent_onboarding/default/new/skills/profile_model_explained.md`
- `agent_onboarding/default/new/skills/configuration_map_guide.md`


