
# configuration_map_guide

Purpose
- Explain where configuration lives and how class/profile routing is controlled.

Configuration file
- `config/context_compass_config.yaml`

Key sections
- `profiles`
  - active class, available classes, onboarding transitions.
- `roles_map` / `roles`
  - role-to-`SKILLS.MD` mappings for default and user-defined classes.
  - `SKILLS.MD` headers define inheritance order.
- `workflow`
  - ticket microcycle and note behavior controls.
- `artifacts`
  - artifact board and lifecycle controls.

Most important keys for onboarding
- `profiles.active_profile`
  - Current active class/profile.
- `profiles.onboarding.first_time_default_profile`
  - First-time entry class (typically `new`).
- `profiles.onboarding.allowed_post_onboarding_profiles`
  - Which classes user can choose immediately after onboarding.
- `profiles.onboarding.fallback_post_onboarding_profile`
  - Safe fallback if no explicit choice is made.
- `roles.new`
  - New-role `SKILLS.MD` file path.
- Default role entries (examples):
  - `roles.engineer`
  - `roles.design_engineer`
  - `roles.platform_engineer`
  - `roles.qa_engineer`
  - `roles.security_engineer`
  - `roles.story_designer`
  - `roles.story_novel_artist`
  - `roles.researcher`
  - `roles.draft_writer`
  - `roles.developmental_editor`
  - `roles.line_copy_editor`
  - `roles.continuity_fact_checker`
  - `roles.proofreader`

Class assignment basics
1) Confirm class exists in `profiles.available_profiles`.
2) Ensure its `SKILLS.MD` path exists in the `roles` mapping.
3) Set `profiles.active_profile` to the chosen class.
4) Validate `SKILLS.MD` inheritance chain (`INHERITS_SKILLS_FROM: ...`).

Recommended defaults after onboarding
- For general code-development work: `engineer` (inherits `general`).
- For specialized posture, default to the closest matching role:
  - `design_engineer` for architecture/design/handoff,
  - `platform_engineer` for CI/CD/deploy/observability/ops,
  - `qa_engineer` for testing and quality gates,
  - `security_engineer` for security review and hardening,
  - `story_designer` for fiction narrative architecture,
  - `story_novel_artist` for visual art direction and consistency,
  - `researcher` for evidence-backed plausibility,
  - `draft_writer` for manuscript drafting and rewrites,
  - `developmental_editor` for structural editing,
  - `line_copy_editor` for line/copy polish,
  - `continuity_fact_checker` for canon/timeline/fact integrity,
  - `proofreader` for final publication lock.

Validation checks
- `rg -n "active_profile|available_profiles|user_defined_profiles|onboarding" context_compass/config/context_compass_config.yaml`
- `Get-Content context_compass/SKILLS.MD`
- `Get-Content context_compass/agent_onboarding/default/new/SKILLS.MD`
- `Get-Content context_compass/agent_onboarding/default/general/SKILLS.MD`
- `Get-Content context_compass/agent_onboarding/default/engineer/SKILLS.MD`
- `Get-Content context_compass/agent_onboarding/default/design_engineer/SKILLS.MD`
- `Get-Content context_compass/agent_onboarding/default/platform_engineer/SKILLS.MD`
- `Get-Content context_compass/agent_onboarding/default/qa_engineer/SKILLS.MD`
- `Get-Content context_compass/agent_onboarding/default/security_engineer/SKILLS.MD`
- `Get-Content context_compass/agent_onboarding/default/story_designer/SKILLS.MD`
- `Get-Content context_compass/agent_onboarding/default/story_novel_artist/SKILLS.MD`
- `Get-Content context_compass/agent_onboarding/default/researcher/SKILLS.MD`
- `Get-Content context_compass/agent_onboarding/default/draft_writer/SKILLS.MD`
- `Get-Content context_compass/agent_onboarding/default/developmental_editor/SKILLS.MD`
- `Get-Content context_compass/agent_onboarding/default/line_copy_editor/SKILLS.MD`
- `Get-Content context_compass/agent_onboarding/default/continuity_fact_checker/SKILLS.MD`
- `Get-Content context_compass/agent_onboarding/default/proofreader/SKILLS.MD`

References
- `SKILLS.MD`
- `agent_onboarding/default/new/skills/profile_model_explained.md`
- `PROFILE_CLASS_CREATION_GUIDE.md`

