# Longest Substring Without Repeating Characters

Find the length of the longest substring without repeating characters.

## Task

Write a function `longest_substring_without_repeating(s)` that returns the length of the longest substring that contains no repeating characters.

- A substring is a contiguous sequence of characters
- Return 0 for empty strings
- Case sensitive: 'A' and 'a' are different characters
- All characters (letters, digits, spaces, punctuation) count

## Template

```python
def longest_substring_without_repeating(s: str) -> int:
    pass


if __name__ == "__main__":
    print(longest_substring_without_repeating("abcabcbb"))  # 3 ("abc")
    print(longest_substring_without_repeating("bbbbb"))  # 1 ("b")
    print(longest_substring_without_repeating("pwwkew"))  # 3 ("wke")
    print(longest_substring_without_repeating(""))  # 0
    print(longest_substring_without_repeating("a"))  # 1
    print(longest_substring_without_repeating("abcdef"))  # 6
    print(longest_substring_without_repeating("dvdf"))  # 3 ("vdf")
```

## Hint

<details>
<summary>Click to reveal hint</summary>

Use the **sliding window** technique with a dictionary to track character positions:

```python
char_index = {}  # Track last seen index of each character
max_length = 0
left = 0  # Left boundary of window

for right in range(len(s)):
    char = s[right]

    # If char seen and within current window, move left boundary
    if char in char_index and char_index[char] >= left:
        left = char_index[char] + 1

    char_index[char] = right  # Update character's position
    if right - left + 1 > max_length:  # Update max
        max_length = right - left + 1

return max_length
```

**How it works:**
- `left` and `right` define the current window (substring)
- When we find a repeat, move `left` past the previous occurrence
- Dictionary tracks the most recent index of each character
- Always track the maximum window size seen

</details>

## Note

<details>
<summary>Click to reveal note</summary>

**The Sliding Window Technique:**

This is a classic example of the sliding window pattern, one of the most important algorithmic techniques.

**Why Sliding Window?**

Naive approach (checking all substrings): O(n³)
```python
# For each starting position
for i in range(len(s)):
    # For each ending position
    for j in range(i, len(s)):
        # Check if substring has no repeats - O(n)
        if has_no_repeats(s[i:j+1]):
            max_length = max(max_length, j - i + 1)
```

Sliding window approach: O(n)
- One pass through the string
- Expand window to the right
- Shrink from left when duplicate found
- Track maximum size

**Why Dictionary for Indices?**

We could use a set to track characters in the window, but storing **indices** is more powerful:
- Tells us not just IF a character was seen, but WHERE
- Allows us to jump `left` directly to the right position
- Avoids having to remove characters one by one

**Complexity:**
- Time: O(n) - each character visited at most twice (once by right, once by left)
- Space: O(min(n, k)) where k is the character set size (alphabet size)

**Example Walkthrough** for "abcabcbb":
```
Index: 0 1 2 3 4 5 6 7
Char:  a b c a b c b b

right=0, char='a': window="a", max=1
right=1, char='b': window="ab", max=2
right=2, char='c': window="abc", max=3
right=3, char='a': duplicate! left moves to 1, window="bca", max=3
right=4, char='b': duplicate! left moves to 2, window="cab", max=3
right=5, char='c': duplicate! left moves to 3, window="abc", max=3
right=6, char='b': duplicate! left moves to 5, window="cb", max=3
right=7, char='b': duplicate! left moves to 7, window="b", max=3

Result: 3
```

</details>
