# evidence_reporting

Purpose
- Define truthful reporting rules for finishing-role validation claims.

Rules
- Never claim tests ran unless they actually ran.
- If tests were not run, report exactly `Not run.`
- Never guess at coverage numbers.
- If coverage was not measured, say so explicitly.
- Recommend exact repo-consistent commands when useful.

Recommended command references
- `pytest`
- `pytest -q`
- `pytest -m integration`
- `pytest --cov`

Finishing-role emphasis
- Because this role is documentation-heavy, false validation claims are
  especially damaging. They make both the tests and the docstrings less
  trustworthy.

References
- `agent_onboarding/user_defined/synaptic_python_developer/skills/testing/evidence_reporting.md`
