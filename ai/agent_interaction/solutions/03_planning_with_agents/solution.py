"""
Solution 03 - Planning with Agents Before Execution
"""

from __future__ import annotations


def understanding_check_prompt() -> str:
    return (
        "Before we start, summarize what needs to be done based on the spec provided. "
        "Cover: what the change is, which files are affected, and what success looks like. "
        "Do not write any code or make any changes yet."
    )


def request_plan_prompt() -> str:
    return (
        "Give me a numbered plan, one step per action. "
        "Each step should describe a single, atomic change. "
        "Do not combine multiple changes into one step. "
        "Do not execute anything yet."
    )


def challenge_step_prompt(step_number: int, step_description: str) -> str:
    return (
        f'Step {step_number} says "{step_description}". '
        "What exactly would change in the codebase? "
        "Which files and lines are affected? "
        "Can this step be scoped more narrowly without losing its intent?"
    )


def reversibility_prompt(step_number: int) -> str:
    return (
        f"If step {step_number} fails midway through execution, "
        "what is the state of the codebase or system at that point? "
        "What is the recovery procedure?"
    )


def approve_step_prompt(step_number: int) -> str:
    return (
        f"Step {step_number} looks good. "
        f"Execute only step {step_number} now and stop immediately after. "
        "Show me the full output or diff before we discuss the next step."
    )


def main() -> None:
    print("=== Understanding Check ===")
    print(understanding_check_prompt())
    print()
    print("=== Request Plan ===")
    print(request_plan_prompt())
    print()
    print("=== Challenge Step 2 ===")
    print(challenge_step_prompt(2, "Replace all print() calls with logger calls"))
    print()
    print("=== Reversibility Check for Step 2 ===")
    print(reversibility_prompt(2))
    print()
    print("=== Approve Step 1 ===")
    print(approve_step_prompt(1))


if __name__ == "__main__":
    main()
