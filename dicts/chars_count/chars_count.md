# Character Count

Count the frequency of each character in a string.

## Task

Write a function `chars_count(text)` that takes a string and returns a dictionary where keys are characters and values
are their frequencies (number of occurrences).

- Count every character including spaces, punctuation, and digits
- The counting should be case-sensitive (treat 'A' and 'a' as different characters)
- Return an empty dictionary for an empty string

## Template

```python
def chars_count(text: str) -> dict[str, int]:
    pass


if __name__ == "__main__":
    print(chars_count("hello"))  # {'h': 1, 'e': 1, 'l': 2, 'o': 1}
    print(chars_count(""))  # {}
    print(chars_count("aaa"))  # {'a': 3}
    print(chars_count("hello world"))  # {'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1}
    print(chars_count("AaBbCc"))  # {'A': 1, 'a': 1, 'B': 1, 'b': 1, 'C': 1, 'c': 1}
```

## Hint

<details>
<summary>Click to reveal hint</summary>

Check if the character is already in the dictionary before incrementing:

```python
freq = {}
for char in text:
    if char in freq:
        freq[char] = freq[char] + 1
    else:
        freq[char] = 1
return freq
```

This pattern is common for frequency counting:
- Check if the character is already in the dictionary
- If yes, increment its count
- If no, initialize it to 1

</details>
