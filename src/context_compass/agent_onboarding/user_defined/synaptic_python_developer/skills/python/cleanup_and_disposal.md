

# cleanup_and_disposal

Purpose
- Enforce deterministic, idempotent cleanup with explicit post-teardown field policy.

Cleanup / Teardown Discipline (Immediately After Initialization)

Cleanup is a core part of this library's correctness contract.
* Cleanup must be deterministic and idempotent.
* Prefer object teardown: call cleanup() on child objects, then delete owned
  references to drop the live surface and prevent use-after-clean.
* Look at existing implementations of the class for patterns to better understand requirements. We cleanup everything; do not leave it to the GC.
* Logger teardown last.
* Do not use placeholder comments like "already deleted above." Write the
  actual teardown assignments or deletes.

Cleanup teardown contract:
* Default posture: after cleaning children, delete owned field references with
  `del self._field` so the object stops exposing stale state.
* Allowed exception: set a field to `None` only when the contract explicitly
  needs a retained post-cleanup tombstone surface for callers, tests, or
  diagnostic introspection.
* If a field is kept as `None` instead of deleted, that must be intentional and
  documented.

Post-cleanup usage rule
* If a class implements cleanup, assume the object is not used after cleanup completes.
* Prefer `self.check_cleaned()` and allow it to throw for methods that require a live object.
* Only use `if self._cleaned: return` when the method must be non-throwing by contract.
* Do NOT snapshot `self._field` into locals unless absolutely necessary and justified.
* Do NOT guard internal fields with `if x is None` when lifecycle guarantees they exist pre-cleanup.
* `None` checks are for external inputs, truly optional state, or deliberately
  retained tombstone fields only.

Rules
- Cleanup implemented immediately after __init__.
- If your base class defines a cleanup contract, prefer deleting owned fields
  after cleanup. Use `None`
  only when the class contract explicitly requires a retained post-cleanup
  field surface.
- Cleanup must be idempotent and safe to call multiple times.
- Use a lock when cleanup can race with active work; check _cleaned before and after locking.
- Tear down child objects before clearing own fields.
- Delete owned references after cleanup by default.
- Logger teardown is always last.
- Do not rely on GC for owned resources.
- Document cleanup ordering and ownership in the docstring.

Checklist
- Guard against double cleanup.
- Acquire lock, then re-check _cleaned.
- Cleanup children in dependency order.
- Delete the lock after guarded teardown by default.
- Delete owned fields explicitly, unless a retained `None` tombstone is part of
  the contract.
- Logger cleanup last.

Example order
1) if _cleaned: return
2) with lock: re-check _cleaned, then cleanup children
3) del self._child
4) del self._lock
5) logger.cleanup() (last)
6) del self._logger

Retained-`None` exception example
1) if callers/tests intentionally read `field` after cleanup:
2) document that `field` becomes `None`
3) set `self.field = None` instead of deleting it
4) keep that exception local and explicit

Examples
- agent_onboarding/user_defined/synaptic_python_developer/examples/python/cleanup_patterns.py




