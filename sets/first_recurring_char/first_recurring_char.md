# First Recurring Character

Find the first character that appears a second time.

## Task

Write a function `first_recurring(text)` that returns the first character in the string that appears again later in the
string.

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

## Hint

<details>
<summary>Click to reveal hint</summary>

Use a set to track characters you've seen:

```python
seen = set()
for char in text:
    if char in seen:
        return char
    seen.add(char)
return None
```

</details>

## Note

<details>
<summary>Click to reveal note</summary>

This problem demonstrates the power of O(1) set lookups.

**Without sets** (using a list), checking `if char in seen` would be O(n), making the total algorithm O(n²).

**With sets**, the membership check is O(1), so the entire algorithm is O(n).

For a string with 1 million characters, that's the difference between:

- O(n²) = 1,000,000,000,000 operations
- O(n) = 1,000,000 operations

</details>
