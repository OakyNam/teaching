"""Reference solution for lesson 05: control flow."""


def describe_number(number: int) -> str:
    """Return whether the number is positive, negative, or zero."""
    if number > 0:
        return f"{number} is positive"
    if number < 0:
        return f"{number} is negative"
    return "0 is zero"


def login_message(username: str, password: str) -> str:
    """Return an access message when the credentials match admin and secret123."""
    return "Access granted!" if username == "admin" and password == "secret123" else "Access denied."


def letter_grade(score: int) -> str:
    """Return A, B, C, D, or F based on the score ranges from the lesson."""
    if score >= 90:
        return "A"
    if score >= 80:
        return "B"
    if score >= 70:
        return "C"
    if score >= 60:
        return "D"
    return "F"


def life_stage(age: int) -> str:
    """Return Child, Teenager, Adult, or Senior based on the provided age."""
    if age < 13:
        return "Child"
    if age <= 17:
        return "Teenager"
    if age <= 64:
        return "Adult"
    return "Senior"


def guess_feedback(secret: int, guess: int) -> str:
    """Return Too low!, Too high!, or Correct! for the guessed number."""
    if guess < secret:
        return "Too low!"
    if guess > secret:
        return "Too high!"
    return "Correct!"


def run() -> None:
    print(describe_number(-3))
    print(login_message("admin", "secret123"))
    print(letter_grade(88))
    print(life_stage(70))
    print(guess_feedback(42, 50))


if __name__ == "__main__":
    run()
