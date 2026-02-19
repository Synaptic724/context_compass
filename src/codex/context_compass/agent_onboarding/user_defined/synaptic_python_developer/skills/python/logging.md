

# logging

Purpose
- Ensure consistent logging discipline.


No print() - Use the Library's Logging Pattern
* Do not add print().
* Use the library's logging abstraction/pattern.
* If you cannot identify the correct logger usage, ask rather than inventing a new logging style.

Rules
- Never use print().
- Primary logger is the Melder channel logger via IrisLoggerFactory.
- Always wrap loggers with SafeLogger using InitHelpers.resolve_safe_logger.
- Stdlib logging is secondary and only used when IrisLogger is unavailable.
- If logger selection is unclear, raise an explicit open question and cite Conduit
  (src/melder/aether/conduit/conduit.py).

Example
- logger = InitHelpers.resolve_safe_logger(logger_factory(self))
- logger.info("message", "method_name")

Examples
- agent_onboarding/user_defined/synaptic_python_developer/examples/python/logging_patterns.py





