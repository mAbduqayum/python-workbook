# String Edit Distance

Create a recursive function that calculates the minimum number of operations required to transform one string into another.

The allowed operations are:
- Insert a character
- Delete a character
- Replace a character

This is also known as the Levenshtein distance.

## Template

```python
def edit_distance(s1: str, s2: str) -> int:
    pass


if __name__ == "__main__":
    print(edit_distance("kitten", "sitting"))  # 3
    print(edit_distance("", "abc"))            # 3
    print(edit_distance("abc", ""))            # 3
    print(edit_distance("abc", "abc"))         # 0
    print(edit_distance("horse", "ros"))       # 3
```

<details>
<summary>Hint</summary>

- Base case: if one string is empty, return the length of the other
- If last characters match, no operation needed for them
- Otherwise, try all three operations and take the minimum:
  - Insert: `edit_distance(s1, s2[:-1]) + 1`
  - Delete: `edit_distance(s1[:-1], s2) + 1`
  - Replace: `edit_distance(s1[:-1], s2[:-1]) + 1`

</details>
