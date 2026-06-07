"""Runnable example for lesson: 03_frontend_site_app."""
from dataclasses import dataclass
from textwrap import dedent


@dataclass(frozen=True)
class FrontendRoute:
    path: str
    url_name: str
    template_name: str
    description: str


def route_table() -> list[FrontendRoute]:
    return [
        FrontendRoute("/", "home", "frontend_site/home.html", "Landing page for collectors."),
        FrontendRoute("/status/", "status", "frontend_site/status.html", "Human-friendly API health page."),
    ]


def home_view_snippet() -> str:
    return dedent(
        """
        def home(request):
            context = {
                'headline': 'API-first Django starter',
                'status_url': '/status/',
                'health_endpoint': '/api/v1/health/',
            }
            return render(request, 'frontend_site/home.html', context)
        """
    ).strip()


def render_preview(context: dict[str, str]) -> str:
    return f"{context['headline']} -> status page: {context['status_url']} -> API: {context['health_endpoint']}"


def main() -> None:
    print("Dedicated frontend app routes only render HTML pages.")
    for route in route_table():
        print(f"- {route.path:<8} name={route.url_name:<7} template={route.template_name}")
        print(f"  {route.description}")

    print("\nView example:")
    print(home_view_snippet())
    preview = render_preview(
        {
            "headline": "Frontend site app",
            "status_url": "/status/",
            "health_endpoint": "/api/v1/health/",
        }
    )
    print("\nTemplate preview:")
    print(preview)

    assert all(route.template_name.startswith("frontend_site/") for route in route_table())
    assert "/api/v1/" in preview
    print("\nValidation: frontend routes render templates and link to a versioned API.")


if __name__ == "__main__":
    main()
