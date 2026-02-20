
# configuration_map_guide

Purpose
- Explain where configuration lives and how class/profile routing is controlled.

Configuration file
- `config/context_compass_config.yaml`

Key sections
- `runtime_state`
  - active default role, first-time transitions.
- `available_profiles`
  - available classes.
- `roles_map` / `roles`
  - role-to-`SKILLS.md` mappings for default and user-defined classes.
  - `SKILLS.md` headers define inheritance order.
- `workflow`
  - ticket microcycle and note behavior controls.
- `artifacts`
  - artifact board and lifecycle controls.

Most important keys for onboarding
- `runtime_state.active_default_role`
  - Current persistent active class/profile.
- `runtime_state.first_time_enabled`
  - Controls whether the user is forced into first-time onboarding.
- `allowed_post_onboarding_profiles`
  - Which classes user can choose immediately after onboarding.
- `roles.new`
  - New-role `SKILLS.md` file path.
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
1) Confirm class exists in `available_profiles`.
2) Ensure its `SKILLS.md` path exists in the `roles` mapping.
3) Set `runtime_state.active_default_role` to the chosen class.
4) Validate `SKILLS.md` inheritance chain (`INHERITS_SKILLS_FROM: ...`).

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
- `rg -n "active_default_role|available_profiles" context_compass/config/context_compass_config.yaml`
- `Get-Content context_compass/SKILLS.md`
- `Get-Content context_compass/agent_onboarding/default/new/SKILLS.md`
- `Get-Content context_compass/agent_onboarding/default/general/SKILLS.md`
- `Get-Content context_compass/agent_onboarding/default/engineer/SKILLS.md`
- `Get-Content context_compass/agent_onboarding/default/design_engineer/SKILLS.md`
- `Get-Content context_compass/agent_onboarding/default/platform_engineer/SKILLS.md`
- `Get-Content context_compass/agent_onboarding/default/qa_engineer/SKILLS.md`
- `Get-Content context_compass/agent_onboarding/default/security_engineer/SKILLS.md`
- `Get-Content context_compass/agent_onboarding/default/story_designer/SKILLS.md`
- `Get-Content context_compass/agent_onboarding/default/story_novel_artist/SKILLS.md`
- `Get-Content context_compass/agent_onboarding/default/researcher/SKILLS.md`
- `Get-Content context_compass/agent_onboarding/default/draft_writer/SKILLS.md`
- `Get-Content context_compass/agent_onboarding/default/developmental_editor/SKILLS.md`
- `Get-Content context_compass/agent_onboarding/default/line_copy_editor/SKILLS.md`
- `Get-Content context_compass/agent_onboarding/default/continuity_fact_checker/SKILLS.md`
- `Get-Content context_compass/agent_onboarding/default/proofreader/SKILLS.md`

References
- `SKILLS.md`
- `agent_onboarding/default/new/skills/profile_model_explained.md`
- `PROFILE_CLASS_CREATION_GUIDE.md`

