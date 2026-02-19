
# decision_record_policy

Purpose
- Require durable decision recording for high-impact architecture/design changes.

Policy
- When a design decision changes:
  - public APIs,
  - schemas/data models,
  - component boundaries/ownership,
  - lifecycle invariants,
  - cross-cutting behavior (auth/retries/caching/observability),
  you MUST record the decision as an ADR or ticket-linked decision artifact.
- The decision record must include:
  - context, decision, options, tradeoffs, consequences, validation, rollout.
- Do not proceed to implementation until decision recording is complete
  when the change is hard to reverse.

References
- `agent_onboarding/default/design_engineer/skills/adr_and_decision_hygiene.md`


