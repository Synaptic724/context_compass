
# architecture_tradeoffs

Purpose
- Make tradeoffs explicit, comparable, and reviewable.
- Prevent "default architecture" choices from being made without rationale.

Minimum tradeoff set
For any non-trivial design, capture:
- Option A (baseline / simplest approach)
- Option B (preferred approach)
- Option C (if relevant: higher complexity / higher leverage)

Tradeoff dimensions (use as a table)
- Value delivered
- Complexity
- Time to implement
- Operational risk
- Performance/scalability
- Reliability/resilience
- Security/privacy risk
- Testability
- Maintainability

Rules
- If you cannot justify the chosen option on at least 2-3 dimensions, stop and gather more evidence.
- If a tradeoff is a risk acceptance, label it as such and request approval.

References
- `agent_onboarding/default/design_engineer/policies/decision_record_policy.md`
- `agent_onboarding/default/design_engineer/skills/adr_and_decision_hygiene.md`


