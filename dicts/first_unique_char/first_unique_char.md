# First Unique Character

Find the first character that appears only once in a string.

## Task

Write a function `first_unique_char(text)` that returns the first character in the string that appears exactly once.

- Return `None` if no character appears exactly once
- Return `None` for empty strings
- The check should be case-sensitive
- Consider all characters including spaces and punctuation

## Template

```python
def first_unique_char(text: str) -> str | None:
    pass


if __name__ == "__main__":
    print(first_unique_char("leetcode"))  # 'l'
    print(first_unique_char("loveleetcode"))  # 'v'
    print(first_unique_char("aabbcc"))  # None
    print(first_unique_char("abcab"))  # 'c'
    print(first_unique_char("a"))  # 'a'
    print(first_unique_char(""))  # None
```

## Hint

<details>
<summary>Click to reveal hint</summary>

This requires two passes through the string:

1. First pass: Build a frequency dictionary
2. Second pass: Iterate through the original string and return the first character with count == 1

```python
# Build frequency dict
freq = {}
for char in text:
    if char in freq:
        freq[char] = freq[char] + 1
    else:
        freq[char] = 1

# Find first unique
for char in text:
    if freq[char] == 1:
        return char

return None
```

Why two passes? We need to know ALL frequencies before we can determine if the first character is unique.

</details>

## Note

<details>
<summary>Click to reveal note</summary>

**Why not return immediately when building the frequency dict?**

You might think you could return a character the first time you see it with count == 1, but this doesn't work:

```python
# WRONG approach:
freq = {}
for char in text:
    if char in freq:
        freq[char] = freq[char] + 1
    else:
        freq[char] = 1
    if freq[char] == 1:
        return char  # This would return the FIRST character seen, not first unique!
```

For "aabbcc", this would incorrectly return 'a' (the first character encountered), even though 'a' appears twice.

We need the full frequency count first, then iterate through the original string to find the first character that appears exactly once.

</details>
