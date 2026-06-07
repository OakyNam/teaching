
"""Reference solution for dataclasses and typing."""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, List, Optional


@dataclass
class SupportTicket:
    ticket_id: int
    title: str
    owner: Optional[str] = None
    tags: List[str] = field(default_factory=list)
    notes: Dict[str, str] = field(default_factory=dict)

    def assign_owner(self, owner: str) -> None:
        self.owner = owner

    def add_tag(self, tag: str) -> None:
        if tag not in self.tags:
            self.tags.append(tag)

    def add_note(self, author: str, note: str) -> None:
        self.notes[author] = note



def build_status_report(tickets: List[SupportTicket]) -> Dict[str, int]:
    report: Dict[str, int] = {}
    for ticket in tickets:
        owner = ticket.owner or "unassigned"
        report[owner] = report.get(owner, 0) + 1
    return report



def run() -> None:
    api_ticket = SupportTicket(ticket_id=101, title="API timeout")
    ui_ticket = SupportTicket(ticket_id=102, title="Dashboard typo")
    api_ticket.assign_owner("Nora")
    api_ticket.add_tag("backend")
    api_ticket.add_note("Nora", "Timeout happens after 30 seconds.")
    ui_ticket.add_tag("frontend")
    print(api_ticket)
    print(build_status_report([api_ticket, ui_ticket]))


if __name__ == "__main__":
    run()
