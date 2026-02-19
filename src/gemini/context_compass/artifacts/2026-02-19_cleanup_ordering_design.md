# cleanup_ordering_design

Purpose
- Capture the design rationale for cleanup ordering contract.

Decision
- Keep logger cleanup last to preserve diagnostic coverage during failures.

Validation
- Add/verify ordering regression test in integration suite.