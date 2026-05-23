
# data_modeling

Purpose
- Provide a disciplined approach to data modeling, schemas, and migrations.
- Ensure designs are correct under concurrency, growth, and change.

Modeling checklist
- Entities and relationships
- Ownership boundaries (which component owns which data)
- Consistency model:
  - strong consistency vs eventual consistency,
  - transaction boundaries,
  - conflict resolution.
- Query patterns:
  - expected reads/writes,
  - indexing strategy,
  - cardinality and growth expectations.
- Migration plan:
  - backward compatible steps,
  - data backfill strategy,
  - rollback/backout plan.

Design questions
- What is the source of truth for each field?
- What invariants must hold?
- What are the failure modes during migration?
- How will you validate data correctness post-migration?

References
- `agent_onboarding/default/design_engineer/skills/nonfunctional_requirements.md`
- `agent_onboarding/default/qa_engineer/skills/test_data_and_environments.md`


