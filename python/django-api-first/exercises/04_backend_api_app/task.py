"""Exercise starter for lesson: 04_backend_api_app."""
from dataclasses import dataclass
from textwrap import dedent


@dataclass(frozen=True)
class IncomingRecord:
    source: str
    email: str
    attempts: int


def normalize_source(source: str) -> str:
    return source.strip().lower()


def validate_record(record: IncomingRecord) -> tuple[bool, list[str]]:
    errors: list[str] = []
    if normalize_source(record.source) not in {"web", "mobile", "partner"}:
        errors.append("unsupported source")
    if "@" not in record.email:
        errors.append("invalid email")
    if record.attempts < 0:
        errors.append("attempts must be zero or greater")
    return (len(errors) == 0, errors)


def response_payload(record: IncomingRecord) -> dict[str, object]:
    ok, errors = validate_record(record)
    return {"ok": ok, "errors": errors, "normalized_source": normalize_source(record.source)}


def api_view_outline() -> str:
    return dedent(
        """
        class IntakeView(APIView):
            def post(self, request):
                serializer = IntakeSerializer(data=request.data)
                serializer.is_valid(raise_exception=True)
                return Response(serializer.validated_data, status=201)
        """
    ).strip()


def run() -> None:
    print("Exercise: implement a serializer and APIView for a DRF backend app.")
    good = IncomingRecord(" Web ", "person@example.com", 1)
    bad = IncomingRecord("desk-phone", "person-at-example.com", -1)

    print(f"- APIView outline: {api_view_outline()}")
    print(f"- Good response: {response_payload(good)}")
    print(f"- Bad response: {response_payload(bad)}")

    assert response_payload(good)["ok"] is True
    assert response_payload(bad)["ok"] is False
    assert response_payload(good)["normalized_source"] == "web"
    print("Validation covered a correct request and a rejected request.")


if __name__ == "__main__":
    run()
