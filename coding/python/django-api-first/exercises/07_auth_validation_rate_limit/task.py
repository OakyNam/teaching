"""Exercise starter for lesson: 07_auth_validation_rate_limit."""
from dataclasses import dataclass


@dataclass(frozen=True)
class TokenClaims:
    user_id: int
    role: str
    org_slug: str


def issue_token_claims(user_id: int, role: str, org_slug: str) -> TokenClaims:
    return TokenClaims(user_id=user_id, role=role, org_slug=org_slug)


def validate_signup(email: str, password: str) -> tuple[bool, list[str]]:
    errors: list[str] = []
    if "@" not in email:
        errors.append("email is invalid")
    if len(password) < 12:
        errors.append("password is too short")
    if password.islower() or password.isalpha():
        errors.append("password should mix letters and numbers or symbols")
    return (len(errors) == 0, errors)


def check_rate_limit(request_count: int, limit: int) -> bool:
    return request_count <= limit


def throttle_window(limit: int, window: str) -> str:
    return f"Allow {limit} requests per {window} before returning HTTP 429."


def run() -> None:
    print("Exercise: add JWT claims, serializer validation, and throttling rules.")
    claims = issue_token_claims(7, "mentor", "cohort-3")
    print(f"- Claims: {claims}")
    print(f"- Window: {throttle_window(60, 'minute')}")
    print(f"- Good signup: {validate_signup('student@example.com', 'SecurePass#2024')}")
    print(f"- Bad signup: {validate_signup('student', 'short')}")
    print(f"- Under limit? {check_rate_limit(4, 10)}")
    print(f"- Under limit? {check_rate_limit(12, 10)}")

    assert validate_signup("student@example.com", "SecurePass#2024")[0] is True
    assert validate_signup("student", "short")[0] is False
    assert check_rate_limit(12, 10) is False
    print("Validation covered one passing request and one throttled or invalid request.")


if __name__ == "__main__":
    run()
