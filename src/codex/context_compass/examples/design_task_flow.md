# Example: design_engineer task flow

Scenario
- Story: add deterministic cleanup ordering to reduce flaky shutdown failures.

Entry gate
- Confirm design-only scope before implementation.

Design workflow
1. Problem framing
- Define non-goals and compatibility constraints.

2. Current-state evidence
- Read existing docs, ticket history, and key code paths.

3. Option set
- Option A: minimal ordering change.
- Option B: full lifecycle refactor.

4. Tradeoff analysis
- Compare risk, implementation effort, and rollback complexity.

5. Proposed design
- Document component boundaries and lifecycle contract.

6. Ticketization
- Story + task split with acceptance criteria and validation plan.

Expected outputs
- design summary in active ticket notes
- optional artifact: `artifacts/*_cleanup_ordering_design.md`
- explicit approval checkpoint before coding