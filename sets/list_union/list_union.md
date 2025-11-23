# List Union

Combine two lists into one without duplicates.

## Task

Write a function `list_union(list1, list2)` that returns a new list containing all unique elements from both input
lists.

- Each element should appear only once in the result
- The order of elements does not need to be preserved

## Template

```python
def list_union(list1: list, list2: list) -> list:
    pass


if __name__ == "__main__":
    print(list_union([1, 2, 3], [3, 4, 5]))  # [1, 2, 3, 4, 5] (order may vary)
    print(list_union(["a", "b"], ["b", "c", "d"]))  # ['a', 'b', 'c', 'd'] (order may vary)
    print(list_union([], [1, 2]))  # [1, 2]
    print(list_union([1, 1, 2], [2, 2, 3]))  # [1, 2, 3] (order may vary)
```

## Hint

<details>
<summary>Click to reveal hint</summary>

Use the set union operator `|` or the `.union()` method:

```python
set1 = set(list1)
set2 = set(list2)
return list(set1 | set2)
```

</details>
