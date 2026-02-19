

# hot_path_attribute_aliasing

Purpose
- Apply measured attribute-access rules in Python hot paths.

Why this exists
- Attribute access style can materially affect runtime in tight loops.
- This skill encodes measured behavior so agents stop guessing and use data.

Rules
- Repeated `self` access in hot loops:
  - Alias once (`local = self._field`) and use the local alias.
- Method parameter flat access (`param.attr`) in hot loops:
  - Default to direct access.
  - Only alias if a local benchmark for that path shows a win.
- Method parameter chained access (`param.a.b...`) with depth >= 2 in hot loops:
  - Alias the resolved leaf once and reuse it.
- Outside hot paths:
  - Prefer readability and avoid unnecessary alias locals.

Challenge protocol
- If an agent disagrees with these rules, they must benchmark and provide evidence.
- The baseline benchmark files are:
  - `benchmarks/testing_other_di/test_local_alias_vs_direct_attr_perf.py`
  - `context_compass/agent_onboarding/user_defined/synaptic_python_developer/skills/python/test_attribute_aliasing_skill_benchmark.py`

Run commands
- `python -m pytest benchmarks/testing_other_di/test_local_alias_vs_direct_attr_perf.py -q -s`
- `python -m pytest context_compass/agent_onboarding/user_defined/synaptic_python_developer/skills/python/test_attribute_aliasing_skill_benchmark.py -q -s`

Evidence reporting format
- Include one table per scenario:
  - flat `self`
  - flat param
  - chained `self` (depth 2/3/4)
  - chained param (depth 2/3/4)
- Include:
  - iterations
  - repeats
  - direct ns/iter
  - alias ns/iter
  - alias/direct ratio

Decision policy
- If alias/direct ratio < 1.0: alias is faster.
- If ratio is near 1.0 (noise band), keep whichever is more readable unless path is proven hot.




