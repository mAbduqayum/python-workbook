# Is Sublist

Check if one list is a sublist (consecutive elements) of another.

## Task

- Create a function `is_sublist(main_list, sub)` that takes two lists
- Return True if sub appears as consecutive elements in main_list, False otherwise

## Template:

```python
def is_sublist(main_list: list, sub: list) -> bool:
    pass


if __name__ == "__main__":
    # Test your function
    print(is_sublist([1, 2, 3, 4, 5], [2, 3, 4]))  # True
    print(is_sublist([1, 2, 3, 4, 5], [2, 4]))  # False
    print(is_sublist([1, 2, 3], []))  # True
```

<details>
<summary><strong>Hint</strong></summary>

- Handle edge cases: empty sub is always a sublist
- Iterate through main_list with a sliding window
- For each position i, check if main_list[i:i+len(sub)] == sub
- Return True if found, False otherwise

</details>

## Note

- Empty list is considered a sublist of any list
- Elements must be consecutive
- [2, 4] is not a sublist of [1, 2, 3, 4, 5] because they're not consecutive
