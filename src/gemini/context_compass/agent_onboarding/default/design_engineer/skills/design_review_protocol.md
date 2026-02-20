
# design_review_protocol

Purpose
- Define how designs are reviewed, validated, and approved before implementation.
- Ensure the handoff is deterministic and non-performative.

Review steps (recommended)
1) Problem framing step
   - verify goal/non-goals, constraints, and acceptance criteria.
2) Architecture step
   - verify boundaries, interfaces, data model, and tradeoffs.
3) Operational step
   - verify rollout, observability, failure handling, and test strategy.
4) Implementation readiness step
   - verify tickets are actionable and scoped.

Review artifacts
- For any review, provide:
  - a concise summary,
  - explicit open questions,
  - explicit decision points requiring approval.

Rules
- Do not start implementation unless a review step is explicitly approved when:
  - design changes public contracts, schemas, or major boundaries,
  - the user requested "design only" first,
  - risk is high or rollback is complex.

References
- `agent_onboarding/default/design_engineer/policies/design_review_policy.md`
- `agent_onboarding/default/general/skills/ticketing_skill_contract.md`


