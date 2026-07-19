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
    print(list_union([2, 3, 5], [5, 7, 11]))  # [2, 3, 5, 7, 11] (order may vary)
    print(list_union(["a", "b"], ["b", "c", "d"]))  # ['a', 'b', 'c', 'd'] (order may vary)
    print(list_union([], [2, 3]))  # [2, 3]
    print(list_union([2, 2, 3], [3, 3, 5]))  # [2, 3, 5] (order may vary)
```
