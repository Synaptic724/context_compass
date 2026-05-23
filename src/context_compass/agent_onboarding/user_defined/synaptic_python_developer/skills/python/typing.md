

# typing

Purpose
- Keep type hints explicit and aligned with contracts.

Minimum content for public API:
* Typing: Always add typehints to signatures, and document complex types in the docstring if needed for clarity.

Rules
- Type hints are mandatory for all functions and methods (public and internal).
- Use `typing.TYPE_CHECKING` for typing-only imports by default.
- Python 3.14 deferred annotations are the baseline for this repo.
  Use the real imported type name directly in annotations when the import lives
  under `TYPE_CHECKING`.
- Use Protocol and ABC only where a real shared structural or inheritance
  contract exists (see interfaces).
- Document complex types in the docstring.
- Avoid dynamic typing when a precise type is known.
- Do not add "from __future__ import annotations" in new files.
- Python 3.14 already defers annotations by default, so this import is not a
  valid workaround for typing-only import pressure.
- Use Optional/Union for nullable and multi-type hints (no PEP 604 unions).
- Do not use "|" union syntax in annotations or docstring signatures.
- Do not quote concrete type names imported only under `TYPE_CHECKING` unless a
  tool-specific edge case genuinely requires it.
- Use `typing.TYPE_CHECKING` for guarded imports when the dependency is
  typing-only; prefer interface extraction only when a concrete shared
  structure truly needs to be enforced across implementations.
- Do not add `else: TypeName = Any` fallback aliases just to satisfy
  annotation resolution.
- Because this repo is typed with mypy, widening a truthful concrete
  collaborator type to `Any` is wrong unless it is genuinely unavoidable and
  explicitly raised to the user first.

Good vs bad
- Good: "def load_config(path: Path) -> Config" with docstring describing Config fields.
- Good: "def build(logger: Optional[Union[IChannelLogger, logging.Logger]]) -> SafeLogger"
- Good: `if TYPE_CHECKING: from x import RealType` then `def f(x: RealType) -> None`
- Bad: "def load_config(path)" with no type hints.
- Bad: "def build(logger: IChannelLogger | logging.Logger | None)" (PEP 604 union syntax).
- Bad: `else: RealType = Any`
- Bad: `def f(x: "RealType") -> None` when `RealType` already comes from a
  `TYPE_CHECKING` import and no tool-specific edge case exists.

Examples
- agent_onboarding/user_defined/synaptic_python_developer/examples/python/protocols_and_abc.py




