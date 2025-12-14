# Flatten List

Create a recursive function that flattens a nested list.

## Template

```python
def flatten_list(lst: list) -> list:
    pass


if __name__ == "__main__":
    print(flatten_list([1, 2, 3]))           # [1, 2, 3]
    print(flatten_list([1, [2, 3], 4]))      # [1, 2, 3, 4]
    print(flatten_list([[1, 2], [3, 4]]))    # [1, 2, 3, 4]
    print(flatten_list([1, [2, [3, [4]]]]))  # [1, 2, 3, 4]
```

<details>
<summary>Hint</summary>

- Empty list returns empty list (base case)
- If element is a list, recursively flatten it
- If element is not a list, add it to result
- Use `isinstance(item, list)` to check if item is a list

</details>
