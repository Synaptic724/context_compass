

# Default Profile: new

Purpose
- First-time onboarding profile.
- Minimal path to onboard a developer before selecting a steady-state profile.

Rules
- Keep this profile lightweight and orientation-focused.
- Do not place deep language-specific execution rules here.
- On completion, route to `general` or `engineer` by config.
- Keep this profile user-facing: explain system purpose, classes, and config.

Folder structure
- `skills/`: first-time onboarding skills.
- `policies/`: onboarding policy and completion rules.
- `behavioral_guidelines/`: user-onboarding behavior flow.
- `examples/`: reserved for first-time onboarding examples.

First-time setup focus
- Use this profile to select a steady-state default profile.
- `general`: shared system/policy/ticketing baseline.
- `engineer`: programming/testing specialization layered on `general`.
- Fiction-authoring specializations layered on `general`:
  - `story_designer`
  - `story_novel_artist`
  - `researcher`
  - `draft_writer`
  - `developmental_editor`
  - `line_copy_editor`
  - `continuity_fact_checker`
  - `proofreader`
- `synaptic_python_developer`: user-defined overlay layered on `engineer`.

Agent-read policy
- README reads are allowed for `new` first-time onboarding.
- Non-new profile execution should use map/policy docs, not README files.

SKILLS.MD top-level sources
- `context_compass/SKILLS.MD`
- `context_compass/agent_onboarding/default/new/SKILLS.MD`

Primary onboarding docs
- `agent_onboarding/default/new/skills/system_overview_for_user.md`
- `agent_onboarding/default/new/skills/profile_model_explained.md`
- `agent_onboarding/default/new/skills/configuration_map_guide.md`
- `agent_onboarding/default/new/skills/onboarding_completion_and_next_step.md`
- `PROFILE_CLASS_CREATION_GUIDE.md` (root user guide; mapped only in `new`)


