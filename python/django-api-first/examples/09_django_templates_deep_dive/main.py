"""Runnable example for lesson: 09_django_templates_deep_dive."""
from dataclasses import dataclass
from pathlib import Path
from textwrap import dedent


@dataclass(frozen=True)
class GlobalTemplateContext:
    environment: str
    release: str
    theme: str
    nav_items: tuple[str, ...]


def context_processor_preview() -> dict[str, str]:
    return {"environment": "teaching", "release": "2024.09", "theme": "clean"}


def child_template_snippet() -> str:
    return dedent(
        """
        {% extends 'base.html' %}
        {% block title %}Submission Queue{% endblock %}
        {% block content %}
          <section>
            <h2>Pending submissions</h2>
            <p>{{ pending_count }} records are waiting for review.</p>
          </section>
        {% endblock %}
        """
    ).strip()


def analyze_base_template(path: Path) -> dict[str, bool]:
    content = path.read_text(encoding="utf-8")
    return {
        "has_title_block": "{% block title %}" in content,
        "has_sidebar_block": "{% block sidebar %}" in content,
        "has_messages_loop": "{% for message in messages %}" in content,
        "has_footer_block": "{% block footer %}" in content,
    }


def main() -> None:
    base_path = Path(__file__).with_name("base.html")
    context = GlobalTemplateContext("teaching", "2024.09", "clean", ("Dashboard", "Status", "API health"))
    print("Context processor preview:")
    print(context_processor_preview())
    print("\nChild template example:")
    print(child_template_snippet())
    print("\nBase template analysis:")
    analysis = analyze_base_template(base_path)
    for key, value in analysis.items():
        print(f"- {key}: {value}")
    print(f"\nNavigation items: {', '.join(context.nav_items)}")

    assert all(analysis.values())
    assert context.release.count(".") == 1
    print("Validation: inheritance blocks and shared context are present.")


if __name__ == "__main__":
    main()
