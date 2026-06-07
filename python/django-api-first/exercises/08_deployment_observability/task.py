"""Exercise starter for lesson: 08_deployment_observability."""
from dataclasses import dataclass


@dataclass(frozen=True)
class HealthCheck:
    database: bool
    cache: bool
    queue: bool


def build_gunicorn_command(workers: int) -> str:
    return f"gunicorn config.wsgi:application --bind 0.0.0.0:8000 --workers {workers}"


def build_health_payload(check: HealthCheck) -> dict[str, object]:
    return {
        "status": "ok" if all(vars(check).values()) else "degraded",
        "checks": vars(check),
    }


def logging_level(debug: bool) -> str:
    return "DEBUG" if debug else "INFO"


def env_summary(domain: str, debug: bool) -> dict[str, object]:
    return {"allowed_hosts": [domain], "debug": debug, "log_level": logging_level(debug)}


def health_url(domain: str) -> str:
    return f"https://{domain}/healthz/"


def run() -> None:
    print("Exercise: prepare production commands, health checks, and logging defaults.")
    healthy = HealthCheck(True, True, True)
    degraded = HealthCheck(True, False, True)

    print(f"- Gunicorn: {build_gunicorn_command(4)}")
    print(f"- Environment: {env_summary('api.example.com', False)}")
    print(f"- Health URL: {health_url('api.example.com')}")
    print(f"- Healthy payload: {build_health_payload(healthy)}")
    print(f"- Degraded payload: {build_health_payload(degraded)}")
    print(f"- Logging level (debug=False): {logging_level(False)}")

    assert build_health_payload(healthy)['status'] == 'ok'
    assert build_health_payload(degraded)['status'] == 'degraded'
    assert logging_level(False) == 'INFO'
    print("Validation covered one healthy environment and one degraded environment.")


if __name__ == "__main__":
    run()
