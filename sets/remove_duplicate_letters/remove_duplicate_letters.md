# Remove Duplicate Letters

Remove duplicate characters from a string while preserving order.

## Task

Write a function `remove_duplicate_letters(text)` that returns a new string with duplicate characters removed.

- Preserve the order of first occurrence of each character
- The comparison should be case-sensitive ('A' and 'a' are different)

## Template

```python
def remove_duplicate_letters(text: str) -> str:
    pass


if __name__ == "__main__":
    print(remove_duplicate_letters("hello"))  # "helo"
    print(remove_duplicate_letters("mississippi"))  # "misp"
    print(remove_duplicate_letters("abcabc"))  # "abc"
    print(remove_duplicate_letters("AaAaBb"))  # "AaBb"
    print(remove_duplicate_letters(""))  # ""
```

## Hint

<details>
<summary>Click to reveal hint</summary>

Use a set to track seen characters while building the result:

```python
seen = set()
result = []
for char in text:
    if char not in seen:
        seen.add(char)
        result.append(char)
return "".join(result)
```

</details>

## Note

<details>
<summary>Click to reveal note</summary>

Why use a list instead of string concatenation?

Strings in Python are immutable. Each `result += char` creates a new string object, making it O(n²) for n characters.

Using a list with `.append()` and then `"".join()` is O(n) - much faster for long strings!

```python
# Slow O(n²)
result = ""
for char in text:
    result += char

# Fast O(n)
result = []
for char in text:
    result.append(char)
return "".join(result)
```

</details>
