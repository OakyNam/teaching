"""Runnable example for lesson: 08_deployment_observability."""
from dataclasses import dataclass
from textwrap import dedent


@dataclass(frozen=True)
class DeploymentConfig:
    domain: str
    workers: int
    debug: bool


def gunicorn_command(config: DeploymentConfig) -> str:
    return (
        f"gunicorn config.wsgi:application --bind 0.0.0.0:8000 "
        f"--workers {config.workers} --access-logfile -"
    )


def nginx_snippet(domain: str) -> str:
    return dedent(
        f"""
        server {{
            listen 80;
            server_name {domain};
            location /static/ {{ alias /srv/app/static/; }}
            location / {{ proxy_pass http://127.0.0.1:8000; }}
        }}
        """
    ).strip()


def health_payload(debug: bool) -> dict[str, object]:
    return {"status": "ok", "debug": debug, "checks": ["database", "redis", "storage"]}


def main() -> None:
    config = DeploymentConfig("api.example.com", 3, False)
    print("Gunicorn command:")
    print(gunicorn_command(config))
    print("\nNginx snippet:")
    print(nginx_snippet(config.domain))
    print("\nHealth payload:")
    print(health_payload(config.debug))

    assert config.debug is False
    assert "proxy_pass" in nginx_snippet(config.domain)
    print("Validation checked production-safe defaults and reverse proxy wiring.")


if __name__ == "__main__":
    main()
