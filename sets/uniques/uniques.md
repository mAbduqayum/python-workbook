# Uniques

Extract unique elements from a list.

## Task

Write a function `uniques(values)` that takes a list and returns a new list containing only the unique elements (no duplicates).

- The order of elements in the result does not need to match the original order
- Return an empty list if the input is empty

## Template

```python
def uniques(values: list) -> list:
    pass


if __name__ == "__main__":
    print(uniques([1, 2, 2, 3, 3, 3]))  # [1, 2, 3] (order may vary)
    print(uniques(["a", "b", "a", "c", "b"]))  # ['a', 'b', 'c'] (order may vary)
    print(uniques([]))  # []
    print(uniques([1, 1, 1, 1]))  # [1]
```

## Hint

<details>
<summary>Click to reveal hint</summary>

Sets automatically remove duplicates. Convert to a set, then back to a list.

```python
unique_set = set(values)
return list(unique_set)
```

</details>
