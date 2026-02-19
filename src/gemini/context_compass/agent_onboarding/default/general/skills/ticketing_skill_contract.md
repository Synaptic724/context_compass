

# ticketing_skill_contract

## Purpose
This document defines how to create deep, descriptive structured tickets for epics, stories, and tasks in `tickets/epics/`, `tickets/stories/`, and `tickets/tasks/`.
The goal is durable, high-context planning that survives compaction and handoffs.

## Ticket Types (Use Templates)
- Epic: big project or cross-cutting initiative with multiple stories.
- Story: medium scope, user- or system-facing slice that can stand alone or live under an epic.
- Task: small, single deliverable that can stand alone.

Templates live in:
- `templates/epic_template.md`
- `templates/story_template.md`
- `templates/task_template.md`

## File Locations and Naming
- Epics: `tickets/epics/`
- Stories: `tickets/stories/`
- Tasks: `tickets/tasks/`

Naming convention (date-first, descriptive):
- `YYYY-MM-DD_<slug>_epic.md`
- `YYYY-MM-DD_<slug>_story.md`
- `YYYY-MM-DD_<slug>_task.md`

## Ticket Content Contract
- Canonical ticket schema and execution-gate requirements live in
  `agent_onboarding/default/general/skills/ticketing.md`.
- Canonical lifecycle sequencing, microcycle order, and closure sync live in
  `agent_onboarding/default/general/skills/workflow.md`.
- Use templates as the executable contract; do not fork section schemas in this
  skill.

## Ticket Formatting Rules
- Title line is required and outcome-focused.
- Metadata is a short bullet list at the top.
- Use short paragraphs and bullet lists for scanability.
- Link epic <-> story <-> task by ID in metadata and checklists.
- Apply formatting standards from
  `agent_onboarding/default/general/skills/configuration_standards.md` and
  config values in `config/context_compass_config.yaml`.

## Context Compaction / Handoff
- Canonical compaction/handoff process lives in
  `agent_onboarding/default/general/skills/context_compaction.md` and
  `agent_onboarding/default/general/skills/compaction_requirements.md`.
- Keep ticket `Context / Handoff Summary` sections current before handoff.


