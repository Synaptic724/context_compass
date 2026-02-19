
# first_time_profile_setup

Purpose
- Define first-time onboarding steps before steady-state profile execution.
- Centralize setup guidance for user orientation, profile selection, and default class assignment.

First-time setup sequence
1) Start from `AGENTS.MD` bootstrap rules.
2) Read `SKILLS.MD` and configuration authority in `config/context_compass_config.yaml`.
3) Explain the system purpose and onboarding model using:
   - `system_overview_for_user.md`
   - `profile_model_explained.md`
   - `configuration_map_guide.md`
4) Offer default class selection for post-onboarding:
   - `general` for system/process execution baseline (shared).
   - `engineer` for most code-development execution (inherits `general`, recommended default).
   - Specialized software roles (inherit `engineer`) when the work requires deeper posture:
     - `design_engineer` (architecture/design/handoff)
     - `platform_engineer` (CI/CD/deploy/observability/ops)
     - `qa_engineer` (test strategy/quality gates/release signoff)
     - `security_engineer` (threat modeling/security review/hardening)
   - Specialized fiction-authoring roles (inherit `general`):
     - `story_designer` (narrative architecture and chapter planning)
     - `story_novel_artist` (visual language, scene art briefs, cover direction)
     - `researcher` (source-backed plausibility constraints)
     - `draft_writer` (manuscript drafting and rewrites)
     - `developmental_editor` (structural diagnosis and rewrite plans)
     - `line_copy_editor` (line-level prose polish)
     - `continuity_fact_checker` (canon/timeline/fact checks)
     - `proofreader` (final typo/punctuation/format lock)
5) Confirm first-time completion and switch to selected default profile path map.

Profile intent summary
- `general`:
  shared system behavior, ticketing, policy, and execution workflow baseline.
- `engineer`:
  programming/testing/architecture/code-construction specialization layered on top of `general`.
- `design_engineer`:
  system/software design and architecture planning specialization layered on top of `engineer`.
- `platform_engineer`:
  CI/CD, deployment, observability, incident workflow specialization layered on top of `engineer`.
- `qa_engineer`:
  test planning, test design, and release quality specialization layered on top of `engineer`.
- `security_engineer`:
  security review, threat modeling, and vulnerability posture specialization layered on top of `engineer`.
- `story_designer`:
  fiction narrative architecture specialization layered on top of `general`.
- `story_novel_artist`:
  fiction visual-language and art-direction specialization layered on top of `general`.
- `researcher`:
  evidence and plausibility research specialization layered on top of `general`.
- `draft_writer`:
  full-manuscript drafting and rewrite execution specialization layered on top of `general`.
- `developmental_editor`:
  structural editing specialization layered on top of `general`.
- `line_copy_editor`:
  prose polish and consistency specialization layered on top of `general`.
- `continuity_fact_checker`:
  canon/timeline/fact integrity specialization layered on top of `general`.
- `proofreader`:
  final surface-quality lock specialization layered on top of `general`.

User-facing recommendation
- This system is designed for code development and supports any language.
- It enhances Codex and other AI workflows by enforcing durable context.
- Recommended mode in this repo is Codex with Extra High reasoning.
- Other reasoning modes are currently untested in this repo.

Rules
- Keep README reads scoped to first-time setup (`new` profile).
- Do not require README reads for non-new profile onboarding paths.
- Treat config YAML as authoritative for profile selection/onboarding.
- Treat skill-map headers as authoritative for inheritance order.

References
- `context_compass/AGENTS.MD`
- `context_compass/config/context_compass_config.yaml`
- `context_compass/SKILLS.MD`
- `agent_onboarding/default/general/SKILLS.MD`
- `agent_onboarding/default/engineer/SKILLS.MD`
- `agent_onboarding/default/design_engineer/SKILLS.MD`
- `agent_onboarding/default/platform_engineer/SKILLS.MD`
- `agent_onboarding/default/qa_engineer/SKILLS.MD`
- `agent_onboarding/default/security_engineer/SKILLS.MD`
- `agent_onboarding/default/story_designer/SKILLS.MD`
- `agent_onboarding/default/story_novel_artist/SKILLS.MD`
- `agent_onboarding/default/researcher/SKILLS.MD`
- `agent_onboarding/default/draft_writer/SKILLS.MD`
- `agent_onboarding/default/developmental_editor/SKILLS.MD`
- `agent_onboarding/default/line_copy_editor/SKILLS.MD`
- `agent_onboarding/default/continuity_fact_checker/SKILLS.MD`
- `agent_onboarding/default/proofreader/SKILLS.MD`
- `agent_onboarding/default/new/SKILLS.MD`
- `agent_onboarding/default/new/policies/new_onboarding_policy.md`

