# Example: platform_engineer task flow

Scenario
- Add a CI stage that runs architecture reference checks before merge.

Workflow
1. Intake
- Identify pipelines, environments, and rollback path.

2. Plan
- Add lightweight check stage after unit tests.

3. Implement
- Update pipeline config and required scripts.

4. Validate
- Run pipeline in dry-run branch.
- Confirm failure behavior when refs break.

5. Handoff
- Document operational risk and rollback command.

Expected outputs
- pipeline config diff
- release note entry
- operational runbook update