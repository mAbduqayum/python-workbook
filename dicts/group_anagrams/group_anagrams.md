# Group Anagrams

Group words that are anagrams of each other.

## Task

Write a function `group_anagrams(words)` that groups words that are anagrams of each other.

- Return a list of lists, where each inner list contains words that are anagrams
- The order of groups doesn't matter
- The order of words within each group doesn't matter
- Empty list should return empty list
- Words are case-sensitive

## Template

```python
def group_anagrams(words: list[str]) -> list[list[str]]:
    pass


if __name__ == "__main__":
    print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
    # [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]

    print(group_anagrams(["abc", "def"]))
    # [['abc'], ['def']]

    print(group_anagrams(["abc", "bca", "cab"]))
    # [['abc', 'bca', 'cab']]

    print(group_anagrams([]))
    # []

    print(group_anagrams(["hello"]))
    # [['hello']]
```

## Hint

<details>
<summary>Click to reveal hint</summary>

Use a dictionary where:
- **Key**: sorted characters of the word (anagrams will have the same sorted form)
- **Value**: list of words with that sorted form

```python
groups = {}

for word in words:
    # Create a key by sorting the word's characters
    key = "".join(sorted(word))

    # Add word to the group for this key
    if key in groups:
        groups[key].append(word)
    else:
        groups[key] = [word]

result = []
for key in groups:
    result.append(groups[key])
return result
```

Example:
- "eat" → sorted: "aet"
- "tea" → sorted: "aet" (same!)
- "ate" → sorted: "aet" (same!)

All three map to the same key, so they end up in the same group.

</details>

## Note

<details>
<summary>Click to reveal note</summary>

**Complexity Analysis:**

- Time: O(n × k log k) where n is number of words, k is average word length
  - We iterate through n words: O(n)
  - For each word, we sort it: O(k log k)
  - Dictionary operations are O(1) on average

- Space: O(n × k) for storing all words and their sorted keys

**Alternative Approach:**

Instead of sorting, you could create a character frequency tuple as the key:
```python
from collections import Counter

for word in words:
    # Use tuple of character counts as key
    key = tuple(sorted(Counter(word).items()))
    groups.setdefault(key, []).append(word)
```

This has the same complexity but might be clearer about what makes words anagrams (same character frequencies).

</details>
