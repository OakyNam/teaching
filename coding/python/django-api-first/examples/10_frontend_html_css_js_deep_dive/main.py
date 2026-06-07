"""Runnable example for lesson: 10_frontend_html_css_js_deep_dive."""
from pathlib import Path


ASSET_NAMES = ("index.html", "styles.css", "app.js")


def asset_summary(path: Path) -> dict[str, bool | int]:
    content = path.read_text(encoding="utf-8")
    return {
        "lines": len(content.splitlines()),
        "has_main": "<main" in content,
        "has_css_variables": "--bg:" in content,
        "has_event_listener": "addEventListener" in content,
    }


def explain_frontend_stack() -> list[str]:
    return [
        "HTML defines accessible sections, forms, and data tables.",
        "CSS uses variables, cards, and responsive grid layout.",
        "JavaScript progressively enhances the page with fetch-like behavior.",
    ]


def design_review(asset_dir: Path) -> dict[str, int]:
    html = (asset_dir / "index.html").read_text(encoding="utf-8")
    css = (asset_dir / "styles.css").read_text(encoding="utf-8")
    js = (asset_dir / "app.js").read_text(encoding="utf-8")
    return {
        "sections": html.count("<section"),
        "css_classes": css.count("."),
        "event_handlers": js.count("addEventListener"),
    }


def main() -> None:
    asset_dir = Path(__file__).parent
    print("Frontend deep-dive asset audit:")
    for asset_name in ASSET_NAMES:
        summary = asset_summary(asset_dir / asset_name)
        print(f"- {asset_name}: {summary}")

    print("\nDesign notes:")
    for note in explain_frontend_stack():
        print(f"- {note}")

    review = design_review(asset_dir)
    print("\nDesign review counts:")
    for key, value in review.items():
        print(f"- {key}: {value}")

    html_summary = asset_summary(asset_dir / "index.html")
    js_summary = asset_summary(asset_dir / "app.js")
    assert html_summary["has_main"] is True
    assert js_summary["has_event_listener"] is True
    assert review["sections"] >= 3
    print("\nValidation: semantic HTML and interactive JavaScript are both present.")


if __name__ == "__main__":
    main()
