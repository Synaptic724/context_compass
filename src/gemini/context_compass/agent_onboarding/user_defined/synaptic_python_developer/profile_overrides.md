

# synaptic_python_developer profile_overrides

Purpose
- Define the user-specific overlay scope for this profile.
- Keep default `general` and `engineer` baselines reusable for public users.

Resolved inheritance
- `general` -> `engineer` -> `synaptic_python_developer`
- Source of truth:
  `agent_onboarding/user_defined/synaptic_python_developer/SKILLS.MD` header
  `INHERITS_SKILLS_FROM: agent_onboarding/default/engineer/SKILLS.MD` and
  the engineer header chain to `agent_onboarding/default/general/SKILLS.MD`.

Overlay scope
- User-preference collaboration tone and engagement style.
- User-preference pushback intensity and clarification cadence.
- User-specific operating emphasis that should not be required for public
  default onboarding paths.

References
- `agent_onboarding/user_defined/synaptic_python_developer/policies/synaptic_policy_overrides.md`
- `agent_onboarding/user_defined/synaptic_python_developer/skills/synaptic_skill_overrides.md`
- `agent_onboarding/user_defined/synaptic_python_developer/behavioral_guidelines/synaptic_behavior_overrides.md`


