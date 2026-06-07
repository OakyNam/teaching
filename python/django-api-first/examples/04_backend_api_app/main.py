"""Runnable example for lesson: 04_backend_api_app."""
from dataclasses import asdict, dataclass
from textwrap import dedent


@dataclass(frozen=True)
class SubmissionPayload:
    source: str
    student_email: str
    score: int


def serializer_snippet() -> str:
    return dedent(
        """
        class SubmissionSerializer(serializers.Serializer):
            source = serializers.CharField(max_length=40)
            student_email = serializers.EmailField()
            score = serializers.IntegerField(min_value=0, max_value=100)
        """
    ).strip()


def api_view_snippet() -> str:
    return dedent(
        """
        class SubmissionView(APIView):
            def post(self, request):
                serializer = SubmissionSerializer(data=request.data)
                serializer.is_valid(raise_exception=True)
                return Response(serializer.validated_data, status=201)
        """
    ).strip()


def validate_payload(payload: SubmissionPayload) -> tuple[bool, list[str]]:
    errors: list[str] = []
    if payload.source not in {"web", "mobile", "partner"}:
        errors.append("source must be web, mobile, or partner")
    if "@" not in payload.student_email:
        errors.append("student_email must look like an email address")
    if not 0 <= payload.score <= 100:
        errors.append("score must stay within 0..100")
    return (len(errors) == 0, errors)


def main() -> None:
    sample = SubmissionPayload("web", "learner@example.com", 91)
    print("Serializer example:")
    print(serializer_snippet())
    print("\nAPIView example:")
    print(api_view_snippet())
    print("\nSerialized sample:")
    print(asdict(sample))

    valid, errors = validate_payload(sample)
    invalid, bad_errors = validate_payload(SubmissionPayload("fax", "broken", 120))
    print(f"Valid sample? {valid} errors={errors}")
    print(f"Invalid sample? {invalid} errors={bad_errors}")

    assert valid is True
    assert invalid is False
    print("Validation checked both a successful API submission and a failing one.")


if __name__ == "__main__":
    main()
