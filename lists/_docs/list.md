# Lists in Python

## Introduction

Lists are ordered collections that can store multiple values in a single variable. They are one of the most versatile
and commonly used data structures in Python.

**Why use lists?**

| Benefit              | Description                                                |
|----------------------|------------------------------------------------------------|
| Group related values | Store multiple related values in a single variable         |
| Maintain order       | Elements keep their position and can be accessed by index  |
| Dynamic sizing       | Automatically grow or shrink as elements are added/removed |
| Efficient access     | Access any element by index in constant time               |
| Versatile storage    | Can store any data type (though typically homogeneous)     |

```python
# Instead of this:
score1 = 85
score2 = 92
score3 = 78

# Use this:
scores = [85, 92, 78]
```

## Creating Lists

| Method                | Syntax                                    | Example                                | Result                |
|-----------------------|-------------------------------------------|----------------------------------------|-----------------------|
| Empty list (literal)  | `[]`                                      | `empty = []`                           | `[]`                  |
| Empty list (function) | `list()`                                  | `empty = list()`                       | `[]`                  |
| With values           | `[val1, val2, ...]`                       | `numbers = [1, 2, 3, 4, 5]`            | `[1, 2, 3, 4, 5]`     |
| From range            | `list(range(...))`                        | `list(range(5))`                       | `[0, 1, 2, 3, 4]`     |
| From range (step)     | `list(range(start, stop, step))`          | `list(range(0, 11, 2))`                | `[0, 2, 4, 6, 8, 10]` |
| List comprehension    | `[expr for var in iterable]`              | `[x ** 2 for x in range(5)]`           | `[0, 1, 4, 9, 16]`    |
| With condition        | `[expr for var in iterable if condition]` | `[x for x in range(10) if x % 2 == 0]` | `[0, 2, 4, 6, 8]`     |
| Nested (2D)           | `[[...], [...]]`                          | `[[1, 2], [3, 4]]`                     | `[[1, 2], [3, 4]]`    |
| Repeat elements       | `[value] * n`                             | `[0] * 5`                              | `[0, 0, 0, 0, 0]`     |
| From string           | `list(string)`                            | `list("abc")`                          | `['a', 'b', 'c']`     |
| Split string          | `string.split()`                          | `"1 2 3".split()`                      | `['1', '2', '3']`     |

### Examples

```python
# Numbers
numbers = [1, 2, 3, 4, 5]
prices = [19.99, 24.50, 15.75]

# Strings
names = ["Alice", "Bob", "Charlie"]
colors = ['red', 'green', 'blue']

# From range
evens = list(range(0, 11, 2))  # [0, 2, 4, 6, 8, 10]
countdown = list(range(10, 0, -1))  # [10, 9, 8, ..., 1]

# List comprehensions
squares = [x ** 2 for x in range(10)]  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
filtered = [x for x in range(20) if x % 2 == 0]  # [0, 2, 4, ..., 18]

# Mixed types (possible but not recommended)
mixed = [1, "hello", 3.14, True]

# Nested lists (2D lists)
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
```

## Accessing Elements

### Indexing

Lists are zero-indexed (first element is at index 0):

```python
fruits = ["apple", "banana", "cherry", "date"]

print(fruits[0])  # "apple"  (first element)
print(fruits[1])  # "banana" (second element)
print(fruits[3])  # "date"   (fourth element)
# print(fruits[4]) # IndexError: list index out of range
```

> **Note: Why does indexing start at 0?**
>
> Zero-based indexing comes from how computers store lists in memory. The index represents the **offset** (distance) from
> the start of the list:
>
> - Index `0` means "0 steps from the start" → first element
> - Index `1` means "1 step from the start" → second element
> - Index `n` means "n steps from the start" → (n+1)th element
>
> This makes array address calculations simpler and more efficient at the hardware level. Many programming languages (C,
> Java, JavaScript, Python) use zero-based indexing for this reason. While it may seem confusing at first, you'll quickly
> get used to thinking: "the first element is at index 0."

### Negative Indexing

Access elements from the end using negative indices:

```python
fruits = ["apple", "banana", "cherry", "date"]

print(fruits[-1])  # "date"   (last element)
print(fruits[-2])  # "cherry" (second from end)
print(fruits[-4])  # "apple"  (fourth from end, same as fruits[0])
```

### Slicing

Extract sublists using `[start:stop:step]`:

| Syntax             | Example            | Result      |
|--------------------|--------------------|-------------|
| `list[start:stop]` | `[1,2,3,4,5][1:4]` | `[2, 3, 4]` |
| `list[start:]`     | `[1,2,3,4,5][2:]`  | `[3, 4, 5]` |
| `list[:stop]`      | `[1,2,3,4,5][:3]`  | `[1, 2, 3]` |
| `list[:]`          | `[1,2,3][:]`       | `[1, 2, 3]` |
| `list[::step]`     | `[1,2,3,4,5][::2]` | `[1, 3, 5]` |
| `list[::-1]`       | `[1,2,3][::-1]`    | `[3, 2, 1]` |

```python
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(numbers[2:7])  # [2, 3, 4, 5, 6]
print(numbers[:5])  # [0, 1, 2, 3, 4]
print(numbers[5:])  # [5, 6, 7, 8, 9]
print(numbers[::2])  # [0, 2, 4, 6, 8]
print(numbers[1::2])  # [1, 3, 5, 7, 9]
print(numbers[::-1])  # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
```

## List Operations

### Length

```python
fruits = ["apple", "banana", "cherry"]
print(len(fruits))  # 3

empty = []
print(len(empty))  # 0
```

### Concatenation

```python
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined = list1 + list2  # [1, 2, 3, 4, 5, 6]

# Original lists unchanged
print(list1)  # [1, 2, 3]
```

### Repetition

```python
zeros = [0] * 5  # [0, 0, 0, 0, 0]
pattern = [1, 2] * 3  # [1, 2, 1, 2, 1, 2]
```

> **Note: Avoid using list multiplication!**
>
> While `[0] * 5` might seem convenient, **it's best to avoid list multiplication entirely** as it can lead to subtle bugs,
> especially with nested lists or when the code is modified later.
>
> **The problem**:
> ```python
> # DANGEROUS - creates references to the SAME inner list!
> matrix = [[0] * 3] * 3  # All rows point to the same list
> matrix[0][0] = 1
> print(matrix)  # [[1, 0, 0], [1, 0, 0], [1, 0, 0]] - all rows modified!
> ```
>
> **Instead, always use list comprehensions or loops**:
> ```python
> # GOOD - clear and explicit
> zeros = [0 for _ in range(5)]
> matrix = [[0 for _ in range(3)] for _ in range(3)]
> ```
>
> List comprehensions are more explicit, easier to understand, and prevent the subtle reference bugs that multiplication
> can cause. They also make your code more maintainable when requirements change.

### Membership Testing

```python
fruits = ["apple", "banana", "cherry"]

print("apple" in fruits)  # True
print("grape" in fruits)  # False
print("grape" not in fruits)  # True
```

### Comparison

```python
# Lexicographic comparison
print([1, 2, 3] == [1, 2, 3])  # True
print([1, 2] < [1, 2, 3])  # True (shorter, same prefix)
print([1, 3] > [1, 2, 5])  # True (3 > 2 at index 1)
```

## Common List Methods

Lists are **mutable** (can be changed after creation).

> **Note: What does "mutable" mean?**
>
> Mutable means the list can be modified after creation—you can add, remove, or change elements without creating a new
> list. This is different from immutable types like strings or tuples, which cannot be changed once created.
>
> **Important**: When you modify a list, all variables pointing to that list see the change. This is why understanding
> list copying (covered later) is crucial to avoid unexpected bugs.

| Method         | Description                 | Example                 | Result                        |
|----------------|-----------------------------|-------------------------|-------------------------------|
| `append(x)`    | Add x to end                | `[1, 2].append(3)`      | `[1, 2, 3]`                   |
| `insert(i, x)` | Insert x at index i         | `[1, 3].insert(1, 2)`   | `[1, 2, 3]`                   |
| `extend(iter)` | Add all items from iterable | `[1, 2].extend([3, 4])` | `[1, 2, 3, 4]`                |
| `remove(x)`    | Remove first x              | `[1, 2, 1].remove(1)`   | `[2, 1]`                      |
| `pop(i)`       | Remove and return item at i | `[1, 2, 3].pop(1)`      | Returns `2`, list is `[1, 3]` |
| `index(x)`     | Index of first x            | `[1, 2, 3].index(2)`    | `1`                           |
| `count(x)`     | Count occurrences of x      | `[1, 2, 1].count(1)`    | `2`                           |
| `sort()`       | Sort in place               | `[3, 1, 2].sort()`      | `[1, 2, 3]`                   |
| `reverse()`    | Reverse in place            | `[1, 2, 3].reverse()`   | `[3, 2, 1]`                   |
| `copy()`       | Shallow copy                | `[1, 2].copy()`         | `[1, 2]`                      |
| `clear()`      | Remove all items            | `[1, 2].clear()`        | `[]`                          |

> **Note: Methods that modify in-place vs return new values**
>
> Some methods modify the list directly (in-place) and return `None`:
> - `append()`, `extend()`, `insert()`, `remove()`, `pop()`, `sort()`, `reverse()`, `clear()`
>
> Others return a new value without modifying the original:
> - `sorted(list)` returns a new sorted list (vs `list.sort()` which sorts in-place)
> - `list[:]` creates a copy (vs assignment which creates a reference)
> - `reversed(list)` returns an iterator (vs `list.reverse()` which reverses in-place)
>
> **Common mistake**: Writing `numbers = numbers.sort()` will set `numbers` to `None` because `sort()` returns `None`!

## Iterating Over Lists

| Method                 | Use Case                        | Syntax                                     | Example                                  |
|------------------------|---------------------------------|--------------------------------------------|------------------------------------------|
| Basic for loop         | Iterate over values             | `for item in list:`                        | `for fruit in fruits: print(fruit)`      |
| With enumerate         | Need index and value            | `for i, item in enumerate(list):`          | `for i, fruit in enumerate(fruits):`     |
| With enumerate (start) | Custom starting index           | `for i, item in enumerate(list, start=n):` | `for i, x in enumerate(data, start=1):`  |
| With range             | Need index to modify list       | `for i in range(len(list)):`               | `for i in range(len(fruits)):`           |
| With zip               | Iterate multiple lists together | `for a, b in zip(list1, list2):`           | `for name, score in zip(names, scores):` |
| Reversed               | Iterate in reverse order        | `for item in reversed(list):`              | `for num in reversed(numbers):`          |
| With slice             | Iterate over part of list       | `for item in list[start:stop]:`            | `for x in numbers[2:5]:`                 |
| While loop             | Complex iteration logic         | `while condition:`                         | `i = 0` <br> `while i < len(list):`      |

## Common Patterns

| Pattern                 | Built-in Approach                         | Manual Approach                                                      |
|-------------------------|-------------------------------------------|----------------------------------------------------------------------|
| **Sum**                 | `total = sum(numbers)`                    | `total = 0` <br> `for n in numbers: total += n`                      |
| **Average**             | `avg = sum(numbers) / len(numbers)`       | `total = sum(numbers)` <br> `avg = total / len(numbers)`             |
| **Maximum**             | `max_val = max(numbers)`                  | `max_val = numbers[0]` <br> `for n in numbers: ...`                  |
| **Minimum**             | `min_val = min(numbers)`                  | `min_val = numbers[0]` <br> `for n in numbers: ...`                  |
| **Count occurrences**   | `count = numbers.count(value)`            | `count = 0` <br> `for n in numbers: if n == value: count+=1`         |
| **Filter**              | `evens = [n for n in nums if n % 2 == 0]` | `evens = []` <br> `for n in nums: if n % 2 == 0: evens.append(n)`    |
| **Transform**           | `squares = [n ** 2 for n in numbers]`     | `squares = []` <br> `for n in numbers: squares.append(n**2)`         |
| **Search (membership)** | `if value in numbers:`                    | `found = False` <br> `for n in numbers: if n == value: ...`          |
| **Search (index)**      | `index = numbers.index(value)`            | `for i, n in enumerate(nums): if n == value: ...`                    |
| **Build from input**    | `nums = [int(input()) for _ in range(n)]` | `nums = []` <br> `for i in range(n): nums.append(int(input()))`      |
| **Reverse**             | `reversed_list = numbers[::-1]`           | `reversed_list = []` <br> `for i in range(len(nums)-1, -1, -1): ...` |
| **Remove duplicates**   | `unique = list(set(numbers))`             | Manual loop checking if item already in new list                     |

## List Copying

### Shallow Copy vs Reference

```python
# Reference (not a copy!)
list1 = [1, 2, 3]
list2 = list1  # list2 points to same list
list2.append(4)
print(list1)  # [1, 2, 3, 4] - modified!

# Shallow copy (creates new list)
list1 = [1, 2, 3]
list2 = list1.copy()  # or list1[:] or list(list1)
list2.append(4)
print(list1)  # [1, 2, 3] - unchanged
print(list2)  # [1, 2, 3, 4]
```

> **Note: Why is this so important?**
>
> This is one of the **most common sources of bugs** for beginners! When you write `list2 = list1`, you're not creating
> a copy—you're creating another name (reference) for the same list in memory. Think of it like two people sharing the
> same notebook: when one person writes in it, the other sees the changes.
>
> **Rule of thumb**: Use `list2 = list1.copy()` or `list2 = list1[:]` whenever you want an independent copy that can be
> modified without affecting the original.

### Copy Methods

| Method             | Syntax                 | Creates New List | Notes                             |
|--------------------|------------------------|------------------|-----------------------------------|
| Assignment (NO!)   | `list2 = list1`        | ❌ No             | Both variables point to same list |
| `.copy()` method   | `list2 = list1.copy()` | ✅ Yes            | Recommended for clarity           |
| Slice notation     | `list2 = list1[:]`     | ✅ Yes            | Common idiom                      |
| `list()` function  | `list2 = list(list1)`  | ✅ Yes            | Explicit conversion               |
| `copy` module      | `copy.copy(list1)`     | ✅ Yes            | For shallow copy                  |
| `copy` module deep | `copy.deepcopy(list1)` | ✅ Yes            | For nested lists (deep copy)      |

```python
original = [1, 2, 3]

# Three ways to copy (all equivalent for simple lists)
copy1 = original.copy()
copy2 = original[:]
copy3 = list(original)

# All are independent copies
copy1.append(4)
print(original)  # [1, 2, 3]
print(copy1)  # [1, 2, 3, 4]
```

## 2D Lists (Nested Lists)

### Creating 2D Lists

```python
# 3x3 matrix
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Create 3x4 matrix of zeros
rows, cols = 3, 4
matrix = [[0 for _ in range(cols)] for _ in range(rows)]
```

### Accessing 2D List Elements

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix[0][0])  # 1 (row 0, col 0)
print(matrix[1][2])  # 6 (row 1, col 2)
print(matrix[2][1])  # 8 (row 2, col 1)
```

### Iterating 2D Lists

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Iterate rows and columns
for row in matrix:
    for element in row:
        print(element, end=" ")
    print()

# With indices
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(matrix[i][j], end=" ")
    print()
```

## Common Mistakes

### 1. Index Out of Range

```python
numbers = [1, 2, 3]
# print(numbers[3])  # IndexError!

# Safe access
if 3 < len(numbers):
    print(numbers[3])
```

### 2. Modifying List While Iterating

```python
# WRONG
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    if num % 2 == 0:
        numbers.remove(num)  # Don't modify while iterating!

# CORRECT - iterate over copy
numbers = [1, 2, 3, 4, 5]
for num in numbers[:]:
    if num % 2 == 0:
        numbers.remove(num)

# BETTER - use list comprehension
numbers = [1, 2, 3, 4, 5]
numbers = [num for num in numbers if num % 2 != 0]
```

> **Note: Why does modifying while iterating fail?**
>
> When you modify a list during iteration (adding/removing elements), you change the list's size and structure while
> Python is trying to iterate through it. This causes elements to be skipped or processed multiple times.
>
> **Example**: If you remove an element at index 2, what was at index 3 moves to index 2, but the loop has already moved
> to index 3, skipping the element that moved!
>
> **Solution**: Either iterate over a copy (`for item in list[:]`), or use list comprehension to create a filtered list.

### 3. Creating 2D Lists Incorrectly

```python
# WRONG - creates references to same list
matrix = [[0] * 3] * 3
matrix[0][0] = 1
print(matrix)  # [[1, 0, 0], [1, 0, 0], [1, 0, 0]] - all rows modified!

# CORRECT
matrix = [[0] * 3 for _ in range(3)]
matrix[0][0] = 1
print(matrix)  # [[1, 0, 0], [0, 0, 0], [0, 0, 0]]
```

> **Note: Why does `[[0] * 3] * 3` create references?**
>
> When you use `[[0] * 3] * 3`, Python creates one inner list `[0, 0, 0]` and then creates three references to that
> **same** list. It's like making 3 variables all point to the same list!
>
> Think of it this way:
> - `[0] * 3` creates `[0, 0, 0]` (one list)
> - `[[0, 0, 0]] * 3` creates three references to that one list
>
> **Solution**: Use a list comprehension `[[0] * 3 for _ in range(3)]` which creates a new independent list in each
> iteration. The `for _ in range(3)` ensures you create 3 separate lists, not 3 references to the same list.

## Best Practices

| Practice                      | ✅ Good                               | ❌ Avoid                                 |
|-------------------------------|--------------------------------------|-----------------------------------------|
| **Transformations**           | `[x*2 for x in nums]`                | Manual loop with append                 |
| **Membership testing**        | `if item in my_list:`                | `for x in my_list: if x == item:`       |
| **Built-in functions**        | `sum(numbers)`, `max(numbers)`       | Manual loops for sum/max/min            |
| **Iteration with index**      | `for i, val in enumerate(list):`     | `for i in range(len(list)):`            |
| **Copying**                   | `new = old.copy()` or `new = old[:]` | `new = old` (creates reference!)        |
| **Naming**                    | `students`, `scores`, `temperatures` | `list1`, `data`, `arr`                  |
| **Type consistency**          | `numbers = [1, 2, 3]`                | `mixed = [1, "two", 3.0]`               |
| **Bounds checking**           | `if i < len(list): list[i]`          | Direct access without checking          |
| **Modifying while iterating** | `for item in my_list[:]:` (copy)     | `for item in my_list:` then modify      |
| **Creating 2D lists**         | `[[0]*cols for _ in range(rows)]`    | `[[0]*cols]*rows` (creates references!) |
| **Reversing**                 | `reversed_list = my_list[::-1]`      | Manual reverse with indices             |
| **Sorting**                   | `sorted(list)` or `list.sort()`      | Manual sorting algorithm                |

## Quick Reference

```python
# Creating
empty = []
numbers = [1, 2, 3]
from_range = list(range(10))

# Accessing
first = numbers[0]
last = numbers[-1]
slice = numbers[1:3]

# Modifying
numbers.append(4)  # Add to end
numbers.insert(0, 0)  # Insert at position
numbers.extend([5, 6])  # Add multiple
numbers.remove(3)  # Remove value
popped = numbers.pop()  # Remove and return last
del numbers[0]  # Delete by index

# Information
length = len(numbers)  # Size
count = numbers.count(2)  # Count occurrences
index = numbers.index(5)  # Find position
exists = 3 in numbers  # Check membership

# Sorting
numbers.sort()  # Sort in place
sorted_nums = sorted(numbers)  # Return sorted copy
numbers.reverse()  # Reverse in place

# Iteration
for item in numbers:  # Iterate values
    for i, item in enumerate(numbers):  # With index
        pass

# Common operations
total = sum(numbers)  # Sum all elements
maximum = max(numbers)  # Find maximum
minimum = min(numbers)  # Find minimum
```

## Summary

**Key Concepts:**

1. **Lists** store ordered collections of elements
2. **Indexing** starts at 0, negative indices count from end
3. **Slicing** extracts sublists with `[start:stop:step]`
4. **Lists are mutable** - can be modified after creation
5. **Many built-in methods** - append, remove, sort, etc.
6. **List comprehensions** provide concise syntax for creating lists
7. **2D lists** represent matrices and tables

Lists are fundamental to Python programming and mastering them is essential for solving complex problems efficiently!
