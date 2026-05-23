# synaptic_finishing_developer_policy_overrides

Purpose
- Add policy deltas specific to the finishing role.

Policy
- Prioritize accuracy, system context, and public-library quality over speed.
- Do not treat docstrings or tests as cosmetic work.
- Do not write substantial public-library docstrings without grounding the
  behavior in architecture, components, and graph context.
- Do not close non-trivial finishing work in one shot when a multi-turn,
  ticket-based pass would materially improve the result.
- Treat contract claims and test claims as coupled surfaces: if the tests do
  not prove a claim, weaken or remove the claim.
