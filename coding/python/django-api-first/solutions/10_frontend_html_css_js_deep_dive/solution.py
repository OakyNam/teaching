"""Reference solution for lesson: 10_frontend_html_css_js_deep_dive."""
from pathlib import Path
from textwrap import dedent


ASSET_DIR = Path(__file__).parent


def load(name: str) -> str:
    return (ASSET_DIR / name).read_text(encoding="utf-8")


def solution_checks() -> dict[str, bool]:
    html = load("index.html")
    css = load("styles.css")
    js = load("app.js")
    return {
        "semantic_structure": "<main" in html and "<table" in html,
        "responsive_css": "@media" in css and "--surface:" in css,
        "interactive_js": "fetchHealth" in js and "addEventListener" in js,
        "progressive_validation": "validateEmail" in js and "subscriber-message" in html,
    }


def endpoint_contract() -> str:
    return dedent(
        """
        GET /api/v1/health/ -> {"status": "ok", "checked_at": "..."}
        GET /api/v1/submissions/ -> [{"learner": "Amina", "source": "web", "score": 97, "status": "accepted"}]
        POST /api/v1/subscribers/ -> {"email": "learner@example.com"}
        """
    ).strip()


def asset_lengths() -> dict[str, int]:
    return {name: len(load(name).splitlines()) for name in ("index.html", "styles.css", "app.js")}


def run() -> None:
    print("Solution asset checks:")
    checks = solution_checks()
    for key, value in checks.items():
        print(f"- {key}: {value}")

    print("\nRecommended endpoint contract:")
    print(endpoint_contract())
    print("\nAsset lengths:")
    print(asset_lengths())

    assert all(checks.values())
    assert "pill--ok" in load("styles.css")
    print("Validation: the completed HTML, CSS, and JS assets are consistent and educational.")


if __name__ == "__main__":
    run()
