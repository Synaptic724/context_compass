

# SKILLS.MD - engineer

Purpose
- Define required baseline engineering skills for the `engineer` role.

Inheritance
- `INHERITS_SKILLS_FROM: agent_onboarding/default/general/SKILLS.MD`

Skill classes (non-negotiable)
- This role defines two classes of skills:
  A) **Required baseline skills** (always required for onboarding/certification)
  B) **On-demand system-context skills** (required only when the active task triggers them)

Rules
- You MUST read **all** paths listed under **Required baseline skills** for this role
  to be considered onboarded/certifiable as `engineer`.
- You MUST NOT claim an on-demand skill was read unless:
  1) a trigger condition was met, AND
  2) you actually read it in full.
- When a trigger condition is met, the on-demand skills become mandatory and MUST be
  read **before** any work in that scope.

Required baseline skills
- `agent_onboarding/default/engineer/AGENTS.MD`
- `agent_onboarding/default/engineer/WORKFLOWS.MD`
- `agent_onboarding/default/engineer/skills/engineer_execution.md`
- `agent_onboarding/default/engineer/skills/technical_expertise.md`
- `agent_onboarding/default/engineer/skills/system_orientation.md`
- `agent_onboarding/default/engineer/skills/documentation_standards.md`
- `agent_onboarding/default/engineer/skills/context_protocol.md`
- `agent_onboarding/default/engineer/skills/src_graph_usage.md`
- `agent_onboarding/default/engineer/skills/src_graph_generation.md`
- `agent_onboarding/default/engineer/skills/system_document_build.md`
- `agent_onboarding/default/engineer/skills/patch_framework_gating.md`
- `agent_onboarding/default/engineer/skills/patch_artifact_consumption.md`
- `agent_onboarding/default/engineer/skills/staleness_protocol.md`
- `agent_onboarding/default/engineer/policies/engineer_quality_policy.md`
- `agent_onboarding/default/engineer/policies/ctx_autonomy_policy.md`
- `agent_onboarding/default/engineer/policies/ctx_autonomy_rubric.md`
- `agent_onboarding/default/engineer/behavioral_guidelines/engineer_workflow.md`
- `agent_onboarding/default/engineer/behavioral_guidelines/task_execution_and_validation.md`
- `agent_onboarding/default/engineer/examples/artifact_workflow.md`
- `agent_onboarding/default/engineer/examples/eng_task_flow.md`

On-demand system-context skills
Trigger conditions (any one makes these mandatory):
- The active ticket requires architecture/system documentation work.
- The task touches `system_docs/` or claims about system/runtime/test architecture are required.
- You are changing cross-cutting behavior that depends on documented architecture or component boundaries.
- The user explicitly requests an architecture/components/tests deep dive.
- `system_docs/` is empty, or you cannot tell whether its contents describe this repository.
- You are cleaning, upgrading, or preparing a Context Compass install for
  distribution. Those operations delete and replace files, so the skill that
  governs them is mandatory before you run either tool.

If triggered, you MUST read:
- `system_docs/system_docs_read_first.md`

Then read whichever of these exist in THIS repository. None of them ship with the
package, so in a fresh install there is nothing here to read:
- `system_docs/src_architecture.md`
- `system_docs/src_components.md`
- `system_docs/tests_architecture.md`
- `system_docs/tests_components.md`

RAISE TO USER THE BELOW DOCUMENTS AND ASK IF REQUIRED TO READ:
- `system_docs/src_graph.md`

If you are cleaning or upgrading an install:
- `agent_onboarding/default/engineer/skills/package_maintenance.md`

Note on a fresh install
- **`system_docs/` ships empty.** The package does not seed architecture,
  component, test or graph documents, because a shipped placeholder in a live
  lane gets read as repository truth no matter what banner sits on top of it.
- `examples/` is where the shape and quality bar live. Read the examples to learn
  the format; write `system_docs/` from your own repository.
- An empty `system_docs/` is the expected state of a new install, not a defect,
  and not something to fill with invented content.
- `system_docs/system_docs_read_first.md` is the entry point and explains the
  order to build these in when the repository is ready.

Note on the source graph
- `system_docs/src_graph.md` and `system_docs/src_graph_index.md` are generated
  per project by `tools/system_documents/python/` and are NOT shipped with this
  package. A fresh install has neither.
- If they are absent, that is expected. Do not treat their absence as a blocked
  onboarding or a missing required read.
- NEVER read `src_graph.md` in full. Read `src_graph_index.md`, verify it, and
  slice only the sections you need. See
  `agent_onboarding/default/engineer/skills/src_graph_usage.md`.
