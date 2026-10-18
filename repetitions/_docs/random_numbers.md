# Repetition in Python - Random Numbers

Games and simulations need unpredictable values. Python's `random` module
provides them. Import it at the top of your program:

```python
import random
```

## Common Functions

| Function                  | Returns                                       | Example                | Possible Results  |
|---------------------------|-----------------------------------------------|------------------------|-------------------|
| `random.randint(a, b)`    | Random integer from `a` to `b`, both included | `random.randint(1, 6)` | `1` to `6`        |
| `random.random()`         | Random float from `0.0` to just below `1.0`   | `random.random()`      | `0.0` to `0.999…` |
| `random.choice(sequence)` | Random item from a sequence, such as a string | `random.choice("HT")`  | `"H"` or `"T"`    |

> **Note:** `randint(1, 6)` includes `6`, unlike `range(1, 6)`, which stops
> at `5`.

## Random Values in a Loop

Each call returns a new value, so calling it inside a loop simulates
repeated events.

### Example 1: Roll a Die 5 Times

```python
import random

for i in range(5):
    print(random.randint(1, 6), end=" ")
print()
```

**Output (different every run):**

```
3 6 1 1 4
```

### Example 2: Roll Until You Get a 6

```python
import random

rolls = 0
roll = 0
while roll != 6:
    roll = random.randint(1, 6)
    rolls += 1
print(f"Rolled a 6 after {rolls} rolls")
```

A `while` loop fits here because you can't know in advance how many rolls it
will take.
