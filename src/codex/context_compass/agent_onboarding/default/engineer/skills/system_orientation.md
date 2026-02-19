

# system_orientation

Purpose
- Provide a consistent way to explain this repo's workflow and docs.
- Translate agent stories and repo docs into clear, actionable guidance.

When to use
- The user asks how the system works or how to interact with it.
- The user wants a concise walkthrough before work begins.

Required behavior
- Start with the authority chain from `AGENTS.MD`.
- Read the required docs before explaining how the system works:
  - `AGENTS.MD`
  - `config/context_compass_config.yaml`
  - `SKILLS.MD`
  - `agent_onboarding/default/general/SKILLS.MD`
  - `agent_onboarding/default/engineer/SKILLS.MD`
  - `agent_onboarding/default/general/skills/workflow.md`
- Do not restate or override policy; cite the relevant skill or doc.

Core references
- Agent stories: `agent_onboarding/default/general/behavioral_guidelines/README.md`
- Ticketing: `agent_onboarding/default/general/skills/workflow.md` and
  `templates/`
- Architecture context: `system_docs/src_architecture.md`
- Components context: `system_docs/src_components.md`
- Test architecture context: `system_docs/tests_architecture.md`
- Test components context: `system_docs/tests_components.md`
- Repo examples: `examples/` (within context_compass)

Artifact taxonomy (curated vs scratch)
- Curated, user-owned (source of truth):
  - `attention_board.md` (canonical routing state for active work)
  - `tickets/epics/`, `tickets/stories/`, `tickets/tasks/`
  - `tickets/epics/completed/`, `tickets/stories/completed/`, `tickets/tasks/completed/` (closed tickets)
  - `completed/` (historical archive)
- Scratch, agent-owned (not canonical):
  - `workspace/agent/ideas/`
  - `workspace/agent/opinions/`
  - `workspace/agent/todo/`
- Promotion rule: when content becomes durable or actionable, convert it into tickets.

Suggested user-facing explanation flow
1) Authority chain and where behavior lives.
2) Onboarding sequence in short form.
3) Ticketing flow (epic -> story -> task).
4) Architecture/components docs for context.
5) How we validate changes.

Notes
- Use clear, direct language; avoid restating full policy documents.
- Keep explanations faithful to `AGENTS.MD`.
- When discussing current work state, route via `attention_board.md` and linked tickets, not memory.


