# Symmetric Difference

Find elements that are in either of two collections but not in both.

## Task

Write a function `symmetric_diff(list1, list2)` that returns a new list containing elements that are in **either** `list1` or `list2`, but **not in both**.

This is like an XOR operation for sets.

- Each element should appear only once in the result
- The order of elements does not need to be preserved

## Template

```python
def symmetric_diff(list1: list, list2: list) -> list:
    pass


if __name__ == "__main__":
    print(symmetric_diff([1, 2, 3], [2, 3, 4]))  # [1, 4] (order may vary)
    print(symmetric_diff(["a", "b", "c"], ["b", "c", "d"]))  # ['a', 'd'] (order may vary)
    print(symmetric_diff([1, 2], [1, 2]))  # []
    print(symmetric_diff([1, 2], [3, 4]))  # [1, 2, 3, 4] (order may vary)
```

## Hint

<details>
<summary>Click to reveal hint</summary>

Use the set symmetric difference operator `^` or the `.symmetric_difference()` method:

```python
set1 = set(list1)
set2 = set(list2)
return list(set1 ^ set2)
```

</details>

## Visual Example

```
list1 = [1, 2, 3]
list2 = [2, 3, 4]

    list1       list2
   +-----+     +-----+
   |  1  |     |     |
   |  +--+-----+--+  |
   |  | 2    3 |  4  |
   +--+--------+-----+
      (common)

Symmetric difference = [1, 4]  (elements NOT in the overlap)
```
