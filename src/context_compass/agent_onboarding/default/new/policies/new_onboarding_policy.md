
# new_onboarding_policy

Purpose
- Define the mandatory policy for `new` first-time onboarding.
- Keep this profile user-facing and orientation-heavy, not implementation-heavy.

Scope
- Applies only when routing through `agent_onboarding/default/new/SKILLS.MD`.
- Ends when the user chooses and applies a default steady-state class/profile.

Policy
- Explain the system in plain language before asking for configuration changes.
- Describe the system goal accurately:
  - context_compass is a policy-driven workflow system for code and fiction,
  - it supports any programming language,
  - it improves consistency across AI coding agents generally.
- State current execution recommendation explicitly:
  - use the strongest reasoning setting your runtime offers,
  - this system trades tokens for reliability, so weak reasoning modes tend to
    produce onboarding claims the agent cannot actually back.
- Explain profile classes and inheritance before asking for selection.
- Present the full set of roles by reading the registry table in `SKILLS.MD`.
  Do not present a role list from any other document; only the registry is current.
- Make `engineer` the recommended default class for general code development.
- If the user needs a specialized posture, route them to the matching role:
  - software lane: `design_engineer`, `platform_engineer`, `qa_engineer`,
    `security_engineer`.
  - fiction lane: `story_designer`, `story_novel_artist`, `researcher`,
    `draft_writer`, `developmental_editor`, `line_copy_editor`,
    `continuity_fact_checker`, `proofreader`.
- Keep `new` profile content minimal; do not load deep engineering policy here.

Configuration authority
- `SKILLS.MD` is the source of truth for:
  - which roles exist,
  - the role -> `SKILLS.MD` path map,
  - which roles are selectable after onboarding,
  - which roles read README files.
- `config/context_compass_config.yaml` is the source of truth for:
  - onboarding defaults and transitions (`profiles.onboarding.*`),
  - workflow, artifact, formatting, and read-limit behaviour.
  - It does NOT enumerate roles.
- `agent_onboarding/*/SKILLS.MD` headers are the source of truth for:
  - inheritance chain,
  - resolved parent-first read order.

Completion criteria
- User understands what the system is for.
- User understands profiles/classes and inheritance.
- User understands where config lives and how to change it.
- User is offered default class selection with `engineer` recommended.
- Next step is clear and explicit before leaving `new`.

References
- `AGENTS.MD`
- `SKILLS.MD`
- `agent_onboarding/default/new/skills/first_time_profile_setup.md`
- `agent_onboarding/default/new/skills/configuration_map_guide.md`
