"""Reference solution for lesson: 08_deployment_observability."""
from dataclasses import dataclass
from textwrap import dedent


@dataclass(frozen=True)
class RuntimeEnvironment:
    allowed_hosts: tuple[str, ...]
    debug: bool
    log_level: str


def production_settings_snippet() -> str:
    return dedent(
        """
        DEBUG = False
        ALLOWED_HOSTS = ['api.example.com']
        SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
        LOGGING = {
            'version': 1,
            'handlers': {'console': {'class': 'logging.StreamHandler'}},
            'root': {'handlers': ['console'], 'level': 'INFO'},
        }
        """
    ).strip()


def validate_runtime(env: RuntimeEnvironment) -> bool:
    return not env.debug and len(env.allowed_hosts) > 0 and env.log_level in {"INFO", "WARNING", "ERROR"}


def health_response(db_ok: bool, queue_ok: bool) -> dict[str, object]:
    return {
        "status": "ok" if db_ok and queue_ok else "degraded",
        "checks": {"database": db_ok, "queue": queue_ok},
    }


def run() -> None:
    env = RuntimeEnvironment(("api.example.com",), False, "INFO")
    broken = RuntimeEnvironment((), True, "TRACE")
    print("Production settings:")
    print(production_settings_snippet())
    print("\nHealth checks:")
    print(health_response(True, True))
    print(health_response(True, False))

    assert validate_runtime(env) is True
    assert validate_runtime(broken) is False
    assert health_response(True, False)["status"] == "degraded"
    print("\nValidation: deploy-time configuration and observability checks are complete.")


if __name__ == "__main__":
    run()
