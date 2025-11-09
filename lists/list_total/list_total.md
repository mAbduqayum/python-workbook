# List Sum

Create a function to calculate the sum of all integers in a list.

## Template:

```python
def list_total(numbers: list[int]) -> int:
    pass


if __name__ == "__main__":
    # Test your function
    print(list_total([1, 2, 3, 4, 5]))  # 15
    print(list_total([10, -5, 3]))      # 8
    print(list_total([]))               # 0
```

## Note

- Don't use builtin `sum` function
- Empty list should return 0
