# 05 – Control Flow (if / elif / else)

## Overview

Programs need to make decisions. **Control flow** lets your code choose different paths
based on conditions — just like real life:

> "If it's raining, take an umbrella. Otherwise, wear sunglasses."

---

## 🔀 The `if` Statement

```python
temperature = 35

if temperature > 30:
    print("It's hot outside!")
```

If the condition is `True`, the indented block runs. If `False`, it's skipped.

> 📐 **Indentation matters in Python!** Use 4 spaces (or one tab) to indent. This is how Python knows which code belongs to the `if` block.

---

## 🔀 `if` / `else`

Add an `else` block for what happens when the condition is `False`:

```python
age = 16

if age >= 18:
    print("You can vote!")
else:
    print("You're too young to vote.")
```

---

## 🔀 `if` / `elif` / `else`

Use `elif` (short for "else if") to check multiple conditions:

```python
score = 75

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")
```

Python checks each condition **top to bottom** and runs the first one that's `True`.
Once a match is found, the rest are skipped.

---

## ⚖️ Comparison Operators

These return `True` or `False`:

| Operator | Meaning               | Example       |
|----------|-----------------------|---------------|
| `==`     | Equal to              | `5 == 5` → True  |
| `!=`     | Not equal to          | `5 != 3` → True  |
| `>`      | Greater than          | `7 > 3` → True   |
| `<`      | Less than             | `2 < 8` → True   |
| `>=`     | Greater than or equal | `5 >= 5` → True  |
| `<=`     | Less than or equal    | `4 <= 6` → True  |

> ⚠️ Don't confuse `=` (assignment) with `==` (comparison)!
> `x = 5` sets x to 5. `x == 5` asks "is x equal to 5?"

---

## 🔗 Logical Operators

Combine multiple conditions:

### `and` – both must be True
```python
age = 25
has_id = True

if age >= 18 and has_id:
    print("You may enter.")
```

### `or` – at least one must be True
```python
day = "Saturday"

if day == "Saturday" or day == "Sunday":
    print("It's the weekend!")
```

### `not` – flips True to False and vice versa
```python
is_raining = False

if not is_raining:
    print("No umbrella needed.")
```

---

## 📦 Checking Membership with `in`

Use `in` to check if a value exists in a string (or list — more on that later!):

```python
email = "user@example.com"

if "@" in email:
    print("Valid email format")
else:
    print("Missing @ symbol")
```

---

## 🏋️ Exercises

Create a file called `control_flow.py`.

**Exercise 1:** Ask the user for a number. Print whether it is positive, negative, or zero.

```python
number = int(input("Enter a number: "))
# Your if/elif/else here
```

Expected outputs:
```
Enter a number: 7    → "7 is positive"
Enter a number: -3   → "-3 is negative"
Enter a number: 0    → "0 is zero"
```

**Exercise 2:** Write a simple login check. Ask for a username and password. If both match `"admin"` and `"secret123"`, print `"Access granted!"`. Otherwise print `"Access denied."`.

**Exercise 3:** Write a grade calculator. Ask for a score (0–100) and print the letter grade using this scale:
- 90–100 → A
- 80–89  → B
- 70–79  → C
- 60–69  → D
- Below 60 → F

**Exercise 4:** Ask the user for their age. Print one of these messages:
- Under 13: "Child"
- 13–17: "Teenager"
- 18–64: "Adult"
- 65 and above: "Senior"

**Exercise 5 (Challenge):** Write a number guessing game (without loops — just one guess):
```python
secret = 42
guess = int(input("Guess the number (1-100): "))

# Print "Too low!", "Too high!", or "Correct!" based on the guess
```

---

⬅️ **Previous:** [04 – User Input and Print](./04_user_input_and_print.md)
➡️ **Next:** [06 – Loops](./06_loops.md)

---

## Answer Key

**Exercise 1 (example):**
```python
number = int(input("Enter a number: "))

if number > 0:
    print(f"{number} is positive")
elif number < 0:
    print(f"{number} is negative")
else:
    print(f"{number} is zero")
```

**Exercise 2 (example):**
```python
username = input("Username: ")
password = input("Password: ")

if username == "admin" and password == "secret123":
    print("Access granted!")
else:
    print("Access denied.")
```

**Exercise 3 (example):**
```python
score = int(input("Enter score (0-100): "))

if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("F")
```

**Exercise 4 (example):**
```python
age = int(input("Enter your age: "))

if age < 13:
    print("Child")
elif age <= 17:
    print("Teenager")
elif age <= 64:
    print("Adult")
else:
    print("Senior")
```

**Exercise 5 (example):**
```python
secret = 42
guess = int(input("Guess the number (1-100): "))

if guess < secret:
    print("Too low!")
elif guess > secret:
    print("Too high!")
else:
    print("Correct!")
```

