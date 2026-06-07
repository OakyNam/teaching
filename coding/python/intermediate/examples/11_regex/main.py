"""Runnable example for lesson: 11_regex"""

import re


EMAIL_PATTERN = re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}")
PHONE_PATTERN = re.compile(r"(?:\+?1[-.\s]?)?(?:\(\d{3}\)|\d{3})[-.\s]?\d{3}[-.\s]?\d{4}")
LOG_PATTERN = re.compile(
    r"(?P<date>\d{4}-\d{2}-\d{2})\s+"
    r"(?P<level>INFO|WARNING|ERROR)\s+"
    r"\[(?P<component>[^\]]+)\]\s+"
    r"(?P<message>.+)"
)
URL_PATTERN = re.compile(r"https?://[^\s\"'<>]+")


def show_basic_patterns() -> None:
    print("== Basic patterns ==")
    text = "Order #451 shipped on 2024-01-15"
    print("match:", re.match(r"Order", text).group())
    print("search:", re.search(r"\d{4}-\d{2}-\d{2}", text).group())
    print("findall:", re.findall(r"\d+", text))
    print("finditer spans:", [match.span() for match in re.finditer(r"\d+", text)])
    print()


def extract_contacts() -> None:
    print("== Email and phone extraction ==")
    text = (
        "Contact ava@example.com, ben.smith@company.io, or support@test.org. "
        "Call (555) 123-4567 or +1 555 444 9999."
    )
    print("emails:", EMAIL_PATTERN.findall(text))
    print("phones:", PHONE_PATTERN.findall(text))
    print()


def parse_log_line() -> None:
    print("== Log parsing with named groups ==")
    line = "2024-01-15 ERROR [auth] Login failed for user@example.com"
    match = LOG_PATTERN.search(line)
    if match:
        print(match.groupdict())
    print()


def extract_urls() -> None:
    print("== URL extraction ==")
    html_like = (
        '<a href="https://example.com/docs">Docs</a> '
        '<img src="http://cdn.example.com/image.png"> '
        'Backup: https://status.example.com'
    )
    print(URL_PATTERN.findall(html_like))
    print()


def clean_data() -> None:
    print("== Data cleaning with re.sub ==")
    messy = "User\tName:   Ava\nStatus:   active   "
    cleaned = re.sub(r"\s+", " ", messy).strip()
    no_labels = re.sub(r"(?:User\s+Name|Status):\s*", "", cleaned)
    print("cleaned:", cleaned)
    print("labels removed:", no_labels)
    print()


def compiled_patterns() -> None:
    print("== Compiled pattern reused ==")
    usernames = ["alice_01", "invalid-user!", "BOB42", "ok_name"]
    username_pattern = re.compile(r"^[A-Za-z0-9_]{3,12}$")
    results = {name: bool(username_pattern.fullmatch(name)) for name in usernames}
    print(results)
    print()


def main() -> None:
    show_basic_patterns()
    extract_contacts()
    parse_log_line()
    extract_urls()
    clean_data()
    compiled_patterns()


if __name__ == "__main__":
    main()
