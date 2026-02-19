# Example: qa_engineer task flow

Scenario
- Validate release-readiness after doc and routing changes.

Workflow
1. Risk review
- Identify critical paths: onboarding, role routing, references.

2. Test strategy
- contract checks: missing refs
- workflow checks: ticket-note lifecycle
- regression checks: adapter entrypoints

3. Execute
- Run reference scan and targeted smoke checks.

4. Report
- Findings ordered by severity with file references.

5. Gate
- Recommend `go` or `no-go` with residual risk list.

Expected outputs
- quality summary note
- defect list or explicit no-findings statement