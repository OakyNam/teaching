"""Exercise starter for lesson: 01_api_first_architecture."""
from dataclasses import dataclass


@dataclass(frozen=True)
class FlowNote:
    frontend_route: str
    api_route: str
    owner: str
    summary: str


def build_versioned_api_prefix(version: str) -> str:
    cleaned = version.strip().lower().replace(" ", "-")
    return f"/api/{cleaned.strip('/')}/"


def build_status_page_context(api_status: str) -> dict[str, str]:
    badge = "healthy" if api_status == "ok" else "degraded"
    return {
        "title": "Collector dashboard",
        "api_status": api_status,
        "badge_class": f"badge badge--{badge}",
    }


def document_data_flow(frontend_route: str, api_route: str, owner: str) -> FlowNote:
    summary = (
        f"The page at {frontend_route} renders first, then requests {api_route}. "
        f"The {owner} team owns the JSON contract."
    )
    return FlowNote(frontend_route, api_route, owner, summary)


def validate_flow(note: FlowNote) -> bool:
    return note.frontend_route.startswith("/") and note.api_route.startswith("/api/")


def run() -> None:
    print("Tasks: add /api/v1/, show API status on a frontend route, and explain ownership.")
    print("Use these helpers as your starter implementation and refine them as you learn.")

    prefix = build_versioned_api_prefix("v1")
    context = build_status_page_context("ok")
    note = document_data_flow("/status/", f"{prefix}health/", "backend_api")
    broken = document_data_flow("status", "/health/", "frontend_site")

    print(f"Versioned prefix: {prefix}")
    print(f"Status badge: {context['badge_class']}")
    print(f"Flow note: {note.summary}")
    print(f"Valid note? {validate_flow(note)}")
    print(f"Broken note? {validate_flow(broken)}")

    assert validate_flow(note) is True
    assert validate_flow(broken) is False
    print("Validation covered one passing path and one failing path.")


if __name__ == "__main__":
    run()
