"""
Exercise 03 - Planning with Agents Before Execution

Read the scenario below. Then write the five planning prompts that you would
send to an agent before asking it to execute any changes.

Fill in each function so it returns an appropriate prompt string.
"""

from __future__ import annotations

# Scenario:
# You want an agent to add structured JSON logging to a FastAPI application.
# The app currently uses print() statements for output. You want all log lines
# to include a timestamp, log level, request ID, and message field.
# The change must not break any existing endpoints or tests.


def understanding_check_prompt() -> str:
    """
    Return a prompt that asks the agent to summarize what it understands about
    the task before it starts. It should NOT write any code yet.
    """
    # TODO
    raise NotImplementedError


def request_plan_prompt() -> str:
    """
    Return a prompt that asks the agent for a numbered, step-by-step plan.
    Remind it to keep steps atomic and not execute yet.
    """
    # TODO
    raise NotImplementedError


def challenge_step_prompt(step_number: int, step_description: str) -> str:
    """
    Return a prompt that challenges a specific plan step, asking the agent to
    clarify exactly what would change and whether the scope can be reduced.
    """
    # TODO
    raise NotImplementedError


def reversibility_prompt(step_number: int) -> str:
    """
    Return a prompt that asks the agent what the system state would be if the
    given step fails midway and how to recover.
    """
    # TODO
    raise NotImplementedError


def approve_step_prompt(step_number: int) -> str:
    """
    Return a prompt that approves only the given step and instructs the agent
    to stop and show output before continuing.
    """
    # TODO
    raise NotImplementedError


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
