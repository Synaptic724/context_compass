

# mrp_policy

Purpose
- Enforce MRP (Most Reasonable Product) as the default strategy.

MRP (Most Reasonable Product)
- Definition: the smallest product that is still coherent, trustworthy, and
  durable enough that shipping it does not create a trap.
- Framing: build it like there is no patch coming, no second chance, and no
  acceptable excuse to ship the core wrong.
- Quality bar: the core experience, boundaries, lifecycle, operability, and
  failure behavior must be right enough that the system can grow without a
  foundational rewrite.
- Ship rule: if the core would need to be reworked immediately after release to
  become trustworthy, it is not MRP yet.
- Practical analogy: treat the build like `Super Mario World`, not a
  patch-it-later live-service product. If the core has to be right the first
  time, MRP is the standard.
- Non-goal: MRP is not perfectionism. It does not mean infinite polish. It
  means the foundational system must be right, coherent, and safe to build on.

MVP (Minimum Viable Product) - Disallowed
- MVP is optimized for speed to validate demand, not robustness.
- MVP is disallowed in this repo.

MLP (Most Lovable Product) - UI Only
- MLP focuses on delight, polish, and adoption.
- Allowed only for UI/UX tasks and only after the MRP core is solid.

Decision heuristic
- If uncertainty is about foundation reliability, choose MRP.
- If the choice is between shipping faster and getting the core right, choose
  getting the core right.
- If the product would become technical debt the moment it ships, it is not
  MRP.
- If success depends on love/retention/referrals, apply MLP after MRP.
- Default to MRP when in doubt.

