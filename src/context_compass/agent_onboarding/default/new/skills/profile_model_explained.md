
# profile_model_explained

Purpose
- Explain profile classes, inheritance, and how profile routing works.

Profile classes
- `new`
  - First-time onboarding path.
  - Focuses on user orientation and setup.

> The registry table in `context_compass/SKILLS.MD` is the authoritative
> role list. The descriptions below are teaching material for first-time
> onboarding and do not include user-defined roles. If the two disagree,
> the registry wins.

- `general`
  - Shared system mechanics and workflow behavior.
  - Baseline class for all work.
- `engineer`
  - General-purpose implementation specialization layered on top of `general`.
  - Includes engineering quality, debugging discipline, and system-doc mechanics.
- `design_engineer`
  - Software/system design specialization layered on top of `engineer`.
  - Includes architecture planning, decomposition, ADR hygiene, and design handoff.
- `platform_engineer`
  - Platform/operations specialization layered on top of `engineer`.
  - Includes CI/CD, deployments, observability, incident workflow, and production safety.
- `qa_engineer`
  - Quality/test specialization layered on top of `engineer`.
  - Includes test strategy, test design, automation practices, and release signoff mechanics.
- `security_engineer`
  - Security specialization layered on top of `engineer`.
  - Includes threat modeling, secure design reviews, dependency risk, and vulnerability handling.
- `story_designer`
  - Fiction narrative-architecture specialization layered on top of `general`.
  - Includes premise design, arc architecture, chapter mapping, and story-bible design.
- `story_novel_artist`
  - Fiction visual-language specialization layered on top of `general`.
  - Includes style systems, scene art briefs, and cover-direction constraints.
- `researcher`
  - Evidence and plausibility specialization layered on top of `general`.
  - Includes source quality triage, confidence labeling, and constraint synthesis.
- `draft_writer`
  - Manuscript drafting specialization layered on top of `general`.
  - Includes draft completion, rewrite execution, and deviation logging.
- `developmental_editor`
  - Structural editing specialization layered on top of `general`.
  - Includes pacing/stakes/arc diagnosis and rewrite-plan generation.
- `line_copy_editor`
  - Prose-quality specialization layered on top of `general`.
  - Includes clarity polishing, style-sheet management, and mechanical cleanup.
- `continuity_fact_checker`
  - Canon/timeline/fact integrity specialization layered on top of `general`.
  - Includes continuity matrices, conflict classification, and fact-risk escalation.
- `proofreader`
  - Final surface-quality specialization layered on top of `general`.
  - Includes typo/punctuation/format lock and final waiver logging.
- `user_defined/<profile_name>`
  - Optional overlay class for personal or team preferences.
  - Should extend defaults instead of replacing them.

Inheritance model
- `engineer` extends `general`.
- `design_engineer` extends `engineer`.
- `platform_engineer` extends `engineer`.
- `qa_engineer` extends `engineer`.
- `security_engineer` extends `engineer`.
- `story_designer` extends `general`.
- `story_novel_artist` extends `general`.
- `researcher` extends `general`.
- `draft_writer` extends `general`.
- `developmental_editor` extends `general`.
- `line_copy_editor` extends `general`.
- `continuity_fact_checker` extends `general`.
- `proofreader` extends `general`.
- User-defined classes typically extend the most specific default role they need:
  - e.g. extend `engineer` for language/style preferences,
  - extend `platform_engineer` for infra-team overlays,
  - extend `security_engineer` for org-specific security controls.
- Read order is parent first, child last.
- Child maps should not duplicate parent paths.

Class selection model
- First-time entry uses `new`.
- After onboarding, the user chooses a steady-state role.
- Recommended default for general development workflows: `engineer`.
- Choose specialized roles when the task requires deeper domain posture.
- Selection is per agent, per session. It is not written anywhere and not
  shared between agents. Two agents in the same repository may hold different
  roles at the same time, so there is no single stored "current" role.

Where roles are declared
- `SKILLS.MD` - the single role registry.
  - One row per role: name, `SKILLS.MD` path, parent, user-defined flag,
    selectable-after-onboarding flag, README flag.
  - A role exists if and only if it has a row there.
- `config/context_compass_config.yaml` holds behaviour settings only. It does
  not enumerate roles. The only onboarding keys it carries are
  `profiles.onboarding.*`.

Where inheritance is defined
- The registry `extends` column names the parent role.
- The authoritative declaration lives in the role's own `SKILLS.MD` header:
  - `` - `INHERITS_SKILLS_FROM: <skills_path|none>` ``
- The two must agree. The header is what an agent walks; the column is what a
  human reads.
- Parent `SKILLS.MD` paths are loaded before child `SKILLS.MD` paths.

Rules for custom classes
- Keep shared process in `general`.
- Keep generalized engineering mechanics in `engineer`.
- Keep specialized domain posture in the closest matching default role.
- Keep personal/team bias in `user_defined`.
- Avoid overlap with inherited parent paths.

References
- `agent_onboarding/default/new/skills/configuration_map_guide.md`
- `PROFILE_CLASS_CREATION_GUIDE.md`

