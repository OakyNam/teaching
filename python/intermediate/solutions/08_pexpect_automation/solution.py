"""Reference solution for pexpect automation."""
        from __future__ import annotations

        import io
        import shlex
        import sys

        try:
            import pexpect
        except ImportError:  # pragma: no cover - educational fallback
            pexpect = None


        def build_prompt_script() -> str:
            return (
                "name = input('Name: ')
"
                "code = input('Code: ')
"
                "print(f'Access granted for {name} with {code}')
"
            )


        def automate_prompt_script(name: str, code: str) -> str:
            transcript = io.StringIO()
            child = pexpect.spawn(sys.executable, ["-c", build_prompt_script()], encoding="utf-8", timeout=3)
            child.logfile = transcript
            child.expect("Name:")
            child.sendline(name)
            child.expect("Code:")
            child.sendline(code)
            child.expect(f"Access granted for {name} with {code}")
            child.expect(pexpect.EOF)
            return transcript.getvalue().strip()


        def run_shell_check() -> str:
            return pexpect.run(f"{shlex.quote(sys.executable)} --version", encoding="utf-8").strip()


        def run() -> None:
            if pexpect is None:
                print("pexpect is not installed. Install it to run this solution.")
                return
            print(automate_prompt_script("Ava", "BLUE-42"))
            print(run_shell_check())


        if __name__ == "__main__":
            run()
