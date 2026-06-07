"""
Exercise 01 - Prompting Fundamentals

Complete the three functions below. Each one should return a fully rendered
prompt string using the Prompt dataclass from the example.

Run this file to print your prompts and review them.
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
    """
    Task: Build a zero-shot prompt that asks an agent to summarize an incident
    report. The agent should act as a site reliability engineer, and the output
    should be a markdown list of exactly three bullet points.
    """
    # TODO: create and return a Prompt(...).render()
    raise NotImplementedError


def build_log_classifier_prompt() -> str:
    """
    Task: Build a few-shot prompt that classifies a log line by severity and
    category. Include at least one example input/output pair in the task text.
    Constrain the output labels to: severity=low/medium/high and
    category=availability/performance/security.
    """
    # TODO: create and return a Prompt(...).render()
    raise NotImplementedError


def build_root_cause_prompt() -> str:
    """
    Task: Build a chain-of-thought prompt that asks an agent to reason step by
    step about why a service might be returning HTTP 503 responses. The agent
    should act as a senior backend engineer.
    """
    # TODO: create and return a Prompt(...).render()
    raise NotImplementedError


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
