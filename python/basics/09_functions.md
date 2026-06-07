# 09 – Functions

## Overview

A **function** is a reusable block of code with a name. Instead of writing the same
code multiple times, you write it once in a function and **call** it whenever you need it.

```python
def greet():
    print("Hello, World!")

greet()   # calling the function → prints "Hello, World!"
greet()   # call it again!
```

---

## 📐 Defining a Function

```python
def function_name():
    # code here
    # indented 4 spaces
```

- `def` keyword tells Python you're defining a function
- The name follows the same rules as variable names
- The colon `:` ends the `def` line
- The body is indented

---

## 📨 Parameters and Arguments

**Parameters** are variables listed in the function definition.
**Arguments** are the actual values you pass when calling the function.

```python
def greet(name):           # 'name' is a parameter
    print(f"Hello, {name}!")

greet("Alice")             # 'Alice' is the argument → Hello, Alice!
greet("Bob")               # → Hello, Bob!
```

### Multiple parameters

```python
def add(a, b):
    print(a + b)

add(3, 5)    # 8
add(10, 20)  # 30
```

---

## 🔙 Returning Values

Use `return` to send a value back to the caller:

```python
def add(a, b):
    return a + b

result = add(3, 5)
print(result)    # 8
```

Without `return`, the function returns `None` by default.

### Return multiple values

```python
def min_max(numbers):
    return min(numbers), max(numbers)

low, high = min_max([3, 1, 7, 2, 9])
print(low, high)   # 1 9
```

---

## 🎛️ Default Parameters

Give parameters a default value — used if no argument is passed:

```python
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

greet("Alice")             # Hello, Alice!
greet("Bob", "Hi")         # Hi, Bob!
greet("Charlie", "Hey")    # Hey, Charlie!
```

> ⚠️ Parameters with defaults must come **after** parameters without defaults.

---

## 🏷️ Keyword Arguments

Pass arguments by name — order doesn't matter:

```python
def describe(name, age, city):
    print(f"{name} is {age} years old from {city}")

describe(age=25, city="Paris", name="Alice")   # any order!
```

---

## 🔭 Variable Scope

Variables created **inside** a function only exist inside that function:

```python
def my_function():
    x = 10    # local variable
    print(x)

my_function()   # 10
print(x)        # ❌ Error! x doesn't exist outside the function
```

Variables defined **outside** all functions are **global**:

```python
name = "Alice"   # global variable

def greet():
    print(f"Hello, {name}")   # can READ global variables

greet()   # Hello, Alice
```

---

## 📦 Functions as Building Blocks

Break big problems into small functions:

```python
def get_circle_area(radius):
    return 3.14159 * radius ** 2

def get_cylinder_volume(radius, height):
    base_area = get_circle_area(radius)   # call another function!
    return base_area * height

volume = get_cylinder_volume(5, 10)
print(f"Volume: {volume:.2f}")   # Volume: 785.40
```

---

## 🏋️ Exercises

Create a file called `functions.py`.

**Exercise 1:** Write a function called `square(n)` that returns the square of a number. Test it with a few values.

**Exercise 2:** Write a function called `is_even(n)` that returns `True` if a number is even, `False` if odd.

```python
print(is_even(4))   # True
print(is_even(7))   # False
```

**Exercise 3:** Write a function called `celsius_to_fahrenheit(c)` that converts a temperature. Then write another called `fahrenheit_to_celsius(f)`. Test both.

**Exercise 4:** Write a function called `calculate_tip(bill_amount, tip_percent=15)`:
- Default tip is 15%
- Return the tip amount (not the total)

```python
print(calculate_tip(50))        # 7.5  (15% of 50)
print(calculate_tip(80, 20))    # 16.0 (20% of 80)
```

**Exercise 5:** Write a function called `count_vowels(text)` that counts and returns the number of vowels in a string (a, e, i, o, u — uppercase and lowercase).

```python
print(count_vowels("Hello World"))   # 3
print(count_vowels("Python"))        # 1
```

**Exercise 6 (Challenge):** Write a function `fizzbuzz(n)` that:
- Returns `"Fizz"` if n is divisible by 3
- Returns `"Buzz"` if n is divisible by 5
- Returns `"FizzBuzz"` if divisible by both
- Returns the number as a string otherwise

Then write a loop that calls it for 1 to 30 and prints the results.

---

⬅️ **Previous:** [08 – Dictionaries](./08_dictionaries.md)
➡️ **Next:** [10 – Modules and Packages](./10_modules_and_packages.md)

---

## Answer Key

**Exercise 1:**
```python
def square(n):
    return n ** 2

print(square(2))
print(square(5))
print(square(-3))
```

**Exercise 2:**
```python
def is_even(n):
    return n % 2 == 0

print(is_even(4))
print(is_even(7))
```

**Exercise 3:**
```python
def celsius_to_fahrenheit(c):
    return (c * 9 / 5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5 / 9

print(celsius_to_fahrenheit(100))
print(fahrenheit_to_celsius(212))
```

**Exercise 4:**
```python
def calculate_tip(bill_amount, tip_percent=15):
    return bill_amount * (tip_percent / 100)

print(calculate_tip(50))
print(calculate_tip(80, 20))
```

**Exercise 5:**
```python
def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0
    for ch in text:
        if ch in vowels:
            count += 1
    return count

print(count_vowels("Hello World"))
print(count_vowels("Python"))
```

**Exercise 6:**
```python
def fizzbuzz(n):
    if n % 3 == 0 and n % 5 == 0:
        return "FizzBuzz"
    if n % 3 == 0:
        return "Fizz"
    if n % 5 == 0:
        return "Buzz"
    return str(n)

for i in range(1, 31):
    print(fizzbuzz(i))
```

