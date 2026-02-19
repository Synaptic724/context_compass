
# system_design_method

Purpose
- Provide a consistent structure for software/system design artifacts.
- Ensure designs cover components, data flows, failure modes, and operability.

Design skeleton (use as headings)
1) Context
   - current system summary (with evidence),
   - problem statement and goals.
2) Constraints
   - compatibility, performance, reliability, security, timeline.
3) Proposed architecture
   - components and responsibilities,
   - boundaries (what depends on what),
   - data flows and control flows.
4) Interfaces and contracts
   - APIs, schemas, events, error semantics, versioning.
5) State and data model
   - entities, relationships, consistency model, migrations.
6) Failure modes and resilience
   - what can fail, how it is detected, how it recovers.
7) Observability and operability
   - logs/metrics/traces, dashboards, runbooks, alerting.
8) Testing and validation
   - unit/integration/e2e, invariants, test data strategy.
9) Rollout and migration plan
   - deploy phases, feature flags, backouts, compatibility windows.
10) Risks and open questions
   - explicit UNKNOWNs and risk acceptance points.
11) Ticketization
   - break into tasks with clear deliverables and dependencies.

Rules
- Prefer explicit diagrams (even ASCII) when it clarifies components and flows.
- Keep each component description atomic: one responsibility cluster per component.
- If you cannot justify a boundary or dependency, mark as UNKNOWN and verify.

References
- `agent_onboarding/default/design_engineer/skills/decomposition_and_boundaries.md`
- `agent_onboarding/default/design_engineer/skills/nonfunctional_requirements.md`
- `agent_onboarding/default/design_engineer/skills/design_review_protocol.md`


