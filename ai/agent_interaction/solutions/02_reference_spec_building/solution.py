"""
Solution 02 - Reference Spec Building
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
    return ReferenceSpec(
        problem_statement=(
            "We need a Python script that reads ECS task CPU and memory metrics "
            "from CloudWatch and writes a CSV report to stdout covering the last 24 hours."
        ),
        in_scope=["CloudWatch GetMetricStatistics API calls", "CSV output to stdout"],
        out_of_scope=["IAM policy changes", "writing output to S3 or a file"],
        constraints=[
            "Python 3.11+",
            "boto3 only — no additional third-party libraries",
            "No IAM changes required to run the script",
        ],
        context=[
            "ECS cluster name is available in the environment variable ECS_CLUSTER.",
            "Region defaults to us-east-1 unless ECS_REGION is set.",
            "Existing boto3 patterns follow cloud/aws/rds/examples/01_connect_and_query/main.py.",
        ],
        acceptance_criteria=[
            "Script writes a CSV header row followed by one data row per ECS task.",
            "CSV columns are: task_id, cpu_utilization_percent, memory_utilization_percent.",
            "Script covers exactly the last 24 hours of metrics.",
            "Script exits 0 on success and 1 with an error message on failure.",
            "Region is configurable via ECS_REGION, defaulting to us-east-1.",
        ],
        output_format="A single Python file named ecs_report.py with inline comments.",
    )


def main() -> None:
    spec = build_spec()
    print(spec.render())


if __name__ == "__main__":
    main()
