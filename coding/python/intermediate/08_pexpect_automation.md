# 08 - pexpect Automation
## Overview
Automate interactive CLI programs in Python using `pexpect` for reliable scripted workflows.
## Learning Goals
- Spawn interactive processes.
- Match expected prompts and send responses.
- Capture outputs for validation and logs.
## Core Example
```python
import pexpect
child = pexpect.spawn("python", encoding="utf-8")
child.expect(">>>")
child.sendline('print("hello")')
child.expect("hello")
child.sendline("exit()")
```
## Exercises
1. Automate two sequential prompts from a script.
2. Add timeout handling and fallback behavior.
3. Save session output to a log file.
---
## Answer Key
1. Chain `expect`/`sendline` calls for each prompt.
2. Catch `pexpect.TIMEOUT` and print recovery guidance.
3. Assign `child.logfile` to a writable file handle.
---
⬅️ Previous: [07 - Pandas Fundamentals](./07_pandas_fundamentals.md)
