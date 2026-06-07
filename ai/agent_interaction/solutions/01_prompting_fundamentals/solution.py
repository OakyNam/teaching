"""
Solution 01 - Prompting Fundamentals
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


def build_incident_summary_prompt() -> str:
    return Prompt(
        role="a site reliability engineer",
        task="Summarize the following incident report in three bullet points.",
        output_format="A markdown list with exactly three items.",
    ).render()


def build_log_classifier_prompt() -> str:
    return Prompt(
        role="an incident classifier",
        task=(
            "Classify the following log line by severity and category.\n\n"
            "Example:\n"
            'Input: "Server rebooted unexpectedly."\n'
            "Output: severity=high, category=availability\n\n"
            "Now classify:\n"
            'Input: "Database query took 4500ms."'
        ),
        constraints=[
            "Use only: severity=low/medium/high",
            "Use only: category=availability/performance/security",
        ],
        output_format="severity=<value>, category=<value>",
    ).render()


def build_root_cause_prompt() -> str:
    return Prompt(
        role="a senior backend engineer",
        task=(
            "Think step by step. "
            "Why might a service start returning HTTP 503 responses after a deployment?"
        ),
        output_format="Numbered reasoning steps followed by a one-sentence conclusion.",
    ).render()


def main() -> None:
    for name, fn in [
        ("incident summary", build_incident_summary_prompt),
        ("log classifier", build_log_classifier_prompt),
        ("root cause", build_root_cause_prompt),
    ]:
        print(f"--- {name} ---")
        print(fn())
        print()


if __name__ == "__main__":
    main()
