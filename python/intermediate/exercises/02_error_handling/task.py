
"""Exercise starter for error handling.

Create a reservation workflow that validates input, uses a custom
exception, and guarantees cleanup with finally.
"""
from __future__ import annotations


class ReservationError(Exception):
    """Raised when reservation details cannot be processed."""



def parse_party_size(value: str) -> int:
    """Convert text to a party size and reject invalid values."""
    raise NotImplementedError("Your implementation here")



def build_reservation(name: str, party_size_text: str) -> dict[str, int | str]:
    """Return a reservation dictionary or re-raise a ReservationError."""
    raise NotImplementedError("Your implementation here")



def save_confirmation(reservation: dict[str, int | str]) -> str:
    """Pretend to save a reservation and return a confirmation message."""
    raise NotImplementedError("Your implementation here")



def run() -> None:
    print("Implement the reservation functions, then call them from run().")
    print("Example input: ('Jordan', '4') and ('Taylor', 'many')")


if __name__ == "__main__":
    run()
