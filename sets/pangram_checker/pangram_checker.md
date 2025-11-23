# Pangram Checker

Check if a string contains every letter of the alphabet.

## Task

Write a function `is_pangram(text)` that returns `True` if the input string contains every letter of the English
alphabet at least once, and `False` otherwise.

- The check should be case-insensitive
- Non-letter characters (spaces, punctuation, numbers) should be ignored

## Template

```python
def is_pangram(text: str) -> bool:
    pass


if __name__ == "__main__":
    print(is_pangram("The quick brown fox jumps over the lazy dog"))  # True
    print(is_pangram("Pack my box with five dozen liquor jugs"))  # True
    print(is_pangram("Hello World"))  # False
    print(is_pangram("abcdefghijklmnopqrstuvwxyz"))  # True
    print(is_pangram("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))  # True
```

## Hint

<details>
<summary>Click to reveal hint</summary>

Extract letters from the text and check if all 26 letters are present:

```python
import string

letters_in_text = set(text.lower()) & set(string.ascii_lowercase)
return len(letters_in_text) == 26
```

Or use subset checking:

```python
alphabet = set(string.ascii_lowercase)
return alphabet <= set(text.lower())
```

</details>

## Note

A **pangram** is a sentence that uses every letter of the alphabet at least once.

Famous pangrams:

- "The quick brown fox jumps over the lazy dog" (35 letters)
- "Pack my box with five dozen liquor jugs" (32 letters)
- "Sphinx of black quartz, judge my vow" (29 letters)

**Perfect pangrams** use each letter exactly once (very rare in English):

- "Mr Jock, TV quiz PhD, bags few lynx" (26 letters)
