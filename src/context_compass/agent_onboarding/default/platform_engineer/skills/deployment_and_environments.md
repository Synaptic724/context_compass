
# deployment_and_environments

Purpose
- Provide deployment and environment discipline with safe rollout patterns.

Deployment checklist
- Environment targets (dev/staging/prod)
- Configuration changes (what keys, where stored, how rolled back)
- Rollout steps (phased if needed)
- Backout plan (explicit and tested when possible)
- Verification signals (what proves success)
- Monitoring/alerts (what proves safety)

Safe rollout patterns
- Phased rollout (canary/percent)
- Feature flags
- Blue/green where supported
- Backward compatible schema/config changes

References
- `agent_onboarding/default/platform_engineer/skills/observability_and_monitoring.md`
- `agent_onboarding/default/platform_engineer/policies/production_change_management_policy.md`


