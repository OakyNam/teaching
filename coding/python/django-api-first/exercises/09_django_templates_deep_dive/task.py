"""Exercise starter for lesson: 09_django_templates_deep_dive."""
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class TemplateAudit:
    extends_base: bool
    defines_content_block: bool
    uses_filters: bool


def load_page_template() -> str:
    return Path(__file__).with_name("page.html").read_text(encoding="utf-8")


def audit_template(template: str) -> TemplateAudit:
    return TemplateAudit(
        extends_base="{% extends 'base.html' %}" in template or '{% extends "base.html" %}' in template,
        defines_content_block="{% block content %}" in template,
        uses_filters="|default" in template or "|title" in template or "|length" in template,
    )


def global_context() -> dict[str, object]:
    return {
        "site_name": "Collector Console",
        "release": "2024.09",
        "links": ["Dashboard", "Status", "Learners"],
    }


def run() -> None:
    print("Exercise: extend a base template, use blocks, and rely on shared context.")
    template = load_page_template()
    audit = audit_template(template)
    broken = audit_template("<h1>raw html only</h1>")

    print(f"- Context: {global_context()}")
    print(f"- Working audit: {audit}")
    print(f"- Broken audit: {broken}")

    assert audit.extends_base is True
    assert audit.defines_content_block is True
    assert broken.extends_base is False
    print("Validation covered a correct child template and an incorrect one.")


if __name__ == "__main__":
    run()
