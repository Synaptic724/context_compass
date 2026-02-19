

# unknowns_gate_reference

Purpose
- Provide one canonical onboarding source for UNKNOWN/FACT evidence discipline.

Unknowns Gate (No Unverified Claims)
- Any statement not supported by evidence is UNKNOWN.
- UNKNOWN is the default claim state for new findings.
- Evidence means at least one of:
  - A specific source file reference (preferred: file + symbol/method/class name).
  - A citation to an explicit, already-verified artifact (for example, an approved doc section).
- If not evidenced => UNKNOWN.
- UNKNOWN items must be labeled UNKNOWN (or added to an Unknowns section).
- UNKNOWN items must be investigated by reading the relevant source(s).
- If investigation cannot be completed (missing source access, ambiguity, or time),
  the item must remain UNKNOWN and must not be promoted to FACT.
- No reasonable assumptions.
- Do not infer behavior from naming, patterns, conventions, or typical frameworks.
- Only code/docs count as evidence.

Operating workflow
1) Start new claims as UNKNOWN.
2) Identify evidence target (file + symbol).
3) Capture reproducible evidence (`path:start_line-end_line` or verified-doc citation).
4) Promote to FACT only when evidence directly supports the claim.
5) If blocked, keep UNKNOWN and record the blocker.

Evidence quality checklist
- Specific: concrete symbols/sections, not broad file assumptions.
- Sufficient: evidence directly supports the exact claim.
- Current: evidence matches current repository state.
- Traceable: another reader can reopen evidence quickly.

Local override rule
- Local docs may extend this policy for domain-specific enforcement.
- Do not duplicate the full Unknowns Gate block unless a documented override is required.

Disallowed shortcuts
- Treating naming conventions as proof.
- Promoting tentative conclusions to FACT without evidence.

References
- `context_compass/AGENTS.MD`
- `context_compass/agent_onboarding/default/general/skills/execution_contract.md`




