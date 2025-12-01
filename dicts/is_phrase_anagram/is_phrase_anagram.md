# Phrase Anagram Checker

Check if two phrases are anagrams of each other, ignoring spaces and case.

## Task

Write a function `is_phrase_anagram(phrase1, phrase2)` that determines if two phrases are anagrams.

- Remove spaces before comparing
- The comparison should be case-insensitive
- Two phrases are anagrams if they contain the same letters with the same frequencies (ignoring spaces and case)
- Empty strings/phrases are anagrams of each other

## Template

```python
def is_phrase_anagram(phrase1: str, phrase2: str) -> bool:
    pass


if __name__ == "__main__":
    print(is_phrase_anagram("listen", "silent"))  # True
    print(is_phrase_anagram("conversation", "voices rant on"))  # True
    print(is_phrase_anagram("The Eyes", "They See"))  # True
    print(is_phrase_anagram("hello world", "world peace"))  # False
    print(is_phrase_anagram("abc", "a b c"))  # True
    print(is_phrase_anagram("", ""))  # True
```

## Hint

<details>
<summary>Click to reveal hint</summary>

Clean both phrases (remove spaces, convert to lowercase), then compare character frequencies:

```python
# Clean the phrases
clean1 = phrase1.lower().replace(' ', '')
clean2 = phrase2.lower().replace(' ', '')

# Build frequency dicts
freq1 = {}
for char in clean1:
    if char in freq1:
        freq1[char] = freq1[char] + 1
    else:
        freq1[char] = 1

freq2 = {}
for char in clean2:
    if char in freq2:
        freq2[char] = freq2[char] + 1
    else:
        freq2[char] = 1

# Compare
return freq1 == freq2
```

</details>

## Note

<details>
<summary>Click to reveal note</summary>

**Famous Phrase Anagrams:**

Some clever phrase anagrams in English:
- "conversation" ↔ "voices rant on"
- "the eyes" ↔ "they see"
- "a gentleman" ↔ "elegant man"
- "eleven plus two" ↔ "twelve plus one"
- "astronomer" ↔ "moon starer"

**Difference from Word Anagrams:**

The key differences in phrase anagram checking:
1. **Ignore spaces**: "a b c" = "abc"
2. **Case insensitive**: "The Eyes" = "they see"

This makes the problem more flexible but requires preprocessing the input before comparison.

</details>
