# Slice

Extract a slice of a list from start index to end index.

## Task

- Create a function `slice_list(lst, start, end)` that takes a list and two indices
- Return a new list containing elements from start to end (inclusive)

## Template:

```python
def slice_list(lst: list, start: int, end: int) -> list:
    pass


if __name__ == "__main__":
    # Test your function
    print(slice_list([1, 2, 3, 4, 5], 1, 3))  # [2, 3, 4]
    print(slice_list(['a', 'b', 'c', 'd'], 0, 2))  # ['a', 'b', 'c']
```

## Note

- Assume start and end are valid indices
- start <= end
- The result includes both start and end indices
