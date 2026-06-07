"""Exercise starter for dataclasses and typing.

Model a support ticket with a dataclass, optional owner information, and
collection fields created with field(default_factory=...).
"""
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
        """Store the name of the teammate handling the ticket."""
        raise NotImplementedError("Your implementation here")

    def add_tag(self, tag: str) -> None:
        """Add a tag when it is not already present."""
        raise NotImplementedError("Your implementation here")

    def add_note(self, author: str, note: str) -> None:
        """Save a note keyed by author name."""
        raise NotImplementedError("Your implementation here")



def build_status_report(tickets: List[SupportTicket]) -> Dict[str, int]:
    """Count tickets by owner, using 'unassigned' when owner is missing."""
    raise NotImplementedError("Your implementation here")



def run() -> None:
    ticket = SupportTicket(ticket_id=101, title="API timeout")
    print("Implement the methods above, then expand run() with sample tickets.")
    print(ticket)


if __name__ == "__main__":
    run()
