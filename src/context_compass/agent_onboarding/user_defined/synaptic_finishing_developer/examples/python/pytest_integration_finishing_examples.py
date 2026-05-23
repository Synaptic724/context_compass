"""Integration-test examples for finishing-role runtime flows."""


class ExampleValidator:
    """Validate one payload according to a simple runtime rule."""

    def validate(self, payload: str) -> bool:
        return payload.startswith("ok:")


class ExamplePublisher:
    """Record successfully published payloads."""

    def __init__(self) -> None:
        self._history: list[str] = []

    def publish(self, payload: str) -> None:
        self._history.append(payload)

    @property
    def history(self) -> list[str]:
        return list(self._history)


class ExampleService:
    """Small multi-object flow: validate, then publish.

    Purpose:
      Model the kind of cross-object runtime flow that deserves integration
      coverage because the boundary itself is the contract.

    Contract:
      - Invalid payloads do not publish.
      - Valid payloads publish exactly once.
    """

    def __init__(self, validator: ExampleValidator, publisher: ExamplePublisher) -> None:
        self._validator = validator
        self._publisher = publisher

    def execute(self, payload: str) -> bool:
        if not self._validator.validate(payload):
            return False
        self._publisher.publish(payload)
        return True


def test_execute_publishes_only_when_validation_passes() -> None:
    """Integration tests should prove the real end-to-end behavior."""

    validator = ExampleValidator()
    publisher = ExamplePublisher()
    service = ExampleService(validator, publisher)

    assert service.execute("bad") is False
    assert publisher.history == []

    assert service.execute("ok:payload") is True
    assert publisher.history == ["ok:payload"]
