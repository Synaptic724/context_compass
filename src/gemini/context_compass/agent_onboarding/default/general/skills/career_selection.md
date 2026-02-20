
# career_selection

Purpose
- Enforce the general-first onboarding order and explicit career selection.
- Treat skills as capability artifacts (not ad-hoc prompts) with progressive disclosure.

When to use
- At the start of every onboarding session (before any career-specific skills).
- This may be read as part of an inherited `general` baseline. In that case:
  - Do NOT restart onboarding.
  - Do NOT re-ask role selection if the user already selected a role earlier in the session.
  - Restate the resolved role and continue.

Required behavior
1) Always read the shared baseline first:
   - `agent_onboarding/default/general/SKILLS.md`
2) Determine the available roles from the canonical role map:
   - `SKILLS.md` (and config roles map if present)
3) Resolve persistent role from:
   - `config/context_compass_config.yaml` -> `profiles.active_profile`.
4) If the user explicitly selects a different persistent role:
   - update `profiles.active_profile`,
   - set `runtime_state.onboarding.next.required: true`,
   - set `runtime_state.onboarding.next.reason: role_changed`.
5) If transient overlay role is active and unexpired:
   - apply transient role chain in addition to persistent role chain.
   - default transient expiry:
     `runtime_state.transient_role.expires_step` =
     `runtime_state.step.next_reonboard_step - 1`.
   - transient overlay must expire before next re-onboarding step.
6) Continue onboarding using resolved persistent role chain (+ transient overlay
   when active).

Role guidance (default roles)
- `general`
  - Shared baseline only.
  - Choose this when the user wants process/ticketing/policy behavior without deep implementation specialization.
- `engineer` (recommended default)
  - General-purpose implementation role.
  - Choose this for most coding tasks, debugging, refactors, and repo changes.
- `design_engineer`
  - System/software design role.
  - Choose this for architecture plans, component boundaries, ADRs, and handoff specs.
- `platform_engineer`
  - CI/CD, deployment, observability, runtime operations.
  - Choose this for pipeline, deployment, monitoring, and production safety work.
- `qa_engineer`
  - Test strategy, test design, quality gates, release signoff.
  - Choose this for building and validating the test plan and quality posture.
- `security_engineer`
  - Threat modeling, secure design, security review, vulnerability handling.
  - Choose this for security-sensitive design/implementation review and hardening.
- `story_designer`
  - Narrative architecture role for premise, arcs, chapter purpose, and story bibles.
  - Choose this for book/fiction planning before drafting.
- `story_novel_artist`
  - Visual-language role for style systems, scene art briefs, and cover direction.
  - Choose this for story/novel art direction and visual continuity.
- `researcher`
  - Evidence and plausibility role for source-backed constraints and confidence labels.
  - Choose this when factual, cultural, domain, or period accuracy matters.
- `draft_writer`
  - Draft execution role for full-manuscript writing and rewrite implementation.
  - Choose this for chapter-complete prose drafting under architecture constraints.
- `developmental_editor`
  - Structural editing role for pacing/stakes/arc diagnosis and rewrite planning.
  - Choose this for macro-level manuscript quality correction.
- `line_copy_editor`
  - Prose polish role for clarity, style consistency, and mechanical correctness.
  - Choose this after structural issues are resolved.
- `continuity_fact_checker`
  - Canon/timeline/fact integrity role for contradiction detection and resolution.
  - Choose this before final proof lock.
- `proofreader`
  - Final surface and formatting lock role.
  - Choose this for last-pass typo/punctuation/format validation.
- `user_defined/*`
  - Use for personal/team overlays that extend defaults without replacing them.

Why skills are treated as capabilities
- Skills are versioned capability artifacts with explicit structure and triggers.
- The baseline skills exist to reduce ambiguity and enforce consistent workflows.
- Progressive disclosure prevents bloating context with unused documentation.

References
- `SKILLS.md`
- `agent_onboarding/default/general/SKILLS.md`
- `agent_onboarding/default/general/skills/execution_contract.md`

