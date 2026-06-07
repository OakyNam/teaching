"""Reference solution for error handling and custom exceptions."""
from __future__ import annotations


class ReservationError(Exception):
    """Raised when reservation details cannot be processed."""



def parse_party_size(value: str) -> int:
    if not value.isdigit():
        raise ReservationError("Party size must be numeric.")
    size = int(value)
    if not 1 <= size <= 12:
        raise ReservationError("Party size must be between 1 and 12.")
    return size



def build_reservation(name: str, party_size_text: str) -> dict[str, int | str]:
    try:
        size = parse_party_size(party_size_text)
    except ReservationError as exc:
        raise ReservationError(f"Reservation for {name} is invalid.") from exc
    return {"name": name, "party_size": size}



def save_confirmation(reservation: dict[str, int | str]) -> str:
    try:
        return (
            f"Saved reservation for {reservation['name']} "
            f"({reservation['party_size']} guests)"
        )
    finally:
        print("Reservation save attempt finished.")



def run() -> None:
    for name, size_text in [("Jordan", "4"), ("Taylor", "many")]:
        try:
            reservation = build_reservation(name, size_text)
            print(save_confirmation(reservation))
        except ReservationError as exc:
            print(f"Could not save reservation: {exc}")
        print()


if __name__ == "__main__":
    run()
