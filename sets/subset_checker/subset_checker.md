# Subset Checker

Determine if one collection is a subset of another.

## Task

Write a function `is_subset(subset, superset)` that returns `True` if all elements of `subset` are contained in
`superset`, and `False` otherwise.

- An empty set is a subset of any set
- A set is a subset of itself

## Template

```python
def is_subset(subset: list, superset: list) -> bool:
    pass


if __name__ == "__main__":
    print(is_subset([2, 3], [2, 3, 5, 7]))  # True
    print(is_subset([2, 11], [2, 3, 5, 7]))  # False
    print(is_subset([], [2, 3, 5]))  # True
    print(is_subset([2, 3, 5], [2, 3, 5]))  # True
    print(is_subset(["a", "b"], ["a", "b", "c"]))  # True
```
