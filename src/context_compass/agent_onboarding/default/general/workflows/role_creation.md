# Workflow: role_creation

## Metadata
- Workflow ID: WF-role-creation
- Status: active
- Owner: user
- Allowed Roles:
  - general
  - engineer
  - design_engineer
  - user_defined/*
- Default Roles:
- Trigger:
  - user explicitly asks to create a new role or class
- Created: 2026-04-26T12:32:40Z
- Updated: 2026-04-26T12:32:40Z

## Purpose
Scaffold a new role or class correctly:
- create the role-local docs
- register the role
- sync tickets and patch artifacts

## Use When
- The user explicitly asks to create a role or class.

## Do Not Use When
- The user has not explicitly asked for role creation.

## Required Reads
- `PROFILE_CLASS_CREATION_GUIDE.md`
- `templates/workflow_simple_template.md`

## Required Skills
- `agent_onboarding/default/general/skills/role_local_workflows.md`

## Context / Handoff Summary
This workflow is on-demand only. It should be used when the user explicitly
asks to create a role or class.
