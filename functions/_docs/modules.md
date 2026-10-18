# Creating Your Own Modules

Any `.py` file is a module. Write functions in one file, and you can import
them into another file in the same folder, using any of the styles from
[`import.md`](import.md).

## Creating a Module

**File: `geometry.py`**

```python
import math


def circle_area(radius):
    """Calculate the area of a circle."""
    return math.pi * radius ** 2


def rectangle_area(length, width):
    """Calculate the area of a rectangle."""
    return length * width
```

**File: `main.py`**

```python
import geometry

print(geometry.circle_area(5))        # 78.53981633974483
print(geometry.rectangle_area(3, 4))  # 12
```

The module's file name must be a valid Python name: lowercase letters, digits,
and underscores, with no spaces (`my_module.py`).

## The Problem: Code That Runs on Import

When you import a module, Python runs **all** of its code, top to bottom:

**File: `calculator.py`**

```python
def add(a, b):
    return a + b


print("Testing calculator...")
print(add(5, 3))
```

**File: `main.py`**

```python
import calculator  # This runs the test code!

print(calculator.add(100, 200))
```

**Output:**

```
Testing calculator...
8
300
```

## The `if __name__ == "__main__":` Guard

Python gives every file a special variable, `__name__`:

- When you **run** the file (`uv run calculator.py`), `__name__` is `"__main__"`
- When you **import** it (`import calculator`), `__name__` is `"calculator"`

So code under this `if` runs only when you run the file directly:

**File: `calculator.py` (improved)**

```python
def add(a, b):
    return a + b


if __name__ == "__main__":
    print("Testing calculator...")
    print(add(5, 3))
```

Now `import calculator` gives you `add` without printing anything, and
`uv run calculator.py` still runs your test code. This is also how the
function exercises are checked; see
[`function_basics.md`](function_basics.md#how-function-exercises-are-checked).

## Structuring a Module

```python
# 1. Imports
import math

# 2. Constants
EARTH_RADIUS_KM = 6371


# 3. Functions
def circumference(radius):
    """Calculate the circumference of a circle."""
    return 2 * math.pi * radius


# 4. Main guard
if __name__ == "__main__":
    print(circumference(EARTH_RADIUS_KM))
```

Define functions at the top level, never inside the guard; otherwise files
that import the module can't use them.

## Don't Name Files After Built-in Modules

If your folder contains a file named `random.py`, then `import random` imports
**your** file instead of Python's module:

```python
import random

random.randint(1, 6)
# AttributeError: module 'random' has no attribute 'randint'
# (consider renaming 'random.py' since it has the same name as the
# standard library module named 'random' ...)
```

## Summary

- Any `.py` file can be imported as a module
- Importing runs the whole file, so put test code under
  `if __name__ == "__main__":`
- Order a module as imports, constants, functions, then the main guard
- Don't name your files after built-in modules
