"""
Exercise 02 - Reference Spec Building

Fill in the ReferenceSpec below for the scenario described in the docstring.
Then call spec.render() and review the output for completeness.

A correct spec should have all five sections populated.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import List


@dataclass
class ReferenceSpec:
    problem_statement: str
    in_scope: List[str] = field(default_factory=list)
    out_of_scope: List[str] = field(default_factory=list)
    constraints: List[str] = field(default_factory=list)
    context: List[str] = field(default_factory=list)
    acceptance_criteria: List[str] = field(default_factory=list)
    output_format: str = ""

    def render(self) -> str:
        lines: List[str] = []
        lines.append("## Problem Statement")
        lines.append(self.problem_statement)
        lines.append("")
        if self.in_scope or self.out_of_scope or self.constraints:
            lines.append("## Scope and Constraints")
            if self.in_scope:
                lines.append("In scope: " + ", ".join(self.in_scope))
            if self.out_of_scope:
                lines.append("Out of scope: " + ", ".join(self.out_of_scope))
            for c in self.constraints:
                lines.append(f"- {c}")
            lines.append("")
        if self.context:
            lines.append("## Context")
            for item in self.context:
                lines.append(f"- {item}")
            lines.append("")
        if self.acceptance_criteria:
            lines.append("## Acceptance Criteria")
            for i, criterion in enumerate(self.acceptance_criteria, 1):
                lines.append(f"{i}. {criterion}")
            lines.append("")
        if self.output_format:
            lines.append("## Output Format")
            lines.append(self.output_format)
        return "\n".join(lines)


def build_spec() -> ReferenceSpec:
    """
    Scenario: You need an agent to write a Python script that reads ECS task
    CPU and memory metrics from CloudWatch and writes a CSV report to stdout.
    The script must use boto3, run with Python 3.11, and not require any IAM
    changes. It should cover the last 24 hours and default to the us-east-1
    region unless ECS_REGION is set. Output a single file named ecs_report.py.

    Fill in each field of ReferenceSpec to capture this scenario completely.
    """
    return ReferenceSpec(
        problem_statement="",  # TODO
        in_scope=[],           # TODO
        out_of_scope=[],       # TODO
        constraints=[],        # TODO
        context=[],            # TODO
        acceptance_criteria=[], # TODO
        output_format="",      # TODO
    )


def main() -> None:
    spec = build_spec()
    print(spec.render())


if __name__ == "__main__":
    main()
