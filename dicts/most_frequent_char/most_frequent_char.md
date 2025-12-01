# Most Frequent Character

Find the character that appears most often in a string.

## Task

Write a function `most_frequent_char(text)` that returns the character that appears most frequently in the string.

- If there's a tie (multiple characters with same max frequency), return any of them
- The comparison should be case-sensitive ('A' and 'a' are different)
- Raise `ValueError` for empty strings
- Count all characters including spaces and punctuation

## Template

```python
def most_frequent_char(text: str) -> str:
    pass


if __name__ == "__main__":
    print(most_frequent_char("hello"))  # 'l'
    print(most_frequent_char("aabbcc"))  # 'a' (or 'b' or 'c' - all tied)
    print(most_frequent_char("a"))  # 'a'
    print(most_frequent_char("abcabc"))  # 'a' (or 'b' or 'c' - all tied)
    print(most_frequent_char("AaAaBb"))  # 'A'
    print(most_frequent_char("hello world"))  # 'l'
```

## Hint

<details>
<summary>Click to reveal hint</summary>

First build a frequency dictionary, then loop through to find the character with the maximum count:

```python
freq = {}
for char in text:
    if char in freq:
        freq[char] = freq[char] + 1
    else:
        freq[char] = 1

max_char = ""
max_count = 0
for char in freq:
    if freq[char] > max_count:
        max_count = freq[char]
        max_char = char

return max_char
```

The algorithm:
- Build a frequency dictionary by counting each character
- Track the character with the maximum count as you iterate
- Return the character with the highest frequency

</details>
