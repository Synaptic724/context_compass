# Example: security_engineer review flow

Scenario
- Review a change touching onboarding and automation guidance.

Workflow
1. Scope trust boundaries
- identify where user input can influence commands.

2. Threat review
- misuse of elevated commands
- accidental secret leakage in artifacts

3. Mitigation checks
- ensure escalation requires explicit approval
- ensure docs ban secret logging

4. Residual risk report
- list accepted and unaccepted risks

Expected outputs
- threat summary
- mitigation checklist
- residual risk decisions