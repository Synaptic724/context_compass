# Example: design_engineer task flow (repo-based)

Scenario
- Story: raise release-readiness doc quality so users can execute this workflow
  from this repository without hidden assumptions.

Entry gate
- Confirm design-first scope and clear boundaries before implementation edits.

Design workflow
1. Problem framing
- Define failures: shallow examples, stale slugs, unclear chain.

2. Current-state evidence
- Review templates, current examples, and system docs.

3. Option set
- Option A: patch only links.
- Option B: rewrite as full repo-based chain.

4. Tradeoff analysis
- Option A is faster but weak.
- Option B is durable and reusable for release hardening.

5. Proposed design
- Pick Option B.
- Define epic/story/task/artifact naming and acceptance gates.

6. Ticketization
- One story, one implementation task, retained overview artifact.

Expected outputs
- design rationale in ticket notes and ADR
- artifact: `examples/example_completed/2026-02-19_context_compass_release_overview_artifact.md`
- explicit approval checkpoint before final closure
