# Remove Outliers

Remove the minimum and maximum values from a list of integers.

## Task

- Create a function `remove_outliers(numbers)` that takes a list of integers
- Return a new list with the minimum and maximum values removed
- If a value is duplicated at the min or max, remove only one occurrence of each
- Assume the list has at least 2 elements

## Template:

```python
def remove_outliers(numbers: list[int]) -> list[int]:
    pass


if __name__ == "__main__":
    # Test your function
    print(remove_outliers([10, 5, 8, 3]))  # [5, 8]
    print(remove_outliers([1, 1, 5, 5]))   # [1, 5]
```
