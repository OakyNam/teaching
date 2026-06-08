"""
Example: Planning conversation scaffolding.

Demonstrates generating the structured planning prompts used at each step of a
planning-first agent conversation before any execution begins.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import List


@dataclass
class PlanningConversation:
    """Generates the ordered prompts for a planning-first agent session."""

    task_summary: str
    spec_text: str
    plan_steps: List[str]

    def understanding_check(self) -> str:
        return (
            f"Before we start, summarize what needs to be done based on this spec:\n\n"
            f"{self.spec_text}\n\n"
            "Do not write any code or make any changes yet."
        )

    def request_plan(self) -> str:
        return (
            "Give me a numbered plan, one step per action. "
            "Do not combine multiple changes into a single step. "
            "Do not execute anything yet."
        )

    def challenge_step(self, step_number: int, step_description: str) -> str:
        return (
            f'Step {step_number} says "{step_description}". '
            "What exactly would change? Can this be scoped more narrowly?"
        )

    def reversibility_check(self, step_number: int) -> str:
        return (
            f"If step {step_number} fails midway, what is the state of the system "
            "and how do we recover?"
        )

    def approve_and_execute(self, step_number: int) -> str:
        return (
            f"Step {step_number} looks good. "
            f"Execute only step {step_number} and stop. "
            "Show me the output before continuing."
        )

    def generate_session_outline(self) -> str:
        lines: List[str] = [
            f"# Planning Session: {self.task_summary}",
            "",
            "## 1. Understanding Check",
            self.understanding_check(),
            "",
            "## 2. Request Plan",
            self.request_plan(),
            "",
            "## 3. Step Review Prompts",
        ]
        for i, step in enumerate(self.plan_steps, 1):
            lines.append(f"### Step {i}: {step}")
            lines.append(self.challenge_step(i, step))
            lines.append("")
            lines.append(self.reversibility_check(i))
            lines.append("")
            lines.append(self.approve_and_execute(i))
            lines.append("")
        return "\n".join(lines)


def main() -> None:
    conversation = PlanningConversation(
        task_summary="Add retry logic to the RDS connection helper",
        spec_text=(
            "Add exponential backoff retry logic to the connect() function in\n"
            "cloud/aws/rds/examples/01_connect_and_query/main.py.\n"
            "Max 3 retries, starting at 1 second, doubling each attempt.\n"
            "Log each retry attempt at WARNING level."
        ),
        plan_steps=[
            "Add a retry loop with exponential backoff around the connect call",
            "Log each retry attempt using the logging module",
            "Raise the original exception after all retries are exhausted",
            "Add a unit test that asserts three retries are attempted on failure",
        ],
    )
    print(conversation.generate_session_outline())


if __name__ == "__main__":
    main()
