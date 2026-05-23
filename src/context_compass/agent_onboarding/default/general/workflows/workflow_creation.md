# Workflow: workflow_creation

## Metadata
- Workflow ID: WF-workflow-creation
- Status: active
- Owner: user
- Allowed Roles:
  - general
  - engineer
  - design_engineer
  - user_defined/*
- Default Roles:
- Trigger:
  - user explicitly asks to create a workflow
- Created: 2026-04-26T12:32:40Z
- Updated: 2026-04-26T12:32:40Z

## Purpose
Scaffold a new role-local workflow from the simple or advanced template and
register it in the target role `WORKFLOWS.MD`.

## Use When
- The user explicitly asks to create a workflow.

## Do Not Use When
- The user has not explicitly asked for workflow creation.

## Required Reads
- `templates/workflow_simple_template.md`
- `templates/workflow_advanced_template.md`
- target role `WORKFLOWS.MD`

## Required Skills
- `agent_onboarding/default/general/skills/role_local_workflows.md`

## Context / Handoff Summary
This workflow is on-demand only. It should be used when the user explicitly
asks to create a workflow.
