# 06 – Loops

## Overview

Loops let you **repeat code** without writing it over and over.
Instead of printing "Hello" 100 times manually, a loop does it for you!

---

## 🔁 The `for` Loop

A `for` loop repeats a block of code **for each item** in a sequence.

```python
for i in range(5):
    print(i)
```

Output:
```
0
1
2
3
4
```

### `range()` explained

`range()` generates a sequence of numbers:

```python
range(5)        # 0, 1, 2, 3, 4        (start=0, stop=5)
range(2, 6)     # 2, 3, 4, 5           (start=2, stop=6)
range(0, 10, 2) # 0, 2, 4, 6, 8        (start=0, stop=10, step=2)
range(5, 0, -1) # 5, 4, 3, 2, 1        (counting backwards)
```

> ⚠️ The **stop** value is never included!

### Looping over a string

```python
for letter in "Python":
    print(letter)
```

Output:
```
P
y
t
h
o
n
```

---

## 🔄 The `while` Loop

A `while` loop keeps running **as long as a condition is True**:

```python
count = 1

while count <= 5:
    print(count)
    count += 1   # count = count + 1
```

Output:
```
1
2
3
4
5
```

> ⚠️ Always make sure the condition eventually becomes `False`, or you'll create an **infinite loop** that never stops! Press `Ctrl + C` to stop a runaway program.

---

## ⏭️ `break` and `continue`

### `break` – exit the loop immediately

```python
for i in range(10):
    if i == 5:
        break
    print(i)
# prints 0, 1, 2, 3, 4 — stops when i is 5
```

### `continue` – skip to the next iteration

```python
for i in range(10):
    if i % 2 == 0:
        continue   # skip even numbers
    print(i)
# prints 1, 3, 5, 7, 9
```

---

## 🔁 Nested Loops

A loop inside another loop:

```python
for row in range(1, 4):
    for col in range(1, 4):
        print(f"({row},{col})", end=" ")
    print()   # new line after each row
```

Output:
```
(1,1) (1,2) (1,3)
(2,1) (2,2) (2,3)
(3,1) (3,2) (3,3)
```

---

## 🧮 Accumulating Values in a Loop

A common pattern — start with a variable and build it up each iteration:

```python
# Sum of 1 to 10
total = 0
for i in range(1, 11):
    total += i   # same as: total = total + i

print(total)   # 55
```

---

## 🏋️ Exercises

Create a file called `loops.py`.

**Exercise 1:** Use a `for` loop to print all numbers from 1 to 20.

**Exercise 2:** Use a `for` loop with `range()` to print all even numbers between 1 and 30.

**Exercise 3:** Write a loop that calculates and prints the multiplication table for a number the user enters:
```
Enter a number: 5
5 x 1 = 5
5 x 2 = 10
...
5 x 10 = 50
```

**Exercise 4:** Use a `while` loop to create a simple countdown:
```
Enter countdown start: 5
5...
4...
3...
2...
1...
Blast off! 🚀
```

**Exercise 5:** Write a number guessing game using a `while` loop. The secret number is 42. Keep asking the user to guess until they get it right:
```
Guess the number: 10   → Too low!
Guess the number: 70   → Too high!
Guess the number: 42   → Correct! You got it in 3 tries!
```
> 💡 Use a counter variable to track the number of attempts.

**Exercise 6 (Challenge):** Print this pattern using nested loops:
```
*
**
***
****
*****
```

---

⬅️ **Previous:** [05 – Control Flow](./05_control_flow.md)
➡️ **Next:** [07 – Lists](./07_lists.md)

---

## Answer Key

**Exercise 1:**
```python
for i in range(1, 21):
    print(i)
```

**Exercise 2:**
```python
for i in range(2, 31, 2):
    print(i)
```

**Exercise 3 (example):**
```python
n = int(input("Enter a number: "))
for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")
```

**Exercise 4 (example):**
```python
count = int(input("Enter countdown start: "))
while count > 0:
    print(f"{count}...")
    count -= 1
print("Blast off!")
```

**Exercise 5 (example):**
```python
secret = 42
tries = 0

while True:
    guess = int(input("Guess the number: "))
    tries += 1

    if guess < secret:
        print("Too low!")
    elif guess > secret:
        print("Too high!")
    else:
        print(f"Correct! You got it in {tries} tries!")
        break
```

**Exercise 6:**
```python
for row in range(1, 6):
    for col in range(row):
        print("*", end="")
    print()
```

