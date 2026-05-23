
# defect_severity_policy

Purpose
- Define consistent defect severity classification.

Severity levels (suggested)
- P0 / Critical:
  - data loss, security exposure, major outage, incorrect core behavior with no workaround.
- P1 / High:
  - major feature broken, frequent crashes, severe performance regressions.
- P2 / Medium:
  - incorrect edge-case behavior, partial degradation, non-critical errors.
- P3 / Low:
  - cosmetic issues, minor inconveniences, easy workaround.

Rules
- Severity must be justified by impact and frequency.
- If unsure, mark UNKNOWN and request more info.

References
- `agent_onboarding/default/general/skills/unknowns_gate_reference.md`


