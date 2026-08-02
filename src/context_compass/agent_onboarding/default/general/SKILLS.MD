

# SKILLS.MD - general

Purpose
- Define active baseline skills for the `general` role.

Inheritance
- `INHERITS_SKILLS_FROM: none`

Activation rule
- All paths listed below are active skills for this role.
- YOU MUST READ ALL PATHS BELOW for all these skills to be considered active.

Active skills
- `agent_onboarding/default/general/AGENTS.MD`
- `agent_onboarding/default/general/skills/general.md`
- `agent_onboarding/default/general/skills/execution_contract.md`
- `agent_onboarding/default/general/skills/compaction_requirements.md`
- `agent_onboarding/default/general/policies/policy_skills.md`
- `agent_onboarding/default/general/skills/agent_stance.md`
- `agent_onboarding/default/general/skills/agent_lifecycle.md`
- `agent_onboarding/default/general/skills/agent_identity.md`
- `agent_onboarding/default/general/skills/career_selection.md`
- `agent_onboarding/default/general/skills/mrp_policy.md`
- `agent_onboarding/default/general/skills/configuration_standards.md`
- `agent_onboarding/default/general/skills/package_upgrade.md`
- `agent_onboarding/default/general/skills/context_gold.md`
- `agent_onboarding/default/general/skills/security_and_secrets.md`
- `agent_onboarding/default/general/skills/repo_topology.md`
- `agent_onboarding/default/general/skills/ticketing.md`
- `agent_onboarding/default/general/skills/ticketing_skill_contract.md`
- `agent_onboarding/default/general/skills/memory_management.md`
- `agent_onboarding/default/general/skills/reactive_documentation.md`
- `agent_onboarding/default/general/skills/active_documentation.md`
- `agent_onboarding/default/general/skills/context_window_budget.md`
- `agent_onboarding/default/general/skills/active_pointerboard.md`
- `agent_onboarding/default/general/skills/mailbox_protocol.md`
- `agent_onboarding/default/general/skills/ticket_closure_attention_sync.md`
- `agent_onboarding/default/general/skills/unknowns_gate_reference.md`
- `agent_onboarding/default/general/skills/self_certification.md`
- `agent_onboarding/default/general/skills/user_approved_certification.md`
- `agent_onboarding/default/general/skills/ticket_microcycle.md`
- `agent_onboarding/default/general/skills/workflow.md`
- `agent_onboarding/default/general/skills/role_local_workflows.md`
- `agent_onboarding/default/general/WORKFLOWS.MD`
- `agent_onboarding/default/general/workflows/cleanup_context_compass.md`
- `agent_onboarding/default/general/workflows/start_context_compass_work.md`
- `agent_onboarding/default/general/workflows/turn_in_selected_tickets.md`
- `agent_onboarding/default/general/workflows/sync_attention_board.md`
- `agent_onboarding/default/general/skills/context_compaction.md`
- `attention_board.md`
- `artifact_board.md`
- `agent_onboarding/default/general/skills/context_management.md`
- `context_management/context_board.md`

Note on the three board paths above. `attention_board.md`, `artifact_board.md` and
`context_management/context_board.md` are baseline reads, but they are **live
mutable state, not policy**. You open them to learn what is happening right now, not
to learn a rule. They therefore satisfy `READ_INTEGRITY_PROOF` by naming current
state rather than a rule callout - see the live-state clause in
`agent_onboarding/default/general/skills/compaction_requirements.md`. Do not invent
a rule to quote from a routing table.
- `agent_onboarding/default/general/behavioral_guidelines/agent_lifecycle_and_heartbeat.md`
- `agent_onboarding/default/general/behavioral_guidelines/work_intake_and_execution.md`
- `agent_onboarding/default/general/behavioral_guidelines/onboarding_summary.md`

On-demand skills
Read only when the trigger is met. Not part of the baseline, and claiming one
was read without meeting its trigger is a false attestation.

**This applies to sections labelled `On-demand`, which is the trigger-gated state.
It is not a rule about everything outside baseline.** A `Self-directed` section is
also outside baseline but has no trigger and needs no permission - waiting for one
there is the failure, not the discipline. `engineer` carries such a section for its
system documents. Three states, defined in `context_compass/SKILLS.MD`.

- `agent_onboarding/default/general/skills/llm_full_usage.md`
  - Trigger: `llm_full.md` exists at the repository root and you are about to
    read from it, or you have been asked to regenerate it.
  - Why it is on-demand: most installs have no `llm_full.md` - it is a view of
    the package produced for whole-system review, not something the package
    ships. Reading the skill when the file is absent teaches a procedure with
    nothing to apply it to.
  - Why it is not optional once triggered: the document is ~27,000 lines. The
    skill exists to stop you reading it whole when a 450-line index would have
    told you the exact range.





