# 07 – Lists

## Overview

A **list** is an ordered collection of items. Think of it as a shopping list 🛒 —
it holds multiple values in a single variable.

```python
fruits = ["apple", "banana", "cherry"]
numbers = [1, 2, 3, 4, 5]
mixed = ["Alice", 30, True, 3.14]   # lists can hold different types!
```

---

## 📍 Accessing Items (Indexing)

Each item has a **position** called an **index**, starting from `0`:

```python
fruits = ["apple", "banana", "cherry"]
#           [0]       [1]       [2]

print(fruits[0])   # apple
print(fruits[1])   # banana
print(fruits[2])   # cherry
```

### Negative indexing (from the end)

```python
print(fruits[-1])   # cherry  (last item)
print(fruits[-2])   # banana  (second to last)
```

---

## ✂️ Slicing

Get a portion of a list:

```python
numbers = [10, 20, 30, 40, 50]

print(numbers[1:3])    # [20, 30]     (index 1 up to, not including, 3)
print(numbers[:3])     # [10, 20, 30] (from start to index 3)
print(numbers[2:])     # [30, 40, 50] (from index 2 to end)
print(numbers[::2])    # [10, 30, 50] (every 2nd item)
print(numbers[::-1])   # [50, 40, 30, 20, 10] (reversed!)
```

---

## 🔧 Modifying Lists

### Change an item
```python
fruits = ["apple", "banana", "cherry"]
fruits[1] = "blueberry"
print(fruits)   # ['apple', 'blueberry', 'cherry']
```

### Add items
```python
fruits.append("date")          # add to the end
fruits.insert(1, "avocado")    # insert at index 1
print(fruits)
```

### Remove items
```python
fruits.remove("apple")         # remove by value (first match)
popped = fruits.pop()          # remove and return the last item
popped = fruits.pop(0)         # remove and return item at index 0
del fruits[1]                  # delete item at index 1
```

### Clear all items
```python
fruits.clear()    # empties the list
```

---

## 📋 Useful List Methods and Functions

```python
numbers = [3, 1, 4, 1, 5, 9, 2, 6]

print(len(numbers))          # 8       — number of items
print(sum(numbers))          # 31      — total
print(min(numbers))          # 1       — smallest
print(max(numbers))          # 9       — largest
print(numbers.count(1))      # 2       — how many times 1 appears
print(numbers.index(5))      # 4       — index of first 5

numbers.sort()
print(numbers)               # [1, 1, 2, 3, 4, 5, 6, 9]  — sorted in place

numbers.reverse()
print(numbers)               # [9, 6, 5, 4, 3, 2, 1, 1]
```

---

## 🔁 Looping Over a List

```python
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)
```

### Loop with index using `enumerate()`

```python
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")
# 0: apple
# 1: banana
# 2: cherry
```

---

## 🔍 Checking Membership

```python
fruits = ["apple", "banana", "cherry"]

print("banana" in fruits)      # True
print("mango" in fruits)       # False
print("mango" not in fruits)   # True
```

---

## ⚡ List Comprehensions (Bonus)

A concise way to create lists:

```python
# Traditional way
squares = []
for i in range(1, 6):
    squares.append(i ** 2)

# List comprehension — one line!
squares = [i ** 2 for i in range(1, 6)]
print(squares)   # [1, 4, 9, 16, 25]
```

With a condition:
```python
evens = [i for i in range(20) if i % 2 == 0]
print(evens)   # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
```

---

## 🏋️ Exercises

Create a file called `lists.py`.

**Exercise 1:** Create a list of 5 of your favorite movies. Print the first, last, and middle movie.

**Exercise 2:** Start with this list: `numbers = [5, 2, 8, 1, 9, 3, 7, 4, 6]`
- Print the length of the list
- Print the sum, min, and max
- Sort the list and print it
- Print the list in reverse order

**Exercise 3:** Ask the user to enter 5 numbers one at a time. Store them in a list, then print:
- The list
- The average (sum / count)
- The largest and smallest numbers

**Exercise 4:** Write a program that removes all duplicate numbers from a list:
```python
numbers = [1, 2, 2, 3, 4, 4, 4, 5]
# Your code here — result should be [1, 2, 3, 4, 5]
```
> 💡 Hint: Try converting to a `set()` and back to a `list()`.

**Exercise 5 (Challenge):** Using a list comprehension, create a list of all numbers between 1 and 50 that are divisible by both 3 and 5. Print the result.

---

⬅️ **Previous:** [06 – Loops](./06_loops.md)
➡️ **Next:** [08 – Dictionaries](./08_dictionaries.md)

---

## Answer Key

**Exercise 1 (example):**
```python
movies = ["Inception", "Interstellar", "The Matrix", "Coco", "Arrival"]
print("First:", movies[0])
print("Middle:", movies[len(movies) // 2])
print("Last:", movies[-1])
```

**Exercise 2:**
```python
numbers = [5, 2, 8, 1, 9, 3, 7, 4, 6]
print(len(numbers))
print(sum(numbers), min(numbers), max(numbers))
numbers.sort()
print(numbers)
numbers.reverse()
print(numbers)
```

**Exercise 3 (example):**
```python
nums = []
for _ in range(5):
    nums.append(float(input("Enter a number: ")))

print(nums)
print("Average:", sum(nums) / len(nums))
print("Largest:", max(nums))
print("Smallest:", min(nums))
```

**Exercise 4:**
```python
numbers = [1, 2, 2, 3, 4, 4, 4, 5]
unique_numbers = list(set(numbers))
unique_numbers.sort()
print(unique_numbers)  # [1, 2, 3, 4, 5]
```

**Exercise 5:**
```python
result = [i for i in range(1, 51) if i % 3 == 0 and i % 5 == 0]
print(result)  # [15, 30, 45]
```

