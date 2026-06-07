"""Runnable example for lesson: 01_api_first_architecture."""
from dataclasses import dataclass
from textwrap import dedent, indent


@dataclass(frozen=True)
class RouteGroup:
    name: str
    prefix: str
    owner: str
    purpose: str


API_FIRST_GROUPS = [
    RouteGroup("frontend pages", "/", "frontend_site", "Render HTML for human users."),
    RouteGroup("public api", "/api/v1/", "backend_api", "Serve stable JSON contracts."),
    RouteGroup("staff admin", "/admin/", "django.contrib.admin", "Operate the system internally."),
]

PAGE_FIRST_GROUPS = [
    RouteGroup("mixed pages", "/", "monolith", "Templates, forms, and JSON live together."),
    RouteGroup("ajax endpoints", "/ajax/", "monolith", "API behavior grows out of page handlers."),
]


def describe(groups: list[RouteGroup]) -> str:
    lines = []
    for group in groups:
        lines.append(f"- {group.prefix:<10} {group.name:<14} owner={group.owner}")
        lines.append(f"  purpose: {group.purpose}")
    return "\n".join(lines)


def project_tree() -> str:
    return dedent(
        """
        config/
            settings.py    # shared Django configuration
            urls.py        # top-level routing split by responsibility
        frontend_site/
            views.py       # page views and templates
            urls.py        # HTML routes only
        backend_api/
            serializers.py # data contracts
            views.py       # APIView or ViewSet classes
            urls.py        # versioned API routes
        """
    ).strip()


def request_flow(page_path: str, api_path: str) -> str:
    return dedent(
        f"""
        Browser GET {page_path}
          -> frontend_site renders HTML shell
          -> JavaScript calls {api_path}
          -> backend_api returns JSON payload
          -> frontend updates the visible state without changing ownership
        """
    ).strip()


def main() -> None:
    print("API-first architecture keeps frontend rendering and API contracts separate.")
    print("\nAPI-first routing:")
    print(describe(API_FIRST_GROUPS))
    print("\nPage-first routing:")
    print(describe(PAGE_FIRST_GROUPS))
    print("\nRecommended project structure:")
    print(indent(project_tree(), "  "))
    flow = request_flow("/", "/api/v1/health/")
    print("\nTypical request flow:")
    print(indent(flow, "  "))

    api_prefixes = [group.prefix for group in API_FIRST_GROUPS]
    assert "/api/v1/" in api_prefixes, "Version your API from the start."
    assert API_FIRST_GROUPS[0].owner != API_FIRST_GROUPS[1].owner
    print("\nValidation: frontend and backend have independent route ownership.")


if __name__ == "__main__":
    main()
