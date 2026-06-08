"""Runnable example for lesson 05: control flow."""


def ticket_message(age: int) -> str:
    if age < 13:
        return "Child ticket"
    if age < 18:
        return "Teen ticket"
    return "Adult ticket"


def main() -> None:
    temperature = 78
    has_membership = True
    email = "sam@example.com"
    score = 88

    if temperature >= 80:
        print("Pack water for the walk.")
    elif temperature >= 60:
        print("A light jacket should be enough.")
    else:
        print("Bring a warm coat.")

    print(f"\nTicket decision: {ticket_message(16)}")
    print(f"Score {score} earns a {'B' if score >= 80 else 'C'}.")

    # Logical operators help combine several rules in one check.
    if 18 <= 35 and has_membership:
        print("Member discount approved.")

    if "@" in email and "." in email:
        print(f"{email} looks like a valid email address.")

    weekend = "Saturday"
    if weekend == "Saturday" or weekend == "Sunday":
        print("It is the weekend, so the store closes early.")


if __name__ == "__main__":
    main()
