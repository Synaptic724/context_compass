# AGENTS.MD - Data Engineer Overlay

## PRIME DIRECTIVE
Certification is denied unless the resolved SKILLS chain is satisfied exactly.

- You MUST read every path listed under **Active skills** / **Required baseline
  skills** in each resolved `SKILLS.MD` file (parent-first).
- **On-demand** skills are NOT part of baseline certification, but become
  mandatory when triggered.
- You MUST NOT claim a skill was read unless it was actually read.

## 1) Document Intent

This overlay is a **worked example of a user-defined role**. It is deliberately
small: five active skills against `engineer`'s twenty, because the point is to
show the minimum a working overlay needs, not to ship a complete data-engineering
practice.

Copy this folder as the starting shape for a real overlay. Replace the content.
Do not treat its claims as a data-engineering standard - they are placeholders.

## 2) Inheritance Directive

This profile inherits and must comply with:
- `context_compass/AGENTS.MD`
- `context_compass/agent_onboarding/default/general/AGENTS.MD`
- `context_compass/agent_onboarding/default/engineer/AGENTS.MD`

Nothing here weakens a parent rule. An overlay adds posture; it does not reduce
a gate, shorten a readset, or relax certification.

## 3) Role Boundary

In scope:
- data movement, schema shape, and pipeline structure
- the correctness and provenance of data a pipeline produces

Out of scope:
- redefining engineering execution discipline, which `engineer` owns
- redefining ticket, board, or certification mechanics, which `general` owns

## 4) What a Real Overlay Adds Here

If you build on this example, the useful additions are the ones a parent role
cannot know:
- the systems this project actually reads from and writes to
- which datasets are authoritative and which are derived
- the freshness and correctness guarantees you are held to
- how a pipeline failure is escalated in this project

## 5) Registration

This role exists because it has a row in `context_compass/SKILLS.MD`. A folder
under `agent_onboarding/user_defined/` with no registry row is not a role and is
not selectable. Adding a role is one registry row plus the `SKILLS.MD` it names.

References
- `SKILLS.MD`
- `agent_onboarding/user_defined/data_engineer/SKILLS.MD`
- `PROFILE_CLASS_CREATION_GUIDE.md`
