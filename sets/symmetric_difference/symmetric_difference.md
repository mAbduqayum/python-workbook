# Symmetric Difference

Find elements that are in either of two collections but not in both.

## Task

Write a function `symmetric_diff(list1, list2)` that returns a new list containing elements that are in **either**
`list1` or `list2`, but **not in both**.

This is like an XOR operation for sets.

- Each element should appear only once in the result
- The order of elements does not need to be preserved

## Template

```python
def symmetric_diff(list1: list, list2: list) -> list:
    pass


if __name__ == "__main__":
    print(symmetric_diff([2, 3, 5], [3, 5, 7]))  # [2, 7] (order may vary)
    print(symmetric_diff(["a", "b", "c"], ["b", "c", "d"]))  # ['a', 'd'] (order may vary)
    print(symmetric_diff([2, 3], [2, 3]))  # []
    print(symmetric_diff([2, 3], [5, 7]))  # [2, 3, 5, 7] (order may vary)
```

## Visual Example

```
list1 = [2, 3, 5]
list2 = [3, 5, 7]

    list1       list2
   +-----+     +-----+
   |  2  |     |     |
   |  +--+-----+--+  |
   |  | 3    5 |  7  |
   +--+--------+-----+
      (common)

Symmetric difference = [2, 7]  (elements NOT in the overlap)
```
