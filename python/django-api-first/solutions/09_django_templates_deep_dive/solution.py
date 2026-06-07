"""Reference solution for lesson: 09_django_templates_deep_dive."""
from dataclasses import dataclass
from pathlib import Path
from textwrap import dedent


@dataclass(frozen=True)
class ContextProcessorExample:
    function_name: str
    keys: tuple[str, ...]


def context_processor_snippet() -> str:
    return dedent(
        """
        def global_ui_context(request):
            return {
                'release': '2024.09',
                'environment': 'production',
                'support_email': 'ops@example.com',
            }
        """
    ).strip()


def solution_template_audit() -> dict[str, bool]:
    template = Path(__file__).with_name("page.html").read_text(encoding="utf-8")
    return {
        "extends_base": "{% extends 'base.html' %}" in template,
        "uses_sidebar_block": "{% block sidebar %}" in template,
        "uses_footer_block": "{% block footer %}" in template,
        "uses_title_filter": "|title" in template,
    }


def run() -> None:
    example = ContextProcessorExample("global_ui_context", ("release", "environment", "support_email"))
    print("Context processor solution:")
    print(context_processor_snippet())
    print("\nRegistered keys:")
    print(example)
    print("\nTemplate audit:")
    audit = solution_template_audit()
    for key, value in audit.items():
        print(f"- {key}: {value}")

    assert all(audit.values())
    assert example.function_name.endswith("context")
    print("Validation: the solution uses inheritance, filters, and shared context.")


if __name__ == "__main__":
    run()
