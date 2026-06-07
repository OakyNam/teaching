"""Demonstrate dataclasses, default factories, and useful type hints."""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, List, Optional


@dataclass
class Project:
    name: str
    owner: Optional[str]
    team: List[str] = field(default_factory=list)
    hours_by_member: Dict[str, int] = field(default_factory=dict)

    def add_member(self, member: str) -> None:
        if member not in self.team:
            self.team.append(member)
            self.hours_by_member.setdefault(member, 0)

    def log_hours(self, member: str, hours: int) -> None:
        self.hours_by_member[member] = self.hours_by_member.get(member, 0) + hours

    def summary(self) -> str:
        owner_name = self.owner or "unassigned"
        total_hours = sum(self.hours_by_member.values())
        return f"{self.name} owned by {owner_name}: {total_hours} hours logged"



def main() -> None:
    project = Project(name="Student Portal Refresh", owner=None)
    project.add_member("Kai")
    project.add_member("Lina")
    project.log_hours("Kai", 5)
    project.log_hours("Lina", 3)

    print(project)
    print(project.summary())
    print(project.hours_by_member)


if __name__ == "__main__":
    main()
