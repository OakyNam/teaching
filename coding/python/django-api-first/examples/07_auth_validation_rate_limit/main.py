"""Runnable example for lesson: 07_auth_validation_rate_limit."""
from dataclasses import dataclass
from textwrap import dedent


@dataclass(frozen=True)
class SignupAttempt:
    email: str
    password: str
    requests_this_minute: int


def jwt_settings_snippet() -> str:
    return dedent(
        """
        REST_FRAMEWORK = {
            'DEFAULT_AUTHENTICATION_CLASSES': (
                'rest_framework_simplejwt.authentication.JWTAuthentication',
            ),
            'DEFAULT_THROTTLE_CLASSES': ['rest_framework.throttling.UserRateThrottle'],
            'DEFAULT_THROTTLE_RATES': {'user': '60/min'},
        }
        """
    ).strip()


def serializer_snippet() -> str:
    return dedent(
        """
        class SignupSerializer(serializers.Serializer):
            email = serializers.EmailField()
            password = serializers.CharField(min_length=12, write_only=True)

            def validate_email(self, value):
                if User.objects.filter(email=value).exists():
                    raise serializers.ValidationError('Email already registered.')
                return value
        """
    ).strip()


def validate_signup(attempt: SignupAttempt) -> tuple[bool, list[str]]:
    errors: list[str] = []
    if "@" not in attempt.email:
        errors.append("email must contain @")
    if len(attempt.password) < 12:
        errors.append("password must be at least 12 characters")
    if attempt.requests_this_minute > 60:
        errors.append("user throttle exceeded")
    return (len(errors) == 0, errors)


def main() -> None:
    good = SignupAttempt("learner@example.com", "correct-horse-1", 3)
    bad = SignupAttempt("broken-email", "short", 99)
    print("JWT settings:")
    print(jwt_settings_snippet())
    print("\nValidation serializer:")
    print(serializer_snippet())
    print("\nSignup validation:")
    print(validate_signup(good))
    print(validate_signup(bad))

    assert validate_signup(good)[0] is True
    assert validate_signup(bad)[0] is False
    print("Validation checked a good authenticated signup path and a throttled failure path.")


if __name__ == "__main__":
    main()
