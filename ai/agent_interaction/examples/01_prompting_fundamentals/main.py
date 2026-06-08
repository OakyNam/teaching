"""
Example: Prompt construction helpers.

Demonstrates building structured prompts programmatically using the four-component
pattern: role/context, task, constraints, and output format.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class Prompt:
    role: str
    task: str
    constraints: List[str] = field(default_factory=list)
    output_format: Optional[str] = None

    def render(self) -> str:
        parts: List[str] = []
        parts.append(f"You are {self.role}.")
        parts.append(self.task)
        if self.constraints:
            parts.append("Constraints:")
            for constraint in self.constraints:
                parts.append(f"- {constraint}")
        if self.output_format:
            parts.append(f"Output format: {self.output_format}")
        return "\n".join(parts)


def zero_shot_example() -> str:
    p = Prompt(
        role="a senior network automation engineer",
        task="Summarize the following incident report in three bullet points.",
        output_format="A markdown list with exactly three items.",
    )
    return p.render()


def few_shot_example() -> str:
    p = Prompt(
        role="an incident classifier",
        task=(
            "Classify the following event.\n\n"
            "Example:\n"
            'Input: "Server rebooted unexpectedly."\n'
            "Output: severity=high, category=availability\n\n"
            'Now classify:\n'
            'Input: "DNS lookup latency increased by 200ms."'
        ),
        constraints=["Use only the labels: severity=low/medium/high, category=availability/performance/security"],
        output_format="severity=<value>, category=<value>",
    )
    return p.render()


def chain_of_thought_example() -> str:
    p = Prompt(
        role="a network protocol expert",
        task=(
            "Think step by step. "
            "What are the network layers involved when a SIP INVITE fails to reach its destination?"
        ),
        output_format="Numbered reasoning steps followed by a one-sentence conclusion.",
    )
    return p.render()


def main() -> None:
    examples = {
        "zero-shot": zero_shot_example,
        "few-shot": few_shot_example,
        "chain-of-thought": chain_of_thought_example,
    }
    for name, fn in examples.items():
        print(f"--- {name} ---")
        print(fn())
        print()


if __name__ == "__main__":
    main()
