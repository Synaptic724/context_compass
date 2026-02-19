

# typing

Purpose
- Keep type hints explicit and aligned with contracts.

Minimum content for public API:
* Typing: Always add typehints to signatures, and document complex types in the docstring if needed for clarity.

Rules
- Type hints are mandatory for all functions and methods (public and internal).
- Use Protocol and ABC where needed (see interfaces).
- Document complex types in the docstring.
- Avoid dynamic typing when a precise type is known.
- Do not add "from __future__ import annotations" in new files.
- Use Optional/Union for nullable and multi-type hints (no PEP 604 unions).
- Do not use "|" union syntax in annotations or docstring signatures.
- Use string literals only when required for tools.
- Do not use typing.TYPE_CHECKING for guarded imports; prefer interfaces for
  dependency boundaries.

Good vs bad
- Good: "def load_config(path: Path) -> Config" with docstring describing Config fields.
- Good: "def build(logger: Optional[Union[IChannelLogger, logging.Logger]]) -> SafeLogger"
- Bad: "def load_config(path)" with no type hints.
- Bad: "def build(logger: IChannelLogger | logging.Logger | None)" (PEP 604 union syntax).

Examples
- agent_onboarding/user_defined/synaptic_python_developer/examples/python/protocols_and_abc.py





