# List Intersection

Find common elements between two lists.

## Task

Write a function `list_intersection(list1, list2)` that returns a new list containing only the elements that appear in **both** input lists.

- Each element should appear only once in the result
- The order of elements does not need to be preserved

## Template

```python
def list_intersection(list1: list, list2: list) -> list:
    pass


if __name__ == "__main__":
    print(list_intersection([2, 3, 5, 7], [5, 7, 11, 13]))  # [5, 7] (order may vary)
    print(list_intersection(["a", "b", "c"], ["b", "c", "d"]))  # ['b', 'c'] (order may vary)
    print(list_intersection([2, 3], [5, 7]))  # []
    print(list_intersection([2, 2, 3, 3], [3, 3, 5, 5]))  # [3]
```
