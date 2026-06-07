"""Reference solution for lesson: 03_frontend_site_app."""
from dataclasses import dataclass
from textwrap import dedent


@dataclass(frozen=True)
class PageRoute:
    path: str
    name: str
    template_name: str
    api_dependency: str


def urlconf_snippet() -> str:
    return dedent(
        """
        urlpatterns = [
            path('', views.home, name='home'),
            path('status/', views.status, name='status'),
        ]
        """
    ).strip()


def build_status_context(status: str) -> dict[str, str]:
    return {
        "title": "Status page",
        "badge_class": "badge badge--success" if status == "ok" else "badge badge--warning",
        "status": status,
        "health_endpoint": "/api/v1/health/",
    }


def route_inventory() -> list[PageRoute]:
    return [
        PageRoute("/", "home", "frontend_site/home.html", "/api/v1/health/"),
        PageRoute("/status/", "status", "frontend_site/status.html", "/api/v1/health/"),
    ]


def run() -> None:
    print("Frontend URL configuration:")
    print(urlconf_snippet())
    context = build_status_context("ok")
    print("\nStatus page context:")
    for key, value in context.items():
        print(f"- {key}: {value}")

    routes = route_inventory()
    print("\nRoute inventory:")
    for route in routes:
        print(f"- {route.path:<8} {route.template_name:<26} depends on {route.api_dependency}")

    assert all(route.template_name.startswith("frontend_site/") for route in routes)
    assert context["health_endpoint"].startswith("/api/v1/")
    assert build_status_context("down")["badge_class"].endswith("warning")
    print("\nValidation: routes, templates, and status badge behavior are correct.")


if __name__ == "__main__":
    run()
