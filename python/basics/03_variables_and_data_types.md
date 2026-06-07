# 03 – Variables and Data Types

## Overview

A **variable** is a named container that stores a value. You can think of it as a labeled box 📦.

```python
name = "Alice"   # the box is labeled "name" and holds "Alice"
age = 25         # the box is labeled "age" and holds 25
```

---

## 📝 Creating Variables

In Python, you create a variable by writing a name, an `=` sign, and a value:

```python
city = "New York"
temperature = 72
is_sunny = True
```

No need to declare a type — Python figures it out automatically!

### Variable naming rules
- Use letters, numbers, and underscores: `my_variable`, `score1`
- Cannot start with a number: ❌ `1score`
- No spaces — use underscores instead: ✅ `first_name` ❌ `first name`
- Case-sensitive: `Name` and `name` are different variables

---

## 🔢 The Four Basic Data Types

### 1. `str` – String (text)

Strings are wrapped in single or double quotes:

```python
greeting = "Hello, World!"
language = 'Python'
sentence = "I'm learning Python!"  # single quote inside double quotes — no problem
```

### 2. `int` – Integer (whole number)

```python
apples = 5
year = 2024
negative = -10
```

### 3. `float` – Decimal number

```python
price = 9.99
pi = 3.14159
temperature = -2.5
```

### 4. `bool` – Boolean (True or False)

```python
is_logged_in = True
has_permission = False
```

> ⚠️ `True` and `False` must be capitalized in Python!

---

## 🔍 Checking the Type of a Variable

Use the built-in `type()` function:

```python
x = 42
print(type(x))    # <class 'int'>

y = "hello"
print(type(y))    # <class 'str'>

z = 3.14
print(type(z))    # <class 'float'>
```

---

## 🔄 Changing a Variable's Value

Variables can be reassigned at any time:

```python
score = 0
print(score)   # 0

score = 10
print(score)   # 10

score = score + 5
print(score)   # 15
```

---

## 🔗 String Operations

You can combine strings using `+` (called **concatenation**):

```python
first = "John"
last = "Doe"
full_name = first + " " + last
print(full_name)   # John Doe
```

You can also use **f-strings** (recommended — cleaner!):

```python
name = "Alice"
age = 30
message = f"My name is {name} and I am {age} years old."
print(message)   # My name is Alice and I am 30 years old.
```

---

## ➕ Basic Math with Numbers

```python
a = 10
b = 3

print(a + b)   # 13  (addition)
print(a - b)   # 7   (subtraction)
print(a * b)   # 30  (multiplication)
print(a / b)   # 3.333... (division — always returns float)
print(a // b)  # 3   (floor division — no remainder)
print(a % b)   # 1   (modulo — remainder only)
print(a ** b)  # 1000 (exponentiation — 10 to the power of 3)
```

---

## 🏋️ Exercises

Open your terminal, activate your `.venv`, and create a file called `variables.py`.

**Exercise 1:** Create variables for your name, age, and favorite number. Print each one.

```python
# Write your code here
name = ___
age = ___
favorite_number = ___
print(name)
print(age)
print(favorite_number)
```

**Exercise 2:** Use an f-string to print a sentence like:
`"My name is Alice, I am 25 years old, and my favorite number is 7."`

**Exercise 3:** Create two number variables and print the result of all 7 math operations (`+`, `-`, `*`, `/`, `//`, `%`, `**`).

**Exercise 4:** What does `type("hello")` return? What about `type(3.14)`? Try it in your Python file using `print(type(...))`.

**Exercise 5 (Challenge):** Can you store the result of a math operation in a variable and then use it in an f-string?
```python
length = 5
width = 3
area = ___       # calculate the area
print(f"The area is {area}")
```

Run your file with:
- Mac: `python3 variables.py`
- Windows: `python variables.py`

---

⬅️ **Previous:** [02 – Virtual Environments](./02_virtual_environments.md)
➡️ **Next:** [04 – User Input and Print](./04_user_input_and_print.md)

---

## Answer Key

**Exercise 1 (example):**
```python
name = "Alice"
age = 25
favorite_number = 7
print(name)
print(age)
print(favorite_number)
```

**Exercise 2 (example):**
```python
print(f"My name is {name}, I am {age} years old, and my favorite number is {favorite_number}.")
```

**Exercise 3 (example):**
```python
a = 10
b = 3
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(a ** b)
```

**Exercise 4:**
```python
print(type("hello"))  # <class 'str'>
print(type(3.14))     # <class 'float'>
```

**Exercise 5:**
```python
length = 5
width = 3
area = length * width
print(f"The area is {area}")
```

