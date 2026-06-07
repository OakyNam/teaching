"""Exercise starter for lesson: 10_frontend_html_css_js_deep_dive."""
from pathlib import Path


ASSET_DIR = Path(__file__).parent


def read_asset(name: str) -> str:
    return (ASSET_DIR / name).read_text(encoding="utf-8")


def asset_checks() -> dict[str, bool]:
    html = read_asset("index.html")
    css = read_asset("styles.css")
    js = read_asset("app.js")
    return {
        "semantic_main": "<main" in html,
        "css_variables": "--bg:" in css,
        "event_listener": "addEventListener" in js,
        "table_body_hook": "results-body" in html and "resultsBody" in js,
    }


def asset_lengths() -> dict[str, int]:
    return {name: len(read_asset(name).splitlines()) for name in ("index.html", "styles.css", "app.js")}


def teaching_notes() -> list[str]:
    return [
        "Keep semantic structure in HTML so assistive technology understands the page.",
        "Use CSS variables for reusable color and spacing choices.",
        "Let JavaScript enhance the table instead of owning the whole page render.",
    ]


def run() -> None:
    print("Exercise: build a semantic, responsive page with vanilla JavaScript.")
    checks = asset_checks()
    broken = {"semantic_main": False, "css_variables": False, "event_listener": False, "table_body_hook": False}
    print(f"- Starter asset checks: {checks}")
    print(f"- Asset lengths: {asset_lengths()}")
    for note in teaching_notes():
        print(f"- {note}")
    print(f"- Broken comparison: {broken}")

    assert all(checks.values())
    assert not all(broken.values())
    print("Validation covered a working asset bundle and a deliberately broken comparison.")


if __name__ == "__main__":
    run()
