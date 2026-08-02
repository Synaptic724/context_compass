

# ctx_autonomy_policy

Purpose
- Define how agents rank ctx quality across file, dir, component, and architecture layers.
- Prevent low-quality ctx from cascading into higher-level summaries.

Scope
- Applies whenever an agent creates or refreshes file_ctx, dir_ctx, component_contexts, or architecture_context.
- Source-of-truth chain:
  - file ctx reflects code
  - dir ctx reflects file ctx
  - component ctx reflects dir ctx
  - architecture ctx reflects component ctx

Policy
- Evaluate ctx quality with the CTX Autonomy rubric before using it as input for higher layers.
- If a ctx would score below 60, stop and refresh/return tasks until quality is acceptable.
- If a ctx scores 60-74, it is usable but must be scheduled for review before high-risk changes.
- If a ctx scores 75+, it is trusted for downstream synthesis.
- Do not generate higher-level ctx from lower-quality inputs.

Unknowns Gate
- Apply the canonical policy in
  `agent_onboarding/default/general/skills/unknowns_gate_reference.md`.
- Do not promote ctx claims to FACT without evidence.
- CTX quality scoring inputs must be evidence-backed at each layer
  (file -> dir -> component -> architecture); otherwise mark UNKNOWN and
  halt higher-layer synthesis.
- If a source ctx claim is ambiguous, preserve UNKNOWN in downstream ctx
  instead of normalizing it into an inferred FACT.

Meaningful data definition
- Accurate: statements match the source of truth (code or lower-level ctx).
- Complete: covers responsibilities, public surface, dependencies, and key flows.
- Specific: avoids vague claims; uses concrete symbols, paths, or behaviors.
- Traceable: can point back to a file path or ctx path that supports the claim.
- Current: aligns with freshness_state and latest hashes.

Ranking model (0-100)
Score each criterion 0-5, then compute:
sum((score/5) * weight)

Criteria and weights
- Fidelity to source (35)
- Coverage of key responsibilities and flows (20)
- Depth and specificity (15)
- Traceability to paths/ctx (15)
- Internal coherence (10)
- Freshness alignment (5)

Scoring anchors (0/3/5)
- Fidelity
  - 5: All claims match code or cited ctx; no contradictions.
  - 3: Mostly correct with minor drift or missing nuance.
  - 0: Material inaccuracies or invented behavior.
- Coverage
  - 5: Responsibilities, public surface, dependencies, key flows all covered.
  - 3: One major area missing (e.g., error model or dependencies).
  - 0: Only a shallow summary or a single section populated.
- Depth and specificity
  - 5: Uses concrete symbols, paths, invariants, and behavioral detail.
  - 3: Mix of specific and generic statements.
  - 0: Vague or purely aspirational language.
- Traceability
  - 5: Each major claim ties to a file/dir ctx path or matrix citation.
  - 3: Some claims traceable, others floating.
  - 0: No traceable sources.
- Internal coherence
  - 5: No conflicts between sections (summary, dependencies, testing).
  - 3: Minor contradictions or unclear boundaries.
  - 0: Conflicting statements across sections.
- Freshness alignment
  - 5: fresh + hashes match; computed fields consistent.
  - 3: needs_review only; no hash mismatch.
  - 0: stale/blocked or mismatched computed fields.

Score bands
- 90-100: A (Excellent)
- 75-89: B (Good)
- 60-74: C (Fair)
- 40-59: D (Weak)
- 0-39: F (Unusable)

Layer-specific guidance
- File ctx
  - Must mirror code behavior, public surface, dependencies, error model, and lifecycle.
  - High scores require clear invariants, side effects, and test expectations.
- Dir ctx
  - Must summarize structure and responsibilities using file ctx only.
  - Inventory and boundaries must match file ctx coverage; avoid generic summaries.
- Component ctx
  - Must synthesize dir ctx into clear boundaries, dependency rules, and key flows.
  - Avoid inventing runtime behavior not supported by dir ctx.
- Architecture ctx
  - Must express system-level flows, non-goals, and integration boundaries.
  - Must remain consistent with component ctx and cite the underlying matrix.

Descriptive examples (score bands)
- File ctx example (B vs D)
  - B (80): "Exports RoleRouter.resolve_role; validates profile maps; raises ValueError on missing role paths; depends on context_compass_config; tests in tests/unit/context_compass/test_role_router.py."
  - D (45): "Handles routing and errors." (no symbols, no paths, no dependencies)
- Dir ctx example (A vs C)
  - A (92): "Owns role-chain resolution; includes resolver map + inheritance-frame context; excludes runtime execution policy."
  - C (65): "Contains routing helpers." (no boundaries, no inventory alignment)
- Component ctx example (B vs F)
  - B (78): "Component: role resolution. Boundary: the registry table and the resolved SKILLS chain; depends on onboarding policy contracts; key flow: select role -> resolve chain parent-first -> enforce execution gates."
  - F (20): "Everything in src/project." (overbroad, no citations, no boundaries)
- Architecture ctx example (A vs C)
  - A (95): "Flow: onboarding -> role selection -> ticket execution -> compaction recovery. Non-goals: product runtime features. Integration boundaries: external callers interact through entrypoint policy files only."
  - C (62): "System is modular with many components." (no flows, no boundaries, no non-goals)

Actions when quality is low
- Score < 60: return/defer downstream ctx tasks; refresh the source ctx first.
- Score 60-74: proceed only if necessary, and flag for review/resurvey.
- Score >= 75: proceed.

Survey expectations (planned)
- Add a ctx autonomy survey job that computes scores for file/dir/component/architecture ctx.
- Record results in context_compass tickets and emit refresh/review tasks for low scores.
- Use results to prioritize ctx improvement work.

References
- `agent_onboarding/default/engineer/skills/context_protocol.md`
- `agent_onboarding/default/engineer/skills/staleness_protocol.md`







