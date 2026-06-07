"""Reference solution for lesson: 01_api_first_architecture."""
from dataclasses import dataclass
from textwrap import dedent


@dataclass(frozen=True)
class Boundary:
    url_prefix: str
    owner: str
    payload: str


def build_root_urlconf() -> str:
    return dedent(
        """
        urlpatterns = [
            path('', include('frontend_site.urls')),
            path('api/v1/', include('backend_api.urls')),
            path('admin/', admin.site.urls),
        ]
        """
    ).strip()


def status_page_context(status: str) -> dict[str, str]:
    tone = "success" if status == "ok" else "warning"
    return {
        "page_title": "System status",
        "status": status,
        "badge_class": f"badge badge--{tone}",
        "api_link": "/api/v1/health/",
    }


def document_boundaries() -> list[Boundary]:
    return [
        Boundary("/", "frontend_site", "HTML templates and page chrome"),
        Boundary("/api/v1/", "backend_api", "JSON serialized resources"),
        Boundary("/admin/", "django admin", "Staff-only operational tooling"),
    ]


def validate_boundary(boundary: Boundary) -> bool:
    return boundary.url_prefix.startswith("/") and boundary.owner != "" and boundary.payload != ""


def run() -> None:
    print("Versioned API-first URL configuration:")
    print(build_root_urlconf())
    context = status_page_context("ok")
    print("\nFrontend status page context:")
    for key, value in context.items():
        print(f"- {key}: {value}")

    print("\nOwnership boundaries:")
    boundaries = document_boundaries()
    for boundary in boundaries:
        print(f"- {boundary.url_prefix:<9} owner={boundary.owner:<13} payload={boundary.payload}")

    broken = Boundary("api/v1/", "", "")
    assert all(validate_boundary(item) for item in boundaries)
    assert validate_boundary(broken) is False
    assert context["api_link"].startswith("/api/v1/")
    print("\nValidation: versioning, status rendering, and ownership checks all passed.")


if __name__ == "__main__":
    run()
