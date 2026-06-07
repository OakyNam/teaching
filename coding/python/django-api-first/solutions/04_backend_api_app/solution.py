"""Reference solution for lesson: 04_backend_api_app."""
from dataclasses import dataclass
from textwrap import dedent


@dataclass(frozen=True)
class HealthResult:
    status: str
    queue_depth: int
    accepted_sources: tuple[str, ...]


def serializer_solution() -> str:
    return dedent(
        """
        class HealthSerializer(serializers.Serializer):
            status = serializers.CharField()
            queue_depth = serializers.IntegerField(min_value=0)
            accepted_sources = serializers.ListField(child=serializers.CharField())
        """
    ).strip()


def view_solution() -> str:
    return dedent(
        """
        class HealthView(APIView):
            def get(self, request):
                payload = {'status': 'ok', 'queue_depth': 2, 'accepted_sources': ['web', 'mobile']}
                serializer = HealthSerializer(payload)
                return Response(serializer.data)
        """
    ).strip()


def validate_health(result: HealthResult) -> tuple[bool, list[str]]:
    errors: list[str] = []
    if result.status not in {"ok", "degraded"}:
        errors.append("status must be ok or degraded")
    if result.queue_depth < 0:
        errors.append("queue_depth cannot be negative")
    if not result.accepted_sources:
        errors.append("accepted_sources cannot be empty")
    return (len(errors) == 0, errors)


def run() -> None:
    result = HealthResult("ok", 2, ("web", "mobile"))
    broken = HealthResult("offline", -1, ())
    print("Serializer solution:")
    print(serializer_solution())
    print("\nAPIView solution:")
    print(view_solution())
    print("\nValidation preview:")
    print(validate_health(result))
    print(validate_health(broken))

    assert validate_health(result)[0] is True
    assert validate_health(broken)[0] is False
    print("Validation confirmed the completed DRF view contract.")


if __name__ == "__main__":
    run()
