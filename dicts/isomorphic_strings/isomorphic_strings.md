# Isomorphic Strings

Check if two strings are isomorphic.

## Task

Write a function `isomorphic_strings(s, t)` that determines if two strings are isomorphic.

- Two strings are isomorphic if characters in `s` can be replaced to get `t`
- Each character must map to exactly one character (bijection)
- Different characters cannot map to the same character
- A character can map to itself
- Strings of different lengths are not isomorphic

## Template

```python
def isomorphic_strings(s: str, t: str) -> bool:
    pass


if __name__ == "__main__":
    print(isomorphic_strings("egg", "add"))  # True
    print(isomorphic_strings("foo", "bar"))  # False
    print(isomorphic_strings("paper", "title"))  # True
    print(isomorphic_strings("ab", "abc"))  # False
    print(isomorphic_strings("abc", "abc"))  # True
    print(isomorphic_strings("", ""))  # True
```

## Hint

<details>
<summary>Click to reveal hint</summary>

Use two dictionaries to track bidirectional mapping:
- `s_to_t`: Maps characters from s to t
- `t_to_s`: Maps characters from t to s

Both mappings must be consistent:

```python
if len(s) != len(t):
    return False

s_to_t = {}
t_to_s = {}

for i in range(len(s)):
    char_s = s[i]
    char_t = t[i]

    # Check s → t mapping
    if char_s in s_to_t:
        if s_to_t[char_s] != char_t:
            return False
    else:
        s_to_t[char_s] = char_t

    # Check t → s mapping
    if char_t in t_to_s:
        if t_to_s[char_t] != char_s:
            return False
    else:
        t_to_s[char_t] = char_s

return True
```

</details>

## Note

<details>
<summary>Click to reveal note</summary>

**Why Two Dictionaries?**

We need bidirectional checking because:

1. **One dictionary isn't enough**:
   - `"ab"` and `"aa"` would pass with only `s_to_t` mapping
   - `a → a` (ok), `b → a` (ok with single dict)
   - But this violates the rule that different characters can't map to the same character

2. **Two dictionaries ensure bijection**:
   - `s_to_t`: Each character in s maps to exactly one character in t
   - `t_to_s`: Each character in t maps to exactly one character in s
   - Together they ensure one-to-one mapping

**Examples:**

Isomorphic: `"egg"` and `"add"`
- e → a, g → d, g → d
- Forward: {e: a, g: d}
- Backward: {a: e, d: g}
- Consistent!

Not isomorphic: `"foo"` and `"bar"`
- f → b, o → a, o → r
- o tries to map to both a and r - inconsistent!

**Complexity**: O(n) time, O(k) space where k is the number of unique characters.

</details>
