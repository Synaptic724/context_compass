

# cleanup_and_disposal

Purpose
- Enforce deterministic, idempotent cleanup with explicit nulling.

Cleanup / Teardown Discipline (Immediately After Initialization)

Cleanup is a core part of this library's correctness contract.
* Cleanup must be deterministic and idempotent.
* Prefer object teardown: call cleanup() on child objects, then null references to assist GC and prevent use-after-clean.
* Look at existing implementations of the class for patterns to better understand requirements. We cleanup everything; do not leave it to the GC.
* Logger teardown last.
* Do not use placeholder comments like "already nulled above." Write the actual null assignments.

Cleanup nulling contract:
* After cleaning children, explicitly set every relevant field/reference to None.
* If a field is not nulled, that must be intentional and documented.

Post-cleanup usage rule
* If a class implements cleanup, assume the object is not used after cleanup completes.
* Prefer `self.check_cleaned()` and allow it to throw for methods that require a live object.
* Only use `if self._cleaned: return` when the method must be non-throwing by contract.
* Do NOT snapshot `self._field` into locals unless absolutely necessary and justified.
* Do NOT guard internal fields with `if x is None` when lifecycle guarantees they exist pre-cleanup.
* `None` checks are for external inputs or truly optional state only.

Rules
- Cleanup implemented immediately after __init__.
- If using cleanable ensure you set all fields to None after cleanup except the _cleaned bool flag.
- Cleanup must be idempotent and safe to call multiple times.
- Use a lock when cleanup can race with active work; check _cleaned before and after locking.
- Tear down child objects before clearing own fields.
- Null all relevant references after cleanup.
- Logger teardown is always last.
- Do not rely on GC for owned resources.
- Document cleanup ordering and ownership in the docstring.

Checklist
- Guard against double cleanup.
- Acquire lock, then re-check _cleaned.
- Cleanup children in dependency order.
- Null the lock after guarded teardown.
- Null all fields explicitly.
- Logger cleanup last.

Example order
1) if _cleaned: return
2) with lock: re-check _cleaned, then cleanup children
3) child = None
4) lock = None
5) logger.cleanup() (last)
6) logger = None

Examples
- agent_onboarding/user_defined/synaptic_python_developer/examples/python/cleanup_patterns.py





