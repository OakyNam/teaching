# 10 – Modules and Packages

## Overview

A **module** is a Python file containing reusable code (functions, variables, classes).
A **package** is a collection of modules. Python has thousands of packages available!

This is how Python scales — you don't have to write everything from scratch.

---

## 📦 Built-in Modules

Python comes with many useful modules. Use `import` to access them.

### `math` – mathematical functions

```python
import math

print(math.pi)           # 3.141592653589793
print(math.sqrt(25))     # 5.0
print(math.floor(3.7))   # 3
print(math.ceil(3.2))    # 4
print(math.pow(2, 8))    # 256.0
print(math.log(100, 10)) # 2.0
```

### `random` – random number generation

```python
import random

print(random.randint(1, 10))          # random integer between 1 and 10
print(random.random())                 # random float between 0.0 and 1.0
print(random.choice(["a", "b", "c"])) # random item from a list

numbers = [1, 2, 3, 4, 5]
random.shuffle(numbers)
print(numbers)                         # shuffled list
```

### `datetime` – dates and times

```python
from datetime import datetime, date

today = date.today()
print(today)                    # 2024-06-15

now = datetime.now()
print(now)                      # 2024-06-15 14:30:22.123456
print(now.strftime("%B %d, %Y")) # June 15, 2024
print(now.year, now.month, now.day)
```

### `os` – operating system interface

```python
import os

print(os.getcwd())           # current working directory
print(os.listdir("."))       # list files in current directory
print(os.path.exists("file.txt"))  # check if file exists
```

---

## 🎯 Import Styles

### Import the whole module

```python
import math
math.sqrt(16)   # must use module name as prefix
```

### Import specific items (no prefix needed)

```python
from math import sqrt, pi
sqrt(16)   # no prefix needed
print(pi)
```

### Import everything (not recommended)

```python
from math import *   # imports everything — can cause name conflicts
```

### Import with an alias

```python
import datetime as dt
print(dt.date.today())
```

---

## 📥 Installing Third-Party Packages with `pip`

The Python Package Index (PyPI) has over 500,000 packages!
Use `pip` to install them (make sure your `.venv` is activated first!).

```bash
pip install requests      # install
pip install requests==2.31.0  # install specific version
pip uninstall requests    # uninstall
pip list                  # see installed packages
pip show requests         # details about a package
```

### Popular packages to know

| Package | What it does |
|---------|-------------|
| `requests` | Make HTTP requests (fetch web data) |
| `pandas` | Data analysis and tables |
| `numpy` | Math and arrays |
| `flask` | Build web servers |
| `pillow` | Image processing |
| `pytest` | Testing your code |

---

## 🗂️ Creating Your Own Module

Any `.py` file is a module! Create `helpers.py`:

```python
# helpers.py

def greet(name):
    return f"Hello, {name}!"

def square(n):
    return n ** 2

PI = 3.14159
```

Then import it in `main.py` (same folder):

```python
# main.py
import helpers

print(helpers.greet("Alice"))   # Hello, Alice!
print(helpers.square(5))        # 25
print(helpers.PI)               # 3.14159
```

Or import specific items:
```python
from helpers import greet, square
print(greet("Bob"))
```

---

## 🧪 The `if __name__ == "__main__":` Pattern

When a Python file is run directly, `__name__` equals `"__main__"`.
When it's imported as a module, `__name__` equals the file name.

This pattern lets a file work both as a script and as a module:

```python
# helpers.py

def greet(name):
    return f"Hello, {name}!"

if __name__ == "__main__":
    # This only runs when you run helpers.py directly
    # It does NOT run when you import helpers
    print(greet("World"))
```

---

## 🏋️ Exercises

**Exercise 1:** Using the `random` module, write a program that simulates rolling a 6-sided die 10 times. Count and print how many times each number (1–6) appeared.

**Exercise 2:** Using the `math` module, write a function `hypotenuse(a, b)` that calculates the hypotenuse of a right triangle using the Pythagorean theorem: `c = sqrt(a² + b²)`.

**Exercise 3:** Using the `datetime` module, write a program that:
- Prints today's date in the format `"Today is Monday, June 15, 2024"`
- Asks the user for their birth year and prints how old they are

**Exercise 4:** Create your own module called `calculator.py` with functions:
- `add(a, b)`
- `subtract(a, b)`
- `multiply(a, b)`
- `divide(a, b)` — handle division by zero gracefully

Then create `main.py` that imports and uses all four functions.

**Exercise 5:** Install the `requests` package with pip (activate your `.venv` first!):
```bash
pip install requests
```
Then write a program that fetches data from a public API:
```python
import requests

response = requests.get("https://api.github.com")
print(response.status_code)   # 200 means success!
print(type(response.json()))  # <class 'dict'>
```

**Exercise 6 (Challenge):** Using the `random` and `math` modules, write a program that:
1. Generates 20 random numbers between 1 and 100
2. Stores them in a list
3. Calculates and prints: min, max, sum, average (rounded to 2 decimal places), and the square root of the average

---

## 🎉 What's Next?

Congratulations on completing the Python Basics series! 🎊

You've learned:
- ✅ Installing Python and setting up a virtual environment
- ✅ Variables, data types, and f-strings
- ✅ User input and print formatting
- ✅ Control flow with if/elif/else
- ✅ Loops (for and while)
- ✅ Lists and list comprehensions
- ✅ Dictionaries
- ✅ Functions and scope
- ✅ Modules and packages

### Suggested next topics:
- **File I/O** – reading and writing files
- **Error handling** – `try / except`
- **Classes and OOP** – object-oriented programming
- **Working with APIs** – fetching real data from the web
- **Frameworks** – Flask (web), Django (web), or Pandas (data science)

---

⬅️ **Previous:** [09 – Functions](./09_functions.md)

---

## Answer Key

**Exercise 1 (example):**
```python
import random

counts = {i: 0 for i in range(1, 7)}
for _ in range(10):
    roll = random.randint(1, 6)
    counts[roll] += 1

print(counts)
```

**Exercise 2:**
```python
import math

def hypotenuse(a, b):
    return math.sqrt(a ** 2 + b ** 2)

print(hypotenuse(3, 4))  # 5.0
```

**Exercise 3 (example):**
```python
from datetime import date

today = date.today()
print(today.strftime("Today is %A, %B %d, %Y"))

birth_year = int(input("Enter your birth year: "))
age = today.year - birth_year
print(f"You are about {age} years old.")
```

**Exercise 4:**
`calculator.py`
```python
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b
```

`main.py`
```python
import calculator

print(calculator.add(10, 5))
print(calculator.subtract(10, 5))
print(calculator.multiply(10, 5))
print(calculator.divide(10, 5))
```

**Exercise 5:**
```python
import requests

response = requests.get("https://api.github.com")
print(response.status_code)
print(type(response.json()))
```

**Exercise 6 (example):**
```python
import random
import math

nums = [random.randint(1, 100) for _ in range(20)]
avg = sum(nums) / len(nums)

print("Numbers:", nums)
print("Min:", min(nums))
print("Max:", max(nums))
print("Sum:", sum(nums))
print("Average:", round(avg, 2))
print("Sqrt of average:", round(math.sqrt(avg), 2))
```

