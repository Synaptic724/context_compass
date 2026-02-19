
# SKILLS Role Map

Purpose
- Define active profile roles and their `SKILLS.MD` entry points.
- Use direct profile-to-skills routing from this top-level `SKILLS.MD` file.

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
- `new`: `agent_onboarding/default/new/SKILLS.MD`
- `general`: `agent_onboarding/default/general/SKILLS.MD`
- `engineer`: `agent_onboarding/default/engineer/SKILLS.MD`
- `design_engineer`: `agent_onboarding/default/design_engineer/SKILLS.MD`
- `platform_engineer`: `agent_onboarding/default/platform_engineer/SKILLS.MD`
- `qa_engineer`: `agent_onboarding/default/qa_engineer/SKILLS.MD`
- `security_engineer`: `agent_onboarding/default/security_engineer/SKILLS.MD`
- `story_designer`: `agent_onboarding/default/story_designer/SKILLS.MD`
- `story_novel_artist`: `agent_onboarding/default/story_novel_artist/SKILLS.MD`
- `researcher`: `agent_onboarding/default/researcher/SKILLS.MD`
- `draft_writer`: `agent_onboarding/default/draft_writer/SKILLS.MD`
- `developmental_editor`: `agent_onboarding/default/developmental_editor/SKILLS.MD`
- `line_copy_editor`: `agent_onboarding/default/line_copy_editor/SKILLS.MD`
- `continuity_fact_checker`: `agent_onboarding/default/continuity_fact_checker/SKILLS.MD`
- `proofreader`: `agent_onboarding/default/proofreader/SKILLS.MD`
- `user_defined/*`: `agent_onboarding/user_defined/<name>/SKILLS.MD`

Role selection directive (non-negotiable)
1) When this `SKILLS.MD` map is read, list the available roles.
2) Ask the user which role to take on (unless the user already selected one).
3) Resolve the selected role to its `SKILLS.MD` path from this map.
4) Read the resolved role `SKILLS.MD`.
5) Treat the resolved role `SKILLS.MD` chain as the routing manifest:
   - You MUST read every path listed under **Active skills** / **Required baseline skills**
     in each resolved `SKILLS.MD` file (parent-first).
   - **On-demand** skills are conditional: do NOT read them for certification unless a trigger condition is met.
   - If an on-demand trigger is met, those on-demand paths become mandatory and MUST be read
     before proceeding in that scope.

Notes
- This file is a routing manifest, not a license to read the whole repo.
- Baseline/on-demand triggers are defined in the resolved role `SKILLS.MD` files and enforced
  by `AGENTS.MD` and `compaction_requirements.md`.
- The default roles are designed as delta layers:
  - `general` is the shared baseline for all work.
  - `engineer` extends `general` for implementation-focused engineering.
  - `design_engineer`, `platform_engineer`, `qa_engineer`, and `security_engineer` extend `engineer`
    for specialized software development workflows.
  - `story_designer`, `story_novel_artist`, `researcher`, `draft_writer`,
    `developmental_editor`, `line_copy_editor`, `continuity_fact_checker`, and
    `proofreader` extend `general` for fiction-authoring workflows.

