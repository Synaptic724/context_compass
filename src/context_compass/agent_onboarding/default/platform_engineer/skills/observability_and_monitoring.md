
# observability_and_monitoring

Purpose
- Make operational behavior measurable and debuggable.

Minimum observability set
- Logs:
  - structured where possible,
  - correlation IDs for request flows.
- Metrics:
  - throughput, latency, error rates,
  - resource utilization (CPU/memory).
- Traces (when available):
  - service boundaries and critical paths.

SLO thinking (lightweight)
- Define what "good" looks like (targets).
- Define alerts for "bad" (thresholds and paging rules).

Rules
- New critical behavior requires new or updated observability.
- If you cannot observe it, you cannot operate it.

References
- `agent_onboarding/default/platform_engineer/skills/incident_response_and_runbooks.md`


