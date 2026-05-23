
# nonfunctional_requirements

Purpose
- Ensure designs address non-functional requirements (NFRs) explicitly.
- Prevent late surprises in performance, reliability, security, and operability.

NFR categories (minimum coverage)
1) Performance
   - latency budgets, throughput expectations, hotspots, caching.
2) Scalability
   - growth assumptions, horizontal scaling limits, state management.
3) Reliability
   - failure modes, retries, idempotency, recovery, backpressure.
4) Operability
   - logging/metrics/tracing, alerting, runbooks, debugging hooks.
5) Security & Privacy
   - threat model, secrets handling, least privilege, data exposure.
6) Cost
   - compute/storage/network cost drivers, guardrails.

Rules
- If an NFR is unknown, declare it UNKNOWN and propose a verification step.
- If the user cares about an NFR, translate it into measurable acceptance criteria.
- If security posture is required, route to security specialist guidance:
  - `agent_onboarding/default/general/skills/security_and_secrets.md`
  - `agent_onboarding/default/security_engineer/SKILLS.MD` (if available/selected)

References
- `agent_onboarding/default/general/skills/unknowns_gate_reference.md`
- `agent_onboarding/default/platform_engineer/skills/observability_and_monitoring.md`
- `agent_onboarding/default/security_engineer/skills/threat_modeling.md`


