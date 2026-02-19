

# Attention Board

Purpose
- Active-work routing board.
- Attention-only summary for fast re-entry.
- Canonical detail lives in linked tickets.

Attention details rule
- Keep this board compact and operational.
- Durable history belongs in ticket `## Notes`, not here.
- Use evidence ranges in `EVIDENCE` (`path:start_line-end_line`).
- Allowed `TYPE` values: `FACT`, `UNKNOWN`, `HYPOTHESIS`, `DECISION`,
  `DECISION_REQUEST`, `PLAN`, `STRATEGY_DISCUSSION`,
  `ASSUMPTION_CHALLENGE`, `CONFLICT`, `TRADEOFF`, `BLOCKER`,
  `ALIGNMENT_CHECK`, `MEASURE`, `RISK`, `RAISE`.
- Ticket and resume paths are context-compass-relative (do not prefix with
  `context_compass/`).
- Use `DATETIME` and `updated_at` values in ISO-8601 UTC
  (`YYYY-MM-DDTHH:MM:SSZ`).
- Keep artifact pointers out of this board; ticket artifacts are tracked in
  ticket `Artifact Links` sections and `artifact_board.md`.

## Active Items
| work_item | status | mode | owner | blocker | next | outcome | exit_signal | ticket | updated_at | reread |
|---|---|---|---|---|---|---|---|---|---|---|
| task: aethericrift discovery interview | in_progress | discovery | codex | none | run interview questions and capture explicit decisions in task/story/epic notes | unresolved AethericRift design unknowns are converted into clear decisions or bounded follow-ups | user confirms interview answers and decision framing | `tickets/tasks/2026-02-18_aethericrift_user_interview_task.md` | 2026-02-18T23:38:20Z | REQUIRED |

## Active Attention Details
- DATETIME: 2026-02-18T23:38:20Z
  TYPE: PLAN
  CLAIM: User requested kickoff for AethericRift and MutationResearch discovery;
    six discovery/design tickets were created and routing now points to the first
    interview task.
  EVIDENCE:
  - tickets/epics/2026-02-18_aethericrift_discovery_and_design_epic.md:1-128
  - tickets/epics/2026-02-18_mutationresearch_discovery_and_design_epic.md:1-129
  - tickets/stories/2026-02-18_aethericrift_discovery_story.md:1-100
  - tickets/stories/2026-02-18_mutationresearch_discovery_story.md:1-101
  - tickets/tasks/2026-02-18_aethericrift_user_interview_task.md:1-95
  - tickets/tasks/2026-02-18_mutationresearch_user_interview_task.md:1-94
  IMPACT: Discovery execution can continue immediately with explicit ticket
    linkage and clear next actions.
  NEXT: ask interview questions for TASK-2026-02-18-aethericrift-user-interview.
  SWITCH_TRIGGER: user provides interview answers and requests next synthesis step.
  RESUME_HIERARCHY: task.
  REREAD: REQUIRED

## Recently Closed Anchors
| work_item | status | owner | blocker | next | ticket | updated_at | reread |
|---|---|---|---|---|---|---|---|
| epic: onboarding policy drift hardening | done | codex | none | none | `tickets/epics/completed/2026-02-17_onboarding_policy_drift_hardening_epic_completed.md` | 2026-02-18T00:29:25Z | REQUIRED |
| story: onboarding policy language alignment | done | codex | none | none | `tickets/stories/completed/2026-02-17_onboarding_policy_language_alignment_story_completed.md` | 2026-02-18T00:29:25Z | REQUIRED |
| story: certification token-only policy | done | codex | none | none | `tickets/stories/completed/2026-02-18_certification_token_only_story_completed.md` | 2026-02-18T00:29:25Z | REQUIRED |
| task: onboarding policy skills/certify/reonboard sweep | done | codex | none | none | `tickets/tasks/completed/2026-02-17_onboarding_policy_skills_certify_reonboard_sweep_task_completed.md` | 2026-02-18T00:29:25Z | REQUIRED |
| task: benchmark p-core baseline and weighted scoring | done | codex | none | route to story-level discovery and location tasks | `tickets/tasks/completed/2026-02-17_codegen_benchmark_pcore_baseline_and_scoring_task_completed.md` | 2026-02-17T16:20:08Z | REQUIRED |
| task: split root AGENTS into bootstrap and profile-owned policies | done | codex | none | none | `tickets/tasks/completed/2026-02-17_agents_bootstrap_split_and_profile_distribution_task_completed.md` | 2026-02-17T15:53:33Z | HELPFUL |
