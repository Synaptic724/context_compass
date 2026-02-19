
# ci_cd_and_release

Purpose
- Define CI/CD pipeline and release discipline.

Pipeline principles
- Make pipelines deterministic:
  - lock versions where possible,
  - avoid environment-dependent behavior.
- Prefer smaller stages with clear artifacts over one giant stage.
- Fail fast on:
  - formatting/lint,
  - unit tests,
  - static analysis,
  - security checks when required.
- Keep secrets out of logs and out of repo.

Release discipline
- Prefer reproducible builds.
- Tag/label releases with traceable identifiers.
- Ensure rollback instructions exist for any release mechanism.

References
- `agent_onboarding/default/platform_engineer/policies/operational_safety_policy.md`
- `agent_onboarding/default/general/skills/security_and_secrets.md`


