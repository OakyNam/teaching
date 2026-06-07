"""Reference solution for lesson: 11_regex"""

from __future__ import annotations

import re
from html import unescape


EMAIL_PATTERN = re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}")
PHONE_PATTERN = re.compile(
    r"""
    ^(?:\+?1[-.\s]?)?        # optional country code
    (?:\(\d{3}\)|\d{3})    # area code
    [-.\s]?                  # optional separator
    \d{3}                    # prefix
    [-.\s]?                  # optional separator
    \d{4}$                   # line number
    """,
    re.VERBOSE,
)
LOG_PATTERN = re.compile(
    r"^(?P<date>\d{4}-\d{2}-\d{2})\s+"
    r"(?P<level>[A-Z]+)\s+"
    r"\[(?P<component>[^\]]+)\]\s+"
    r"(?P<message>.+)$"
)
TAG_PATTERN = re.compile(r"<[^>]+>")
URL_PATTERN = re.compile(r"https?://[^\s\"'<>]+")


def extract_emails(text: str) -> list[str]:
    return EMAIL_PATTERN.findall(text)


def validate_phone(phone: str) -> bool:
    return bool(PHONE_PATTERN.fullmatch(phone.strip()))


def parse_log_line(line: str) -> dict:
    match = LOG_PATTERN.fullmatch(line.strip())
    if not match:
        raise ValueError(f"Invalid log line: {line!r}")
    return match.groupdict()


def clean_html_tags(html: str) -> str:
    text = TAG_PATTERN.sub(" ", html)
    text = unescape(text)
    return re.sub(r"\s+", " ", text).strip()


def extract_urls(text: str) -> list[str]:
    return URL_PATTERN.findall(text)


def run() -> None:
    sample_text = (
        "Emails: ava@example.com, ben.smith@company.io. "
        "Links: https://example.com/docs and http://status.example.org."
    )
    print("emails:", extract_emails(sample_text))
    print("phone valid:", validate_phone("(555) 123-4567"))
    print(
        "log:",
        parse_log_line("2024-01-15 ERROR [auth] Login failed for user@example.com"),
    )
    print("html:", clean_html_tags("<p>Hello <b>world</b> &amp; team</p>"))
    print("urls:", extract_urls(sample_text))


if __name__ == "__main__":
    run()
