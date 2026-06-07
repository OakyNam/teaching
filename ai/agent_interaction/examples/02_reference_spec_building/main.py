"""
Example: Reference spec builder.

Demonstrates constructing a structured reference spec document that can be
passed to an AI agent as context before asking it to execute a task.
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


def build_connection_monitor_spec() -> ReferenceSpec:
    return ReferenceSpec(
        problem_statement=(
            "The RDS connection pool is exhausted during peak hours. "
            "We need a script that monitors active connections and pages the on-call "
            "engineer when usage exceeds a configurable threshold."
        ),
        in_scope=["read-only CloudWatch metrics query", "SNS notification"],
        out_of_scope=["modifying RDS configuration", "restarting connections"],
        constraints=[
            "Python 3.11+",
            "No new third-party libraries beyond boto3",
            "Threshold must be configurable via an environment variable",
        ],
        context=[
            'Database credentials are in AWS Secrets Manager under "teaching/rds".',
            "SNS topic ARN is in the environment variable ALERT_TOPIC_ARN.",
            "Existing scripts follow the pattern in cloud/aws/rds/examples/01_connect_and_query/main.py.",
        ],
        acceptance_criteria=[
            "Script exits 0 when connection usage is below threshold.",
            "Script sends an SNS message and exits 1 when threshold is exceeded.",
            "Threshold defaults to 80 when the environment variable is not set.",
            "Script logs its actions at INFO level using the standard logging module.",
        ],
        output_format="A single Python file named monitor_connections.py with inline comments.",
    )


def main() -> None:
    spec = build_connection_monitor_spec()
    print(spec.render())


if __name__ == "__main__":
    main()
