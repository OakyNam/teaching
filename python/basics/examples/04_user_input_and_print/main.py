"""Runnable example for lesson 04: user input and print."""


def main() -> None:
    simulated_name = "  jordan  "
    simulated_age = "34"
    simulated_bill = "18.75"

    print("Pretend the user typed these answers:")
    print("What is your name?", simulated_name)
    print("How old are you?", simulated_age)
    print("What was the bill?", simulated_bill)

    clean_name = simulated_name.strip().title()
    next_age = int(simulated_age) + 1
    bill_total = float(simulated_bill)

    # f-strings make mixed text and values easy to read.
    print(f"\nHello, {clean_name}! Next year you will be {next_age}.")
    print(f"A bill of ${bill_total:.2f} with 8% tax becomes ${bill_total * 1.08:.2f}.")

    print("\nDifferent print styles:")
    print("Name:", clean_name, "| Age next year:", next_age)
    print("2024", "06", "15", sep="-")
    print("Loading", end="")
    print("...")
    print("Formatted with str.format(): {} ordered {} notebooks.".format(clean_name, 3))


if __name__ == "__main__":
    main()
