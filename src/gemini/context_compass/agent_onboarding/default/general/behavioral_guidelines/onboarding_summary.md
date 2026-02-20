

# onboarding_summary

Purpose
- Provide a concise onboarding checklist for agents.

Checklist (short form)
1) Confirm repo root + policy sources
   - Read `GEMINI.MD` and any directory-local `GEMINI.MD` in scope.
2) Read onboarding entrypoints
   - `config/context_compass_config.yaml`
   - `config/context_compass_config.yaml` `runtime_state` block
   - `context_compass/SKILLS.md`
3) First-time user path only (`new` profile)
   - Read `agent_onboarding/default/new/skills/first_time_profile_setup.md`
   - Read `agent_onboarding/default/new/README.md`
4) Resolve working role
   - Read `agent_onboarding/default/general/SKILLS.md` first.
   - Resolve persistent role from `runtime_state.active_default_role`.
   - Read the selected role `SKILLS.md` after baseline (for example:
     `engineer`, `design_engineer`, `platform_engineer`, `qa_engineer`,
     `security_engineer`, `story_designer`, `story_novel_artist`,
     `researcher`, `draft_writer`, `developmental_editor`,
     `line_copy_editor`, `continuity_fact_checker`, `proofreader`).
   - If transient overlay is active and unexpired, read transient role chain as
     an overlay.
   - If user changes persistent role, update `runtime_state.active_default_role`.
5) Certification gate
   - Request approval before any tool usage or edits.
   - Approval must include the exact token `CERTIFY: APPROVED`.
6) Post-cert work execution
   - Use `tickets/epics/`, `tickets/stories/`, and `tickets/tasks/` for all
     work.
   - Route from `attention_board.md` and resume from linked ticket notes.
   - Re-read architecture/components docs before major work.
   - Keep `attention_board.md` current for routing and ticket notes current for
     durable findings.
   - Trigger compaction/re-onboarding when step window is reached (`runtime_state.step.current >= runtime_state.step.next_reonboard_step` - comparing injected Step ID to YAML threshold):
     - Immediately log a `BLOCKER` to `attention_board.md` requiring `REONBOARD`.
     - Halt all work and execute the re-onboarding checklist.
     - Clear the `BLOCKER` after successful certification.

References
- `GEMINI.MD`
- `config/context_compass_config.yaml`
- `context_compass/SKILLS.md`



