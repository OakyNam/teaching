# 11 - Python Regex
## Overview
Regular expressions (regex) are compact text patterns used to search, extract, validate, and transform strings. In Python, regex is most useful when plain string methods are too rigid: validating emails or phone numbers, pulling IDs out of logs, cleaning HTML-like text, or splitting inconsistent user input.

### What regex is and when to use it
Regex describes *patterns* instead of exact text. That makes it ideal for:
- **Pattern matching**: check whether data follows a format.
- **Extraction**: pull emails, URLs, numbers, tags, or tokens from text.
- **Validation**: confirm whether a string matches a required structure.
- **Transformation**: replace or clean matching text with `re.sub()`.

Use regex when the data is semi-structured. For plain fixed substrings, `in`, `.split()`, or `.replace()` are often simpler.

## Learning Goals
- Use the `re` module to match, search, extract, split, and replace text.
- Understand core pattern syntax such as character classes, anchors, groups, and quantifiers.
- Recognize greedy vs lazy matching and choose the right one.
- Parse realistic text such as logs, contact lists, and HTML-like snippets.
- Write readable, reusable patterns with `re.compile()` and `re.VERBOSE`.

## Core Example
```python
import re

text = "Contact ava@example.com or ben@example.org for support."
pattern = re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}")
print(pattern.findall(text))
```

### The `re` module toolbox
Python's `re` module provides several entry points:

| Function | Use case |
|---|---|
| `re.match(pattern, text)` | Match only at the **start** of the string. |
| `re.search(pattern, text)` | Find the **first** match anywhere in the string. |
| `re.findall(pattern, text)` | Return all matches as a list. |
| `re.finditer(pattern, text)` | Return match objects for all matches. |
| `re.sub(pattern, repl, text)` | Replace matches with new text. |
| `re.split(pattern, text)` | Split text by a regex delimiter. |

```python
import re

sample = "Order #123 shipped on 2024-01-15"
print(re.match(r"Order", sample).group())
print(re.search(r"\d{4}-\d{2}-\d{2}", sample).group())
print(re.findall(r"\d+", sample))
for match in re.finditer(r"\d+", sample):
    print(match.group(), match.span())
print(re.sub(r"\d", "X", sample))
print(re.split(r"[ #-]", sample))
```

### Pattern basics
These symbols appear in most regex patterns:

| Pattern | Meaning |
|---|---|
| `.` | Any character except newline (unless `re.DOTALL` is used). |
| `*` | Zero or more of the previous token. |
| `+` | One or more of the previous token. |
| `?` | Zero or one of the previous token. |
| `^` | Start of string or line. |
| `$` | End of string or line. |
| `[]` | Character set or range, such as `[A-Z]`. |
| `|` | OR operator. |
| `()` | Capturing group. |

Examples:
- `cat|dog` matches either `cat` or `dog`
- `colou?r` matches `color` and `colour`
- `^[A-Z][a-z]+$` matches a capitalized word

### Character classes
Shortcut classes make patterns shorter and easier to read:

| Class | Meaning |
|---|---|
| `\d` | Digit |
| `\D` | Not a digit |
| `\w` | Word character: letters, digits, underscore |
| `\W` | Not a word character |
| `\s` | Whitespace |
| `\S` | Not whitespace |
| `\b` | Word boundary |
| `\B` | Not a word boundary |

```python
import re

text = "Room 42 is on floor 7"
print(re.findall(r"\d", text))
print(re.findall(r"\w+", text))
print(re.findall(r"\b[a-zA-Z]{4}\b", text))
```

### Quantifiers and greedy vs lazy matching
Quantifiers control *how many* characters are consumed:

| Quantifier | Meaning |
|---|---|
| `{n}` | Exactly `n` times |
| `{n,}` | At least `n` times |
| `{n,m}` | Between `n` and `m` times |

By default, regex is **greedy**: it takes as much text as possible.

```python
import re

html = "<b>bold</b><i>italic</i>"
print(re.findall(r"<.*>", html))     # greedy
print(re.findall(r"<.*?>", html))    # lazy using *?
```

Lazy quantifiers stop earlier:
- `*?`
- `+?`
- `??`
- `{n,m}?`

### Groups
Groups help organize and extract parts of a match.

#### Capturing groups
Use `()` to capture pieces for later access.

```python
import re

match = re.search(r"(\d{4})-(\d{2})-(\d{2})", "2024-01-15")
print(match.group(1))  # year
print(match.group(2))  # month
print(match.group(3))  # day
```

#### Non-capturing groups
Use `(?:...)` when grouping is needed but storing the match is not.

```python
import re

pattern = r"^(?:https?://)?(?:www\.)?example\.com$"
print(bool(re.match(pattern, "https://www.example.com")))
```

#### Named groups
Use `(?P<name>...)` to give groups meaningful names.

```python
import re

log_pattern = re.compile(
    r"(?P<date>\d{4}-\d{2}-\d{2})\s+"
    r"(?P<level>INFO|WARNING|ERROR)\s+"
    r"\[(?P<component>[^\]]+)\]\s+"
    r"(?P<message>.+)"
)
match = log_pattern.search("2024-01-15 ERROR [auth] Login failed")
print(match.groupdict())
```

### Flags
Flags modify how matching works:

| Flag | Effect |
|---|---|
| `re.IGNORECASE` | Ignore letter case. |
| `re.MULTILINE` | Make `^` and `$` work per line. |
| `re.DOTALL` | Make `.` also match newlines. |

```python
import re

text = "First line\nSecond line"
print(bool(re.search(r"^Second", text, re.MULTILINE)))
print(bool(re.search(r"first", text, re.IGNORECASE)))
print(bool(re.search(r"First.*Second", text, re.DOTALL)))
```

### Compiled patterns with `re.compile()`
If you reuse the same regex many times, compile it once.

```python
import re

email_pattern = re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}")
for text in ["a@example.com", "not-an-email", "b@test.org"]:
    print(text, bool(email_pattern.fullmatch(text)))
```

Compiled patterns improve readability and can improve performance in repeated use.

### `re.VERBOSE` for readable patterns
Complex regex becomes easier to maintain when spaces and comments are allowed.

```python
import re

phone_pattern = re.compile(
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
```

### Common real-world patterns
#### Email extraction
```python
email_pattern = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"
```
This is good for extraction. Very strict email validation usually requires more than regex alone.

#### US phone numbers
```python
phone_pattern = r"^(?:\+?1[-.\s]?)?(?:\(\d{3}\)|\d{3})[-.\s]?\d{3}[-.\s]?\d{4}$"
```
Matches values such as `555-123-4567`, `(555) 123-4567`, and `+1 555 123 4567`.

#### URL extraction
```python
url_pattern = r"https?://[^\s\"'<>]+"
```
Useful for pulling links out of plain text or HTML-like content.

#### Log parsing
```python
log_pattern = r"(?P<date>\d{4}-\d{2}-\d{2}) (?P<level>INFO|ERROR) \[(?P<component>[^\]]+)\] (?P<message>.+)"
```
Named groups make downstream processing easier.

### Practical examples with realistic input data
```python
import re

text = """
Team contacts: ava@example.com, ben.smith@company.io
Emergency line: (555) 123-4567
Docs: https://docs.example.com/start
"""

print(re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", text))
print(re.findall(r"https?://[^\s]+", text))
print(re.sub(r"\s+", " ", text).strip())
```

## Exercises
1. Implement `extract_emails(text: str) -> list[str]` to find every email in a larger block of text.
2. Implement `validate_phone(phone: str) -> bool` for common US phone formats.
3. Implement `parse_log_line(line: str) -> dict` for lines like `2024-01-15 ERROR [auth] Login failed for user@example.com`.
4. Implement `clean_html_tags(html: str) -> str` to strip HTML tags and return readable text.
5. Implement `extract_urls(text: str) -> list[str]` for `http` and `https` links.
---
## Answer Key
1. Use `re.findall()` with a reusable email pattern.
2. Anchor the pattern with `^` and `$` and allow optional separators and country code.
3. Use named groups with `groupdict()` for `date`, `level`, `component`, and `message`.
4. Remove tags with `re.sub()` and normalize whitespace.
5. Match `https?://` followed by non-space, non-tag characters.
---
⬅️ Previous: [10 - OOP Design Concepts (Composition, SOLID, and Interfaces)](./10_oop_design_concepts.md)
➡️ Next: [12 - Python JSON](./12_json.md)
