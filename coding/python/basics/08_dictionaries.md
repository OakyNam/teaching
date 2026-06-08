# 08 – Dictionaries

## Overview

A **dictionary** stores data as **key-value pairs** — like a real dictionary where
you look up a word (key) to find its definition (value).

```python
person = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}
```

Dictionaries are great when your data has **named fields** rather than a positional order.

---

## 📖 Accessing Values

Use the key in square brackets:

```python
print(person["name"])   # Alice
print(person["age"])    # 30
```

### Using `.get()` (safer)

If the key doesn't exist, `[]` raises an error. `.get()` returns `None` instead:

```python
print(person.get("email"))           # None — no error
print(person.get("email", "N/A"))    # N/A  — custom default
```

---

## ✏️ Adding and Updating

```python
person["email"] = "alice@example.com"   # add new key
person["age"] = 31                       # update existing key

print(person)
```

---

## 🗑️ Removing Items

```python
del person["city"]                  # delete a key
email = person.pop("email")         # remove and return the value
person.clear()                      # remove all items
```

---

## 🔑 Useful Dictionary Methods

```python
profile = {"name": "Bob", "age": 25, "job": "developer"}

print(profile.keys())     # dict_keys(['name', 'age', 'job'])
print(profile.values())   # dict_values(['Bob', 25, 'developer'])
print(profile.items())    # dict_items([('name', 'Bob'), ('age', 25), ...])

print(len(profile))       # 3
print("name" in profile)  # True — check if key exists
```

---

## 🔁 Looping Over Dictionaries

### Loop over keys (default)
```python
for key in profile:
    print(key)
```

### Loop over values
```python
for value in profile.values():
    print(value)
```

### Loop over key-value pairs (most common)
```python
for key, value in profile.items():
    print(f"{key}: {value}")
```

Output:
```
name: Bob
age: 25
job: developer
```

---

## 📦 Nested Dictionaries

Dictionaries can contain other dictionaries:

```python
users = {
    "alice": {
        "age": 30,
        "email": "alice@example.com"
    },
    "bob": {
        "age": 25,
        "email": "bob@example.com"
    }
}

print(users["alice"]["email"])   # alice@example.com
```

---

## 📋 List of Dictionaries

A very common pattern — a list where each item is a dictionary:

```python
students = [
    {"name": "Alice", "grade": 92},
    {"name": "Bob", "grade": 85},
    {"name": "Charlie", "grade": 78}
]

for student in students:
    print(f"{student['name']}: {student['grade']}")
```

---

## 🔄 Dictionary Comprehensions (Bonus)

Similar to list comprehensions:

```python
squares = {x: x**2 for x in range(1, 6)}
print(squares)   # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
```

---

## 🏋️ Exercises

Create a file called `dictionaries.py`.

**Exercise 1:** Create a dictionary for yourself with keys: `name`, `age`, `city`, `favorite_color`. Print each value using its key.

**Exercise 2:** Write a program that uses a dictionary as a simple phone book:
```python
contacts = {
    "Alice": "555-1234",
    "Bob": "555-5678",
    "Charlie": "555-9012"
}
```
Ask the user for a name, then look up and print their number. If not found, print `"Contact not found."` (use `.get()`).

**Exercise 3:** Count how many times each letter appears in a string using a dictionary:
```python
text = "hello world"
letter_count = {}
# Your code here
# Expected: {'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1}
```
> 💡 Hint: Use `.get(letter, 0) + 1`

**Exercise 4:** You have a list of students with grades:
```python
students = [
    {"name": "Alice", "grade": 92},
    {"name": "Bob", "grade": 74},
    {"name": "Charlie", "grade": 88},
    {"name": "Diana", "grade": 61},
]
```
Print only the students who passed (grade >= 70). Print their name and grade.

**Exercise 5 (Challenge):** Build a simple inventory system. Start with an empty dictionary. Allow the user to:
1. Add an item and quantity
2. View the full inventory
3. Quit

```
Menu: (a)dd | (v)iew | (q)uit
> a
Item name: apples
Quantity: 10
Added! 
> v
Inventory: {'apples': 10}
> q
Goodbye!
```

---

⬅️ **Previous:** [07 – Lists](./07_lists.md)
➡️ **Next:** [09 – Functions](./09_functions.md)

---

## Answer Key

**Exercise 1 (example):**
```python
me = {
    "name": "Alice",
    "age": 25,
    "city": "Cairo",
    "favorite_color": "blue",
}

print(me["name"])
print(me["age"])
print(me["city"])
print(me["favorite_color"])
```

**Exercise 2 (example):**
```python
contacts = {
    "Alice": "555-1234",
    "Bob": "555-5678",
    "Charlie": "555-9012",
}

name = input("Enter a name: ")
number = contacts.get(name)
if number:
    print(f"{name}: {number}")
else:
    print("Contact not found.")
```

**Exercise 3:**
```python
text = "hello world"
letter_count = {}

for letter in text:
    letter_count[letter] = letter_count.get(letter, 0) + 1

print(letter_count)
```

**Exercise 4:**
```python
students = [
    {"name": "Alice", "grade": 92},
    {"name": "Bob", "grade": 74},
    {"name": "Charlie", "grade": 88},
    {"name": "Diana", "grade": 61},
]

for student in students:
    if student["grade"] >= 70:
        print(f"{student['name']}: {student['grade']}")
```

**Exercise 5 (example):**
```python
inventory = {}

while True:
    choice = input("Menu: (a)dd | (v)iew | (q)uit\n> ").strip().lower()

    if choice == "a":
        item = input("Item name: ").strip().lower()
        qty = int(input("Quantity: "))
        inventory[item] = inventory.get(item, 0) + qty
        print("Added!")
    elif choice == "v":
        print("Inventory:", inventory)
    elif choice == "q":
        print("Goodbye!")
        break
    else:
        print("Invalid option.")
```

