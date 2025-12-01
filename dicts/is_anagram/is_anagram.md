# Anagram Checker

Check if two words are anagrams of each other.

## Task

Write a function `is_anagram(word1, word2)` that determines if two words are anagrams.

- Two words are anagrams if they contain the same characters with the same frequencies
- The comparison should be case-sensitive ('A' and 'a' are different)
- Words of different lengths cannot be anagrams
- Empty strings are anagrams of each other

## Template

```python
def is_anagram(word1: str, word2: str) -> bool:
    pass


if __name__ == "__main__":
    print(is_anagram("listen", "silent"))  # True
    print(is_anagram("hello", "world"))  # False
    print(is_anagram("abc", "abcd"))  # False
    print(is_anagram("test", "test"))  # True
    print(is_anagram("", ""))  # True
    print(is_anagram("a", "a"))  # True
```

## Hint

<details>
<summary>Click to reveal hint</summary>

Build frequency dictionaries for both words and compare them:

```python
if len(word1) != len(word2):
    return False

# Build frequency dict for word1
freq1 = {}
for char in word1:
    if char in freq1:
        freq1[char] = freq1[char] + 1
    else:
        freq1[char] = 1

# Build frequency dict for word2
freq2 = {}
for char in word2:
    if char in freq2:
        freq2[char] = freq2[char] + 1
    else:
        freq2[char] = 1

# Compare the two dictionaries
return freq1 == freq2
```

</details>

## Note

<details>
<summary>Click to reveal note</summary>

**Two Approaches:**

1. **Dictionary approach** (O(n) time, O(k) space where k is unique characters):
   - Build frequency maps for both words
   - Compare the dictionaries
   - More explicit about what we're checking

2. **Sorting approach** (O(n log n) time, O(n) space):
   - Sort both words and compare the sorted strings
   - Simpler code but slower for large inputs
   - `sorted(word1) == sorted(word2)`

Both approaches are valid. The dictionary approach is better for understanding character frequency patterns, while sorting is more concise.

**What is an Anagram?**

An anagram is a word or phrase formed by rearranging the letters of another word or phrase, using all original letters exactly once. Examples:
- "listen" ↔ "silent"
- "debit card" ↔ "bad credit" (phrases)
- "astronomer" ↔ "moon starer"

</details>
