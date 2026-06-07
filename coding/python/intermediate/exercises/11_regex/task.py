"""Exercise starter for lesson: 11_regex"""


def extract_emails(text: str) -> list[str]:
    """TODO: Return every email address found in *text*."""
    return []


def validate_phone(phone: str) -> bool:
    """TODO: Return True when *phone* matches a common US phone format."""
    return False


def parse_log_line(line: str) -> dict:
    """TODO: Parse a log line into date, level, component, and message fields."""
    return {"date": "", "level": "", "component": "", "message": line}


def clean_html_tags(html: str) -> str:
    """TODO: Strip HTML tags and return readable plain text."""
    return html


def extract_urls(text: str) -> list[str]:
    """TODO: Return every http/https URL found in *text*."""
    return []


def run() -> None:
    print("Implement the regex exercise functions in this file.")
    print("Starter result:", extract_emails("Contact me at ava@example.com"))


if __name__ == "__main__":
    run()
