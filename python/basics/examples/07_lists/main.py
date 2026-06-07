"""Runnable example for lesson 07: lists."""


def main() -> None:
    groceries = ["milk", "bread", "eggs", "coffee"]
    prices = [4.50, 2.25, 3.99, 8.75]

    print("Original shopping list:", groceries)
    print("First item:", groceries[0])
    print("Last two items:", groceries[-2:])
    print("Every other price:", prices[::2])

    groceries.append("bananas")
    groceries.remove("bread")
    groceries.sort()
    print("\nUpdated shopping list:", groceries)

    highest_price = max(prices)
    cheapest_price = min(prices)
    print(f"Most expensive item costs ${highest_price:.2f}.")
    print(f"Cheapest item costs ${cheapest_price:.2f}.")

    print("\nLooping with enumerate():")
    for index, item in enumerate(groceries, start=1):
        print(f"{index}. {item}")

    discounted_prices = [round(price * 0.9, 2) for price in prices]
    print("\nDiscounted prices:", discounted_prices)


if __name__ == "__main__":
    main()
