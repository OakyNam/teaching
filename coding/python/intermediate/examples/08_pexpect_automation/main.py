"""Demonstrate basic pexpect automation for interactive programs."""
from __future__ import annotations

import io
import shlex
import sys

try:
    import pexpect
except ImportError:  # pragma: no cover - educational fallback
    pexpect = None



def main() -> None:
    if pexpect is None:
        print("pexpect is not installed. Install it to run this lesson example.")
        return

    prompt_script = (
        "name = input('Name: ')\n"
        "code = input('Code: ')\n"
        "print(f'Access granted for {name} with {code}')\n"
    )
    transcript = io.StringIO()
    child = pexpect.spawn(sys.executable, ["-c", prompt_script], encoding="utf-8", timeout=3)
    child.logfile = transcript

    try:
        child.expect("Name:")
        child.sendline("Ava")
        child.expect("Code:")
        child.sendline("BLUE-42")
        child.expect("Access granted for Ava with BLUE-42")
        child.expect(pexpect.EOF)
    except pexpect.TIMEOUT:
        print("The interactive program took too long to respond.")
        return

    version_text = pexpect.run(f"{shlex.quote(sys.executable)} --version", encoding="utf-8").strip()
    print("Captured transcript:")
    print(transcript.getvalue().strip())
    print(f"Shell command output: {version_text}")


if __name__ == "__main__":
    main()
