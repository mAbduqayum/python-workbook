# Python Error Handling Guide

Python uses **exceptions** to handle errors gracefully. Instead of crashing, you can catch errors and respond appropriately.

## Basic Structure

```python
try:
    # Code that might raise an exception
    result = 10 / 0
except ZeroDivisionError:
    # Handle the specific error
    print("Cannot divide by zero!")
```

## Catching Multiple Exceptions

```python
try:
    value = int(input("Enter a number: "))
    result = 10 / value
except ValueError:
    print("That's not a valid number!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
except (TypeError, AttributeError) as e:  # Catch multiple in one block
    print(f"Type or attribute error: {e}")
```

## The Full try/except/else/finally Pattern

```python
try:
    file = open("data.txt", "r")
    data = file.read()
except FileNotFoundError:
    print("File not found!")
else:
    # Runs only if NO exception occurred
    print(f"Read {len(data)} characters")
finally:
    # ALWAYS runs, regardless of exceptions
    print("Cleanup complete")
```

| Clause    | When It Runs                          |
|-----------|---------------------------------------|
| `except`  | Only if an exception occurred         |
| `else`    | Only if NO exception occurred         |
| `finally` | ALWAYS runs (exception or not)        |

## Catching All Exceptions

```python
try:
    risky_operation()
except Exception as e:  # Catches most exceptions
    print(f"Something went wrong: {e}")
```

> [!WARNING]
> Avoid bare `except:` — it catches everything including `KeyboardInterrupt` and `SystemExit`, making your program hard to stop.

```python
# Generally avoid this!
try:
    risky_operation()
except:
    print("Something went wrong")
```

## Raising Exceptions

Use `raise` to throw an exception intentionally:

```python
def validate_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    if age > 150:
        raise ValueError("Age seems unrealistic")
    return age
```

Re-raising a caught exception:

```python
try:
    validate_age(-5)
except ValueError:
    print("Logging the error...")
    raise  # Re-raises the caught exception
```

## Context Managers (Preferred for Resources)

Context managers automatically handle cleanup, even when exceptions occur:

```python
# Automatically closes file, even with exceptions
with open("data.txt", "r") as file:
    data = file.read()

# Multiple resources
with open("input.txt") as infile, open("output.txt", "w") as outfile:
    outfile.write(infile.read())
```

## Common Built-in Exceptions

| Exception            | When It Occurs                        |
|----------------------|---------------------------------------|
| `ValueError`         | Wrong value type/content              |
| `TypeError`          | Wrong type for operation              |
| `KeyError`           | Dictionary key not found              |
| `IndexError`         | List index out of range               |
| `AttributeError`     | Attribute doesn't exist               |
| `FileNotFoundError`  | File doesn't exist                    |
| `IOError`            | I/O operation failed                  |
| `ImportError`        | Module import failed                  |
| `ZeroDivisionError`  | Division by zero                      |
| `RuntimeError`       | Generic runtime error                 |

## Best Practices

| Do ✅                              | Don't ❌                               |
|------------------------------------|----------------------------------------|
| Catch specific exceptions          | Catch generic `Exception` or bare `except` |
| Use context managers for resources | Leave files/connections open           |
| Validate early, fail fast          | Silently ignore errors                 |
| Clean up in `finally`              | Use empty `except: pass` blocks        |

```python
# ❌ Bad: Silencing errors
try:
    do_something()
except:
    pass

# ✅ Good: Be specific and handle appropriately
try:
    value = int(user_input)
except ValueError:
    print("Please enter a valid number")
```

## Accessing Exception Details

```python
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"Exception type: {type(e).__name__}")  # ZeroDivisionError
    print(f"Exception message: {e}")              # division by zero
```

## Assertions (For Development Only)

Assertions are simple checks that should always be true during development:

```python
def calculate_average(numbers):
    assert len(numbers) > 0, "List cannot be empty"
    return sum(numbers) / len(numbers)
```

> [!CAUTION]
> Assertions can be disabled with `python -O`. Never use them for user input validation — use proper exception handling instead.

---

**Key Principle**: Handle exceptions at the level where you can do something meaningful about them. Let others propagate up to where they can be properly handled.
