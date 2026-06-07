"""Exercise starter for lesson: 03_frontend_site_app."""
from dataclasses import dataclass


@dataclass(frozen=True)
class HomeContext:
    headline: str
    badge_text: str
    api_link: str


def build_home_context(api_ok: bool) -> HomeContext:
    return HomeContext(
        headline="Collection portal",
        badge_text="API healthy" if api_ok else "API unavailable",
        api_link="/api/v1/health/",
    )


def build_route_pattern(name: str) -> str:
    return f"path('{name}/', views.{name}, name='{name}')"


def validate_template_name(template_name: str) -> bool:
    return template_name.startswith("frontend_site/") and template_name.endswith(".html")


def run() -> None:
    print("Exercise: wire a frontend Django app with routes, views, and templates.")
    context = build_home_context(api_ok=True)
    good_template = "frontend_site/home.html"
    bad_template = "home.txt"

    print(f"- Headline: {context.headline}")
    print(f"- Badge: {context.badge_text}")
    print(f"- Route starter: {build_route_pattern('status')}")
    print(f"- Good template valid? {validate_template_name(good_template)}")
    print(f"- Bad template valid? {validate_template_name(bad_template)}")

    assert validate_template_name(good_template) is True
    assert validate_template_name(bad_template) is False
    assert context.api_link.startswith("/api/v1/")
    print("Validation confirms one working and one failing template path.")


if __name__ == "__main__":
    run()
