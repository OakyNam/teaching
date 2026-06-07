# 04 – User Input and Print

## Overview

So far we've been hard-coding values. Now let's make programs that **talk to the user**!

---

## 🖨️ The `print()` Function

`print()` displays output in the terminal. You've already seen it — let's go deeper.

```python
print("Hello!")                    # Hello!
print("The answer is", 42)         # The answer is 42
print("Pi is approximately", 3.14) # Pi is approximately 3.14
```

### Printing multiple values

`print()` can take multiple arguments separated by commas:

```python
name = "Alice"
age = 25
print("Name:", name, "| Age:", age)   # Name: Alice | Age: 25
```

### Controlling the separator

By default, `print()` puts a space between items. Change it with `sep=`:

```python
print("2024", "06", "15", sep="-")   # 2024-06-15
print("a", "b", "c", sep=", ")       # a, b, c
```

### Controlling the end character

By default, `print()` adds a newline at the end. Change it with `end=`:

```python
print("Loading", end="")
print("...")   # prints on the same line: Loading...
```

---

## ⌨️ The `input()` Function

`input()` pauses the program and waits for the user to type something and press Enter.
It always returns a **string**.

```python
name = input("What is your name? ")
print("Hello,", name)
```

When you run this:
```
What is your name? Alice
Hello, Alice
```

### Always converts to string

```python
age = input("How old are you? ")
print(type(age))   # <class 'str'> — it's a string, not a number!
```

---

## 🔄 Converting Input to a Number

Since `input()` returns a string, you need to **convert** it if you want to do math.

Use `int()` to convert to an integer, or `float()` for decimals:

```python
age = int(input("How old are you? "))
print(age + 1)   # Works! Adds 1 to the number
```

```python
price = float(input("Enter price: "))
tax = price * 0.08
print(f"With tax: {price + tax:.2f}")   # :.2f rounds to 2 decimal places
```

> ⚠️ If the user types something that's not a number and you use `int()`, Python will crash with an error. We'll learn how to handle this later!

---

## 🛠️ Useful String Methods

Strings have built-in methods you can call:

```python
name = "  alice  "

print(name.strip())        # "alice"     — removes leading/trailing spaces
print(name.strip().upper()) # "ALICE"    — converts to uppercase
print(name.strip().lower()) # "alice"    — converts to lowercase
print(name.strip().title()) # "Alice"    — capitalizes first letter
```

Check length with `len()`:

```python
word = "Python"
print(len(word))   # 6
```

---

## 📐 Formatting Numbers in Print

Use f-strings to format numbers nicely:

```python
pi = 3.14159265
print(f"Pi is {pi:.2f}")     # Pi is 3.14      (2 decimal places)
print(f"Pi is {pi:.4f}")     # Pi is 3.1416    (4 decimal places)

big_number = 1000000
print(f"Big: {big_number:,}")  # Big: 1,000,000 (comma separator)
```

---

## 🏋️ Exercises

Create a file called `input_output.py` in your project folder.

**Exercise 1:** Write a program that asks for the user's name and greets them:
```
What is your name? Bob
Hello, Bob! Welcome to Python!
```

**Exercise 2:** Write a program that asks for two numbers and prints their sum:
```
Enter first number: 10
Enter second number: 5
The sum of 10 and 5 is 15
```
> 💡 Remember to convert the input with `int()`!

**Exercise 3:** Write a program that asks for a temperature in Celsius and converts it to Fahrenheit.
Formula: `F = (C × 9/5) + 32`
```
Enter temperature in Celsius: 100
100°C is equal to 212.0°F
```

**Exercise 4:** Write a program that asks for a word and prints:
- The word in ALL CAPS
- The length of the word
- The word reversed (hint: `word[::-1]`)

**Exercise 5 (Challenge):** Ask the user for their first name and last name separately, then print:
```
Full name: John Doe
Initials: J.D.
```

---

⬅️ **Previous:** [03 – Variables and Data Types](./03_variables_and_data_types.md)
➡️ **Next:** [05 – Control Flow (if/elif/else)](./05_control_flow.md)

---

## Answer Key

**Exercise 1 (example):**
```python
name = input("What is your name? ")
print(f"Hello, {name}! Welcome to Python!")
```

**Exercise 2 (example):**
```python
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print(f"The sum of {a} and {b} is {a + b}")
```

**Exercise 3 (example):**
```python
c = float(input("Enter temperature in Celsius: "))
f = (c * 9 / 5) + 32
print(f"{c}C is equal to {f}F")
```

**Exercise 4 (example):**
```python
word = input("Enter a word: ")
print(word.upper())
print(len(word))
print(word[::-1])
```

**Exercise 5 (example):**
```python
first = input("First name: ").strip().title()
last = input("Last name: ").strip().title()
print(f"Full name: {first} {last}")
print(f"Initials: {first[0]}.{last[0]}.")
```

