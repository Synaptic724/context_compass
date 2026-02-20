
# SKILLS Role Map

Purpose
- Define active profile roles and their `SKILLS.md` entry points.
- Use direct profile-to-skills routing from this top-level `SKILLS.md` file.

Available roles
- `new`
- `general`
- `engineer`
- `design_engineer`
- `platform_engineer`
- `qa_engineer`
- `security_engineer`
- `story_designer`
- `story_novel_artist`
- `researcher`
- `draft_writer`
- `developmental_editor`
- `line_copy_editor`
- `continuity_fact_checker`
- `proofreader`
- `user_defined/*`

Available path map
- `new`: `agent_onboarding/default/new/SKILLS.md`
- `general`: `agent_onboarding/default/general/SKILLS.md`
- `engineer`: `agent_onboarding/default/engineer/SKILLS.md`
- `design_engineer`: `agent_onboarding/default/design_engineer/SKILLS.md`
- `platform_engineer`: `agent_onboarding/default/platform_engineer/SKILLS.md`
- `qa_engineer`: `agent_onboarding/default/qa_engineer/SKILLS.md`
- `security_engineer`: `agent_onboarding/default/security_engineer/SKILLS.md`
- `story_designer`: `agent_onboarding/default/story_designer/SKILLS.md`
- `story_novel_artist`: `agent_onboarding/default/story_novel_artist/SKILLS.md`
- `researcher`: `agent_onboarding/default/researcher/SKILLS.md`
- `draft_writer`: `agent_onboarding/default/draft_writer/SKILLS.md`
- `developmental_editor`: `agent_onboarding/default/developmental_editor/SKILLS.md`
- `line_copy_editor`: `agent_onboarding/default/line_copy_editor/SKILLS.md`
- `continuity_fact_checker`: `agent_onboarding/default/continuity_fact_checker/SKILLS.md`
- `proofreader`: `agent_onboarding/default/proofreader/SKILLS.md`
- `user_defined/*`: `agent_onboarding/user_defined/<name>/SKILLS.md`

Role selection directive (non-negotiable)
1) Resolve the selected role from
   `config/context_compass_config.yaml` -> `runtime_state.active_default_role`.
2) If the user explicitly selects a different persistent role:
   - update `runtime_state.active_default_role` to that role.
3) Optional transient overlay:
   - when `runtime_state.transient_role.role` is set and
     the injected Step ID is below
     `runtime_state.transient_role.expires_step`, apply transient role reads
     in addition to `runtime_state.active_default_role`.
   - when setting a transient role, default
     `runtime_state.transient_role.expires_step` to
     `runtime_state.step.next_reonboard_step - 1`.
   - transient overlay expires at/after `expires_step`.
4) Resolve the role path(s) from this map.
5) Read the resolved role `SKILLS.md`.
6) Treat the resolved role `SKILLS.md` chain as the routing manifest:
   - You MUST read every path listed under **Active skills** / **Required baseline skills**
     in each resolved `SKILLS.md` file (parent-first).
   - **On-demand** skills are conditional: do NOT read them for certification unless a trigger condition is met.
   - If an on-demand trigger is met, those on-demand paths become mandatory and MUST be read
     before proceeding in that scope.

Notes
- This file is a routing manifest, not a license to read the whole repo.
- Baseline/on-demand triggers are defined in the resolved role `SKILLS.md` files and enforced
  by `GEMINI.MD` and `compaction_requirements.md`.
- The default roles are designed as delta layers:
  - `general` is the shared baseline for all work.
  - `engineer` extends `general` for implementation-focused engineering.
  - `design_engineer`, `platform_engineer`, `qa_engineer`, and `security_engineer` extend `engineer`
    for specialized software development workflows.
  - `story_designer`, `story_novel_artist`, `researcher`, `draft_writer`,
    `developmental_editor`, `line_copy_editor`, `continuity_fact_checker`, and
    `proofreader` extend `general` for fiction-authoring workflows.


