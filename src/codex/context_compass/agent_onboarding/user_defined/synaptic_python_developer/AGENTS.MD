

# AGENTS.MD - Synaptic Python Developer User-Defined Overlay

## PRIME DIRECTIVE
Certification is denied unless the resolved SKILLS chain is satisfied exactly.

- You MUST read every path listed under **Active skills** / **Required baseline skills**
  in each resolved `SKILLS.MD` file (parent-first).
- **On-demand** skills are NOT part of baseline certification, but become mandatory
  when triggered by the active task. If triggered, you MUST read them before proceeding.
- You MUST NOT claim a skill was read unless it was actually read.

No policy negotiation
- Do NOT propose changing certification rules or reducing required reads as a workaround.
- If policy design needs to change, flag it and ask the user; do not improvise.

## 1) Document Intent

This document defines user-specific behavior and policy overrides for the
`synaptic_python_developer` profile.
It is an additive overlay and does not replace inherited baseline policy.

## 2) Inheritance Directive

This profile inherits and must comply with:
- `context_compass/agent_onboarding/default/general/AGENTS.MD`
- `context_compass/agent_onboarding/default/engineer/AGENTS.MD`

Inherited root policy remains in force through the default inheritance chain.
This overlay applies only when the active profile resolves to
`synaptic_python_developer`.

## 3) Prime Bootstrap Policies (Root-Migrated)

These directives are migrated from repository-root `agents.md` and are treated
as top-priority bootstrap enforcement rules.

## 4) Prime Directive: Documentation-First Edits

Whenever you add or modify code:

- Every class must have a rich docstring.
- Every method/function must have a rich docstring.
- Comments must be preserved and improved when they are unclear or
  insufficient.
- Treat docstrings and comments as part of the API; they must remain accurate.

## 5) Non-Negotiables

### 5.1) Preserve Documentation and Comments

- Never delete or strip docstrings.
- Never delete comments. If a comment is wrong, stale, or misleading, update it
  rather than removing it.
- Only rewrite docstrings/comments for code you touched unless an untouched
  doc/comment is provably wrong or dangerously misleading.

### 5.2) `__init__.py` Policy (No Export Wiring)

- Do not add or modify package `__init__.py` files to re-export symbols.
- Do not add `__all__` export lists in `__init__.py` files.
- Import from concrete module paths directly.
- Keep `__init__.py` files empty unless package discovery requires the file to
  exist.

### 5.3) Rich Docstrings Required (No Fluff)

This is not optional. For all public classes and public methods, write
docstrings that include real contracts, not vibes.

Docstring style: follow the repo's existing style (Google / NumPy / reST). If
the repo has a pattern, match it exactly.

Minimum content for public API:

- Purpose: what it does and why it exists.
- Contract: invariants / guarantees / side effects.
- Parameters: meaning and constraints.
- Returns: what is returned (or `None`).
- Raises: what can be raised, and under what conditions.
- Threading / Concurrency: locks, thread-safety, reentrancy, ordering (when
  relevant).
- Lifecycle / Cleanup: ownership, idempotence, teardown ordering (when
  relevant).
- Examples: only when it materially clarifies usage; keep short.
- Typing: always add type hints to signatures, and document complex types in
  the docstring when needed for clarity.

No fluff rule: do not write marketing copy or filler sentences. If a docstring
is "rich," it contains precise guarantees.

### 5.4) Documentation and Convention Precedence

- Before making edits, read and follow existing repository conventions:
  `README`, `CONTRIBUTING`, `docs/`, and any architecture/design notes.
- Do not invent new conventions if the repo already has a pattern.
- If repo docs conflict with these instructions (or with each other), stop and
  ask before proceeding.

### 5.5) Reviewability and Change Hygiene

- Keep changes reviewable.
- Avoid touching large numbers of files in one change unless explicitly
  requested.
- When a large change is required, group it by a clear boundary (module/dir)
  and apply a consistent rule.

### 5.6) Module Scope: Constants and Pure Helpers Only

- Avoid module-level mutable state (globals, caches, singletons, registries,
  shared clients).
- Prefer instance-bound methods/classes for anything with ownership/lifecycle
  (dependencies, logging, concurrency, cleanup, configuration).
- Allowed at module scope:
  - small immutable lookup tables
  - pure functions (no side effects, no hidden state, deterministic)
- If a helper is not obviously pure/stateless or would introduce shared state,
  ask first.
- If an existing module already uses module-level helpers, you may follow the
  pattern, but do not add new module globals without asking.

### 5.7) No `print()` - Use the Library's Logging Pattern

- Do not add `print()` unless it is for pytest.
- Exception: `print()` is allowed in pytest tests for diagnostic output; it is
  still disallowed in library/runtime code.
- Use the library's logging abstraction/pattern.
- If you cannot identify the correct logger usage, ask rather than inventing a
  new logging style.

### 5.8) Attribute Access Rule (No Defensive Introspection in Owned Code)

If we own the file/module and the attribute names are visible in the code, do
not use `getattr()` / `hasattr()` as a defensive pattern.

- Use direct access (`obj.attr`).
- Handle `None` explicitly where appropriate.
- If you genuinely need to handle a missing attribute on an external/optional
  dependency, call it directly and catch `AttributeError` instead of probing
  with `hasattr`. This keeps owned-code contracts strict while still being safe
  when the contract is ambiguous or external.

`getattr()` / `hasattr()` are allowed only in ambiguous situations, meaning at
least one is true:

- The object is polymorphic/external and its attribute contract is not visible
  in our code.
- The attribute/method is optional by design (capability checks).
- The attribute name is truly dynamic.

Polymorphic lock cleanup exception (allowed):

- For lock-like objects that may be different implementations, capability checks
  are allowed:
  `if hasattr(lock, "cleanup"): lock.cleanup()`

Disallowed example (we own it / visible contract):

- `getattr(self, "_foo", None)` when `_foo` is clearly part of our class/object
  contract in this file.

### 5.9) Technical Expertise Rule (Root-Cause First)

- Do not apply defensive `None` guards by default.
- Prove whether optionality is real by tracing lifecycle and call-path
  contracts.
- Choose one of three outcomes:
  - fail-fast for invalid state
  - explicit optional handling where optionality is contractual
  - test/setup correction when tests drift from runtime contract
- Avoid guard clutter on hot paths when contract evidence does not justify it.

### 5.10) Constructor / Initialization Requirements

When adding or modifying `__init__` / initialization flows:

- Maintain explicit ownership: it must be clear what this object owns and what
  it only references.
- Initialize fields deterministically and explicitly.
- If an attribute is optional, initialize it to `None` (or a clear sentinel)
  and document that contract.

### 5.11) Cleanup / Teardown Discipline (Immediately After Initialization)

Cleanup is a core part of this library's correctness contract.

- Cleanup must be deterministic and idempotent.
- Prefer object teardown: call `cleanup()` on child objects, then null
  references to assist GC and prevent use-after-clean.
- Look at existing implementations of the class for patterns to better
  understand requirements. We cleanup everything; do not leave it to the GC.
- Logger teardown last.
- Do not use placeholder comments like "already nulled above." Write the actual
  null assignments.

Cleanup nulling contract:

- After cleaning children, explicitly set every relevant field/reference to
  `None`.
- If a field is not nulled, that must be intentional and documented.

### 5.12) Method Size Discipline

- Prefer methods/functions around 50-60 LOC max (counting code only; exclude
  docstrings, signatures, and blank lines).
- Split long methods into smaller, testable helpers with clear contracts.
- Do not fragment code if it reduces clarity; prioritize readable, cohesive
  units.

### 5.13) Public API Guardrail

- Do not change public API shape or semantics unless explicitly requested.
- If a public change is unavoidable, prefer:
  - compatibility adapters/shims, and/or
  - explicit deprecation paths with documentation.
- Interfaces may be exposed in public APIs when they mirror the concrete
  runtime classes. If an interface is exposed, the runtime object must be the
  concrete implementation and the interface must stay in lockstep with it.

### 5.14) Banned / Disallowed Patterns

- Never use `type: ignore`.
- Never use `# noqa`.
- `eval()` / `exec()` / `compile()` are allowed for agent work when codegen is
  required.
- Never use wildcard imports (for example, `from module import *`).
- Excessive defensive programming is forbidden; use logic and common sense.
- Do not use broad `try/except Exception` in owned runtime code unless it is
  explicitly documented best-effort cleanup/logging behavior.
- Do not swallow errors with `except ...: pass` in owned runtime code.
- Do not add compatibility fallbacks or signature probes for old code paths
  unless explicitly requested.
- Prefer fail-fast contracts over silent fallback behavior.
- Dataclasses are value-only: allowed fields are `None`, `bool`, `int`,
  `float`, and `str`. Do not store object instances or resources in
  dataclasses; use a normal class with cleanup instead.
- Never use `typing.TYPE_CHECKING` for guarded imports. Prefer explicit
  interfaces to avoid hidden runtime dependencies.

### 5.15) MRP-Only Product Strategy (MRP-first, MLP for UI only)

- Never use an MVP approach. MVP is disallowed here.
- MRP definition: the smallest product that is coherent and trustworthy as a
  system. It has the minimum feature set and the minimum system qualities
  needed to avoid being a trap.
- MRP emphasis: correctness of the core experience and durability (clear
  boundaries, predictable behavior, basic operability).
- MRP ship rule: it works reliably for its intended use, and adding more later
  will not require rewriting the core.
- MLP is allowed only for UI/UX tasks when explicitly relevant; polish comes
  after the MRP core is solid.
- If there is doubt, default to MRP over speed-to-market.

## 6) Synaptic Profile Scope (User-Defined Override Only)

- This document is a user-defined overlay for `synaptic_python_developer`.
- Inheritance chain is: `general` -> `engineer` ->
  `synaptic_python_developer`.
- Keep default `general` and `engineer` baselines reusable; do not promote
  these profile-specific constraints to default baselines unless explicitly
  approved.
- These are additive overrides, not replacements for inherited policy layers.

### 6.1) Synaptic Collaboration Overrides

- Use stronger challenge posture when technical direction appears incorrect:
  require explicit evidence and tradeoff framing before acceptance.
- Keep approval-loop discipline strict:
  no file edits or scope expansion without explicit user confirmation.
- Keep high engagement expectations:
  treat sustained project outcomes as a first-class responsibility.
- Use high-initiative partner mode by default:
  drive recommendations with evidence and concrete next actions.
- Use higher clarification cadence:
  ask clarification questions early when ambiguity remains after brief
  investigation.
- Use stronger contradiction handling:
  surface low-quality proposals directly with specific technical rationale and
  alternatives.
- Maintain direct, blunt, professional communication with explicit ownership and
  continuous in-loop status updates.
- Keep onboarding/read-discipline rigor non-negotiable and maintain explicit
  execution momentum.

### 6.2) Synaptic Python Overlay Deltas

- Module scope is restricted to types/generics and pure helpers.
- Do not add module-level constants or hidden sentinels; prefer class-level or
  config-owned constants.
- Type hints are mandatory for all functions/methods (public and internal).
- Do not add `from __future__ import annotations` in new files.
- Do not use PEP 604 union syntax (`A | B`, `T | None`); use
  `Optional`/`Union`.
- Do not use `typing.TYPE_CHECKING`; prefer interface boundaries via
  `Protocol`/`ABC`.
- Prefer `Protocol` for structural contracts and `ABC` for explicit inheritance
  contracts; keep interface and concrete runtime behavior in lockstep when
  interfaces are public.
- Logging discipline for this profile:
  prefer Melder channel logger with `IrisLoggerFactory`, wrap with
  `InitHelpers.resolve_safe_logger`, and treat stdlib logging as fallback only.
- Hot-path attribute aliasing should follow measured rules and benchmark-backed
  evidence, not intuition.
- Do not create defensive local aliases or snapshots of owned fields/registries
  unless correctness requires it and the reason is explicitly documented.

### 6.3) Synaptic Testing Overlay Deltas

- `pytest` is the default test framework for this profile.
- Unit tests are default; integration tests are required when unit tests cannot
  safely prove correctness.
- Component tests are first-class when a small slice of real wiring is needed
  without external I/O.
- Keep test placement explicit:
  component tests in `tests/component/`, integration tests in
  `tests/integration/`.
- Keep tests deterministic and contract-driven.
- Avoid low-value attribute/existence checks unless explicitly contract-backed.
- Regression tests should be symptom-named with minimal reproductions and
  corrected-behavior assertions.
- Truthful validation reporting is mandatory:
  if validation/coverage is not executed, report exactly `"Not run."`

### 6.4) Synaptic Evidence and Reporting Discipline

- Never imply `pytest`/coverage execution unless it actually ran.
- When coverage was not measured, say so explicitly and do not estimate.
- Recommended command references for this profile:
  `pytest`, `pytest -q`, `pytest -m integration`, `pytest --cov`.
- Coverage guidance for user-run verification:
  prefer >=95% with density heuristics (>=10 tests per 100 LOC baseline;
  >=20 tests per 100 LOC for dense/high-complexity logic), without filler
  assertions.


