# 01 - Prompting Fundamentals

## Overview
A prompt is the primary interface between you and an AI agent. Clear, structured prompts consistently produce better results than vague or incomplete ones. This lesson covers the core patterns every team member should know before relying on agents in their workflow.

## Anatomy of a Good Prompt
Every effective prompt has four components:

1. **Role / context** — tell the agent who it is and what situation it is operating in.
2. **Task** — describe precisely what you want the agent to do.
3. **Constraints** — specify format, scope limits, tone, or what to avoid.
4. **Output format** — describe what a correct response looks like.

## Core Prompting Patterns

### Zero-shot
Ask the agent to complete a task without any examples. Works well for well-defined, familiar tasks.
```
Summarize the following incident report in three bullet points.
```

### Few-shot
Provide one or more examples of the desired input → output pattern before giving the real input.
```
Example:
Input: "Server rebooted unexpectedly."
Output: severity=high, category=availability

Now classify:
Input: "DNS lookup latency increased by 200ms."
```

### Chain-of-thought
Ask the agent to reason step by step before giving a final answer. Reduces errors on multi-step or ambiguous problems.
```
Think step by step. What are the network layers involved when a SIP INVITE fails to reach its destination?
```

### Role assignment
Anchor the agent in a specific persona to sharpen relevance.
```
You are a senior network automation engineer reviewing a Python script that manages Cisco device configs via RESTCONF.
```

## Common Mistakes
- **Too vague**: "Help me with networking" gives the agent nothing to act on.
- **No constraints**: Leaving out format or scope requirements produces inconsistent output.
- **Treating first output as final**: Iterate. Refine the prompt when the first response misses the mark.
- **Ignoring context window limits**: Long conversations drift. Restart with a clean, focused prompt for new tasks.

## Exercises
- Exercise: [exercises/01_prompting_fundamentals/task.py](./exercises/01_prompting_fundamentals/task.py)
- Solution: [solutions/01_prompting_fundamentals/solution.py](./solutions/01_prompting_fundamentals/solution.py)

➡️ Next: [02 - Reference Spec Building](./02_reference_spec_building.md)
