# comment_craft

Purpose
- Define how this role writes comments that preserve contract understanding
  instead of narrating obvious code.

Comment mission
- Comments exist to explain the non-obvious:
  - why a branch exists
  - why an ordering constraint matters
  - why a lock or gate is necessary
  - why cleanup happens in a particular order
  - why one collaborator is used instead of another

Good comment targets
- synchronization boundaries
- lifecycle transitions
- cleanup cascades
- publication or cache invalidation side effects
- contract caveats that are easy to break in refactors
- intentionally asymmetric behavior

Bad comment targets
- restating the next line of code
- narrating trivial assignments
- repeating the docstring with no new value
- stale historical notes with no current contract relevance

Commenting rules
- Preserve useful existing comments.
- Update stale comments instead of deleting them silently.
- Prefer one targeted high-signal comment over a block of noise.
- When behavior is system-sensitive, explain the system reason, not just the
  local mechanics.

Examples of high-value comment intent
- “Hold the room lock across both state updates so the viewer never observes a
  half-refreshed projection set.”
- “Clean the child registry before nulling the descriptor cache so later
  teardown cannot publish stale records.”

Finishing check
- If the comment disappeared, would a future maintainer likely break the
  contract?
  - if yes, keep or improve it
  - if no, it probably should not exist

References
- `system_docs/src_components.md`
- `system_docs/src_graph.md`
- `agent_onboarding/user_defined/synaptic_python_developer/skills/python/comments.md`
