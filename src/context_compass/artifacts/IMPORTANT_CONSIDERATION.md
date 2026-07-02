# IMPORTANT_CONSIDERATION

## Metadata
- Artifact ID: ART-EXAMPLE-important-consideration
- Status: reference_example

## Purpose
Show the shape of a narrow, high-signal artifact that captures one unresolved
design or runtime question without pretending the answer is already known.

This file is intentionally generic. It is a sample artifact structure for
Context Compass users who want to record one important open issue with durable
context.

## When To Use A Note Like This
- A design question is important enough to deserve its own artifact.
- The question cuts across more than one subsystem or ticket.
- The team needs a durable investigation anchor before implementation
  continues.

## Example Question Shape
- how should one unresolved runtime or architecture boundary behave when
  multiple subsystems interact?

## Good Artifact Behavior
- Stay focused on one question.
- Separate facts, pressures, and open questions.
- Avoid pretending that unknown semantics are already settled.
- Link the artifact back to exactly one active ticket or investigation lane.

## Suggested Sections
- current pressure or trigger
- runtime or design anchors
- hard semantic questions
- candidate rules
- source anchors
- current best summary

## Non-Goals
- This is not a full architecture document.
- This is not a dumping ground for every open issue.
- This should not contain private repository paths or project-specific jargon
  unless the artifact is intentionally repo-local and not meant for release.
