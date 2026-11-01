# Handling Errors

Some problems only appear while a program runs. The code is correct, and then a
user types `abc` where you expected a number:

```python
age = int(input("Age: "))
print(age + 1)
```

```
Traceback (most recent call last):
  File "/home/farid/age.py", line 1, in <module>
    age = int(input("Age: "))
ValueError: invalid literal for int() with base 10: 'abc'
```

`int()` can't turn `abc` into a number, so it **raises an exception**: an object
that says what went wrong. Here it is a `ValueError`. Nothing handled the
exception, so Python stopped the program and printed this traceback. The appendix
[Debugging Your Programs](../../appendix/debugging.md) shows how to read one.

This chapter shows how to handle exceptions so that your program can carry on.

## try and except

Put the line that can fail in a `try` block, and say what to do about the failure
in an `except` block:

```python
try:
    age = int(input("Age: "))
    print(age + 1)
except ValueError:
    print("That isn't a whole number.")
```

Python runs the `try` block line by line:

- If no line raises an exception, Python skips the `except` block.
- If a line raises a `ValueError`, Python skips the rest of the `try` block and
  runs the `except` block. The program then continues after it.
- If a line raises any other exception, this `except` doesn't apply, and the
  program still crashes.

Type `20` and the program prints `21`. Type `abc` and it prints the message
instead of a traceback.

## Keep try Short

Put only the lines that can fail inside `try`. A long block catches errors you
didn't plan for, and hides real bugs:

```python
text = input("Age: ")
try:
    age = int(text)
except ValueError:
    age = 0
print(age + 1)
```

## Several Exceptions

A `try` can have one `except` for each kind of failure. Python runs the first one
that matches:

```python
try:
    value = int(input("Enter a number: "))
    result = 10 / value
except ValueError:
    print("That's not a valid number!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
```

To handle several exceptions the same way, list them in a tuple.

## The Exception's Message

`as e` gives you the exception itself, and printing it prints its message:

```python
try:
    value = int(input("Enter a number: "))
    result = 10 / value
except (ValueError, ZeroDivisionError) as e:
    print(f"Invalid input: {e}")
```

Type `0` and it prints `Invalid input: division by zero`.

## else and finally

Two more clauses are optional:

```python
try:
    value = int(input("Enter a number: "))
except ValueError:
    print("That's not a valid number!")
else:
    print(f"You entered {value}")
finally:
    print("Done")
```

| Clause    | When It Runs                       |
|-----------|------------------------------------|
| `except`  | Only if a matching exception occurred |
| `else`    | Only if no exception occurred      |
| `finally` | Always, exception or not           |

`else` keeps the `try` block short: the code that needs `value` stays out of it.
`finally` is for work that must happen however the block ends.

## Don't Silence Errors

An empty `except` hides every problem, including the bugs you need to see:

```python
# Bad: any mistake in the try block disappears
try:
    age = int(input("Age: "))
except:
    pass

# Good: name the error you expect, and respond to it
try:
    age = int(input("Age: "))
except ValueError:
    print("Please enter a whole number.")
```

> **Warning:** A bare `except:` catches everything, even `KeyboardInterrupt`,
> which is Ctrl+C, so your program becomes hard to stop. `except Exception` is
> less extreme, but it hides your bugs the same way. Name the exception you expect.

## Common Built-in Exceptions

| Exception           | When It Occurs                 | Example               |
|---------------------|--------------------------------|-----------------------|
| `ValueError`        | The right type, but a bad value | `int("abc")`         |
| `TypeError`         | The wrong type for an operation | `"a" + 1`            |
| `IndexError`        | No item at that list index     | `[1, 2][5]`           |
| `KeyError`          | No such key in a dictionary    | `{"a": 1}["b"]`       |
| `ZeroDivisionError` | Division by zero               | `10 / 0`              |
| `NameError`         | No variable by that name       | `print(totl)`         |
| `AttributeError`    | No such attribute or method    | `"a".append("b")`     |
| `ImportError`       | A module can't be imported     | `import nothing_here` |
| `FileNotFoundError` | The file doesn't exist         | `open("missing.txt")` |
