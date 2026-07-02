

# logging

Purpose
- Ensure consistent logging discipline.


No print() - Use the Library's Logging Pattern
* Do not add print().
* Use the library's logging abstraction/pattern.
* If you cannot identify the correct logger usage, ask rather than inventing a new logging style.

Rules
- Never use print().
- Primary logger path is `InitHelpers.resolve_channel_logger(...)` through the
  hosted provider.
- Explicit logger objects should be wrapped with
  `InitHelpers.resolve_safe_logger(...)`.
- Stdlib logging is secondary and should be registered at the provider level as
  the basic fallback only.
- If logger selection is unclear, raise an explicit open question and cite the
  repository's real logger owner or logger-factory source file.

Example
- logger = InitHelpers.resolve_channel_logger(self, channels="system")
- logger.info("message", "method_name")

Examples
- agent_onboarding/user_defined/synaptic_python_developer/examples/python/logging_patterns.py







