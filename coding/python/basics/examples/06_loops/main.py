"""Runnable example for lesson 06: loops."""


def main() -> None:
    print("For loop with range(1, 6):")
    for number in range(1, 6):
        print(number, end=" ")
    print("\n")

    print("While loop countdown:")
    countdown = 3
    while countdown > 0:
        print(f"{countdown}...")
        countdown -= 1
    print("Lift off!\n")

    print("break stops a loop as soon as the goal is reached:")
    for guess in [12, 28, 42, 50]:
        if guess == 42:
            print("Found the secret number.")
            break
        print(f"{guess} was not correct.")

    print("\ncontinue skips work you do not need:")
    for value in range(1, 8):
        if value % 2 == 0:
            continue
        print(f"Odd value: {value}")

    print("\nNested loops can build patterns:")
    for row in range(1, 5):
        print("*" * row)


if __name__ == "__main__":
    main()
