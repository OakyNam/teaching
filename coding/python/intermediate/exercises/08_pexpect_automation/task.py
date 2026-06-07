"""Exercise starter for pexpect automation.

Build a small prompt script, automate it with expect/sendline, and run a
separate shell command for verification.
"""
from __future__ import annotations

try:
    import pexpect
except ImportError:  # pragma: no cover - educational fallback
    pexpect = None



def build_prompt_script() -> str:
    """Return Python code for a two-prompt interactive script."""
    raise NotImplementedError("Your implementation here")



def automate_prompt_script(name: str, code: str) -> str:
    """Use pexpect to answer both prompts and return the transcript."""
    raise NotImplementedError("Your implementation here")



def run_shell_check() -> str:
    """Run a simple shell command through pexpect.run and return its output."""
    raise NotImplementedError("Your implementation here")



def run() -> None:
    if pexpect is None:
        print("Install pexpect to complete this exercise.")
        return
    print("Implement the stubs, then call automate_prompt_script('Ava', 'BLUE-42').")
    print("Bonus: assign a logfile so you can inspect the session transcript.")


if __name__ == "__main__":
    run()
