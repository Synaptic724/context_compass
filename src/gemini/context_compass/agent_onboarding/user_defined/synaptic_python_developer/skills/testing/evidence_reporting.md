

# evidence_reporting

Purpose
- Enforce truthful reporting of tests and checks.

Validation Truthfulness
* Never claim tests/lint/type-checks were run unless they were actually run.
* If validation is skipped, say explicitly: "Not run."
* If fast checks exist, recommend the exact commands - but do not pretend they happened.

Truthful Validation Reporting
When reporting validation status:
* Only claim unit/integration/coverage runs if you actually ran them.
* If not run, say "Not run."
* If recommending commands, be specific and repo-consistent (e.g., pytest, pytest -q, pytest -m integration, pytest --cov). Do not invent a workflow that contradicts repository docs.

Rules
- Never claim tests ran unless they actually ran.
- If tests were not run, report: "Not run."
- Suggest repo-consistent commands when needed.
- If coverage was not measured, say so explicitly.

Example commands
- pytest
- pytest -q
- pytest -m integration
- pytest --cov

References
- agent_onboarding/default/general/README.md



