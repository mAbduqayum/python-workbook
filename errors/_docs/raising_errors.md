# Raising Errors

So far Python has raised the exceptions. Your own code can raise them too, when
it's given something it can't work with.

## raise

`raise` stops the function at once. Nothing after it runs, and the function
returns nothing:

```python
def validate_age(age: int) -> int:
    if age < 0:
        raise ValueError("Age cannot be negative")
    if age > 150:
        raise ValueError("Age seems unrealistic")
    return age


print(validate_age(30))  # 30
print(validate_age(-5))  # Crashes: ValueError: Age cannot be negative
```

Use `ValueError` for a value that makes no sense, and `TypeError` for a value of
the wrong type. Write a message that says what was wrong.

## Why Not Just Print?

A function that prints a message and returns nothing leaves the caller with
`None`, which then causes a confusing crash somewhere else. A raised exception
can't be missed, and it lets the caller decide what to do:

```python
def validate_age(age: int) -> int:
    if age < 0:
        raise ValueError("Age cannot be negative")
    return age


try:
    validate_age(-5)
except ValueError as e:
    print(f"Invalid age: {e}")  # Invalid age: Age cannot be negative
```

## Where to Catch

An exception travels up through the calls until a `try` catches it. Catch it where
you can do something useful about it, and let it pass everywhere else.

`read_age` below has no way to ask the user again, so it doesn't catch anything.
Both its own `ValueError` and the one from `int()` reach the code that can respond:

```python
def read_age(text: str) -> int:
    age = int(text)
    if age < 0:
        raise ValueError("Age cannot be negative")
    return age


for text in ["20", "abc", "-5"]:
    try:
        print(read_age(text))
    except ValueError as e:
        print(f"Invalid age: {e}")
```

```
20
Invalid age: invalid literal for int() with base 10: 'abc'
Invalid age: Age cannot be negative
```

Sometimes you want to respond and still let the exception travel on. `raise` with
no exception, inside an `except` block, raises the same one again:

```python
def load_age(text: str) -> int:
    try:
        return int(text)
    except ValueError:
        print(f"Couldn't read the age: {text}")
        raise
```

## Check First, or Catch?

When a simple check can prevent the error, make the check:

```python
prices = {"tea": 3, "coffee": 5}
item = "juice"

if item in prices:
    print(prices[item])
else:
    print(f"No price for {item}")  # No price for juice
```

Catch the exception when only trying can tell you, as with `int()`: to check a
string in advance, you would have to write most of `int()` yourself.

## Assertions

`assert` checks something that must be true unless your own code has a bug. If the
condition is false, it raises an `AssertionError`:

```python
def average(numbers: list[float]) -> float:
    assert len(numbers) > 0, "List cannot be empty"
    return sum(numbers) / len(numbers)
```

> **Warning:** Running Python with `-O` turns assertions off. Never use them to
> check what a user typed: use an `if` and `raise` for that.

## Best Practices

| Do                                | Don't                                      |
|-----------------------------------|--------------------------------------------|
| Catch specific exceptions         | Catch generic `Exception` or bare `except` |
| Keep `try` blocks short           | Wrap a whole program in one `try`          |
| Raise early, with a clear message | Return a value that hides the problem      |
| Clean up in `finally`             | Use empty `except: pass` blocks            |
