"""Reference solution for lesson: 07_auth_validation_rate_limit."""
from dataclasses import dataclass
from textwrap import dedent


@dataclass(frozen=True)
class RequestSnapshot:
    email: str
    role: str
    request_count: int


def auth_solution_snippet() -> str:
    return dedent(
        """
        class ProtectedSubmissionView(APIView):
            authentication_classes = [JWTAuthentication]
            throttle_classes = [UserRateThrottle]

            def post(self, request):
                serializer = SubmissionSerializer(data=request.data)
                serializer.is_valid(raise_exception=True)
                return Response(serializer.validated_data, status=201)
        """
    ).strip()


def validate_snapshot(snapshot: RequestSnapshot) -> tuple[bool, list[str]]:
    errors: list[str] = []
    if "@" not in snapshot.email:
        errors.append("invalid email")
    if snapshot.role not in {"student", "mentor", "admin"}:
        errors.append("invalid role")
    if snapshot.request_count > 60:
        errors.append("user throttle exceeded")
    return (len(errors) == 0, errors)


def run() -> None:
    good = RequestSnapshot("mentor@example.com", "mentor", 10)
    bad = RequestSnapshot("mentor", "guest", 120)
    print("Auth solution snippet:")
    print(auth_solution_snippet())
    print("\nValidation preview:")
    print(validate_snapshot(good))
    print(validate_snapshot(bad))

    assert validate_snapshot(good)[0] is True
    assert validate_snapshot(bad)[0] is False
    print("Validation confirmed the final auth, validation, and throttling rules.")


if __name__ == "__main__":
    run()
