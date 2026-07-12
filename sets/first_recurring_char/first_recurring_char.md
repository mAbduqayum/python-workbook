# First Recurring Character

Find the first character that appears a second time.

## Task

Write a function `first_recurring(text)` that returns the first character to appear a second time when reading the string from left to right.

- Return `None` if no character repeats
- The check should be case-sensitive

## Template

```python
def first_recurring(text: str) -> str | None:
    pass


if __name__ == "__main__":
    print(first_recurring("ABCA"))  # "A"
    print(first_recurring("ABCBA"))  # "B"
    print(first_recurring("ABC"))  # None
    print(first_recurring("ABBA"))  # "B"
    print(first_recurring("aAbBaA"))  # "a"
    print(first_recurring(""))  # None
```
