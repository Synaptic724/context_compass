

# technical_expertise

Purpose
- Enforce engineering-grade problem diagnosis before code changes.
- Prevent defensive guard sprawl that hides contract errors and adds hot-path overhead.

Core rule
- Do not blindly add defensive checks for every possible `None` or missing attribute.
- Diagnose the real runtime contract first, then apply the smallest correct fix.

Root-cause workflow (required)
1) Reproduce the issue with concrete failing evidence (stack trace, test, or runtime path).
2) Trace call-path ownership and lifecycle boundaries.
   - **Tracing means opening each file along the path and reading it.** Finding the
     callers with `grep` is how you get the list; it is not the trace. A caller list
     tells you where a name appears - not whether that call site holds a lock, owns
     the object, passes a borrowed reference, or runs before cleanup. Those are the
     facts the diagnosis turns on, and only the source states them.
3) Identify whether `None`/missing state is valid, invalid, or test-only setup drift.
4) Classify the fix:
   - Contract violation: fail fast with explicit error.
   - Valid optional state: handle explicitly at the boundary where optionality is real.
   - Test mismatch: update test setup to match production contract.
5) Implement minimal change that preserves performance and clarity.

Performance discipline
- Every extra guard in hot or frequently executed paths has cost.
- Prefer strict contracts over repetitive defensive branching.
- Add guards only when the contract requires optional state.

Contract discipline
- Use lifecycle evidence, not assumptions, to decide if a field can be `None`.
- `check_cleaned()` proves cleaned-state only; it does not prove all owned references are populated.
- If an API requires active ownership state, enforce that requirement explicitly.

Anti-patterns
- Adding broad `if x is None: return` everywhere without proving optionality.
- Swallowing root causes with catch-all fallback behavior.
- Treating failing tests as proof of production contracts without call-path validation.

Expected outcome
- Fewer superficial fixes.
- Better failure semantics.
- Lower overhead on critical paths.

References
- `AGENTS.MD`
- `agent_onboarding/default/engineer/skills/context_protocol.md`



