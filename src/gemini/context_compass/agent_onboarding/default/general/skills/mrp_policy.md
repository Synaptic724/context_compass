

# mrp_policy

Purpose
- Enforce MRP (Most Reasonable Product) as the default strategy.

MRP (Most Reasonable Product)
- Definition: the smallest product that is coherent and trustworthy as a system.
- Minimums: minimum feature set and minimum system qualities to avoid a trap.
- Emphasis: correctness of the core experience + durability (clear boundaries, predictable behavior, basic operability).
- Ship rule: it works reliably for intended use, and future growth will not require rewriting the core.

MVP (Minimum Viable Product) - Disallowed
- MVP is optimized for speed to validate demand, not robustness.
- MVP is disallowed in this repo.

MLP (Most Lovable Product) - UI Only
- MLP focuses on delight, polish, and adoption.
- Allowed only for UI/UX tasks and only after the MRP core is solid.

Decision heuristic
- If uncertainty is foundation reliability, choose MRP.
- If success depends on love/retention/referrals, apply MLP after MRP.
- Default to MRP when in doubt.


