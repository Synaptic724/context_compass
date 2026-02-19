

# security_and_secrets

Purpose
- Enforce a strict no-secrets-in-repo policy.
- Provide safe alternatives for secret handling during agent work.
- Define refusal conditions when a user requests unsafe storage.

Non-negotiable rules
- Never store secrets anywhere in the repo, including `agent_onboarding/`, `tickets/epics/`,
  `tickets/stories/`, `tickets/tasks/`, `tickets/epics/completed/`, `tickets/stories/completed/`, `tickets/tasks/completed/`,
  `completed/`, and `artifacts/`.
- Never write secrets into tickets, docs, or logs.
- Never commit secrets, even temporarily, even in test data.
- If a user requests storing secrets in-repo, refuse and ask for a safe alternative.

What counts as a secret
- Credentials (API keys, tokens, passwords, cookies).
- Private keys, certificates, or access URLs with embedded credentials.
- Internal endpoints that include authentication material.
- Any value the user labels as secret/confidential.

Approved alternatives
- Environment variables injected at runtime.
- OS keychain or secret manager (1Password, Keychain, Vault, etc.).
- CI/CD secret store or runtime injected config.
- Runtime-only prompts (no persistence, no logging).

Refusal protocol (required)
- State that storing secrets in-repo is not allowed.
- Provide at least one safe alternative and ask for confirmation.
- Do not proceed with any write that would persist the secret.

Logging and output hygiene
- Do not print secrets to stdout/stderr.
- If a secret appears in input, do not echo it back.
- Mask or omit secrets in examples and documentation.

References
- `AGENTS.MD`



