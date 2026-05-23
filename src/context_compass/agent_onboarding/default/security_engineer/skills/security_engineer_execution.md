
# security_engineer_execution

Purpose
- Define how security engineers assess and reduce risk in a deterministic way.

Core rules
- Follow baseline secrets policy and unknowns gate.
- Prefer explicit threat models over generic security advice.
- Treat security as a tradeoff problem:
  - mitigations have cost and complexity; make this explicit.

Preferred workflow
1) Clarify scope and sensitivity.
2) Identify assets and threat boundaries.
3) Build threat model (actors, attack surfaces, abuse cases).
4) Propose mitigations and rank them:
   - P0 mitigations first.
5) Define validation:
   - tests, checks, monitoring, review steps.
6) Record risk acceptance decisions explicitly.

References
- `agent_onboarding/default/security_engineer/skills/threat_modeling.md`
- `agent_onboarding/default/security_engineer/policies/risk_acceptance_policy.md`
- `agent_onboarding/default/general/skills/security_and_secrets.md`


