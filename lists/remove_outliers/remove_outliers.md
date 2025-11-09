# Remove Outliers

Remove the minimum and maximum values from a list of integers.

## Task

- Create a function `remove_outliers(numbers)` that takes a list of integers
- Return a new list with the minimum and maximum values removed

## Template:

```python
def remove_outliers(numbers: list[int]) -> list[int]:
    pass


if __name__ == "__main__":
    # Test your function
    print(remove_outliers([1, 2, 3, 4, 5]))  # [2, 3, 4]
    print(remove_outliers([10, 5, 8, 3]))    # [5, 8]
```

## Note

- If there are duplicate min/max values, remove only one occurrence of each
- Assume the list has at least 2 elements
- The order of remaining elements should be preserved
