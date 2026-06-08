"""Runnable example for lesson 09: functions."""


def greet(name: str, greeting: str = "Hello") -> str:
    return f"{greeting}, {name}!"


def add_prices(*prices: float) -> float:
    return sum(prices)


def describe_order(**details: object) -> str:
    customer = details.get("customer", "Unknown")
    item_count = details.get("item_count", 0)
    return f"{customer} placed an order with {item_count} items."


def main() -> None:
    print(greet("Nina"))
    print(greet("Marco", "Welcome"))

    subtotal = add_prices(12.50, 8.25, 4.75)
    print(f"Subtotal: ${subtotal:.2f}")

    width = 5
    height = 3
    area = width * height
    print(f"Rectangle area: {area}")

    print(describe_order(customer="Nina", item_count=3))

    def square(number: int) -> int:
        return number * number

    print(f"Square of 6: {square(6)}")


if __name__ == "__main__":
    main()
