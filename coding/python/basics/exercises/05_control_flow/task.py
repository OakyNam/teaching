"""Practice tasks for lesson 05: control flow."""

# Replace each NotImplementedError, then run this file to test the sample cases.


def describe_number(number: int) -> str:
    """Return whether the number is positive, negative, or zero."""
    raise NotImplementedError("Your implementation here")


def login_message(username: str, password: str) -> str:
    """Return an access message when the credentials match admin and secret123."""
    raise NotImplementedError("Your implementation here")


def letter_grade(score: int) -> str:
    """Return A, B, C, D, or F based on the score ranges from the lesson."""
    raise NotImplementedError("Your implementation here")


def life_stage(age: int) -> str:
    """Return Child, Teenager, Adult, or Senior based on the provided age."""
    raise NotImplementedError("Your implementation here")


def guess_feedback(secret: int, guess: int) -> str:
    """Return Too low!, Too high!, or Correct! for the guessed number."""
    raise NotImplementedError("Your implementation here")


def run() -> None:
    samples = [
        ("describe_number", lambda: describe_number(-3)),
        ("login_message", lambda: login_message("admin", "secret123")),
        ("letter_grade", lambda: letter_grade(88)),
        ("life_stage", lambda: life_stage(70)),
        ("guess_feedback", lambda: guess_feedback(42, 50)),
    ]
    for name, task in samples:
        try:
            print(f"{name}: {task()}")
        except NotImplementedError as error:
            print(f"{name}: {error}")


if __name__ == "__main__":
    run()
