
# adr_and_decision_hygiene

Purpose
- Keep architecture decisions durable, searchable, and explainable.
- Prevent re-litigating decisions after compaction/handoffs.

When to write a decision record (ADR or ticket-linked decision)
- Any change to:
  - public API contracts,
  - persistent schemas/data models,
  - component boundaries and ownership,
  - lifecycle invariants and cleanup behavior,
  - cross-cutting behavior (auth, caching, retries, observability).
- Any decision that is hard to reverse.

ADR template (minimal)
- Title:
- Status: proposed | accepted | superseded
- Context:
- Decision:
- Options considered:
- Tradeoffs:
- Consequences:
- Rollout/migration:
- Test/validation:
- Links: tickets, code, docs

Rules
- One ADR = one decision.
- Link ADR to the ticket that implements it.
- If superseded, link to the newer ADR and keep the old one for history.

References
- `agent_onboarding/default/design_engineer/policies/decision_record_policy.md`
- `agent_onboarding/default/design_engineer/examples/adr_example.md`


